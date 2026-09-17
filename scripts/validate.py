#!/usr/bin/env python3
"""Check catalog consistency, attributed imports and local Markdown links."""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote
from catalog import ROOT, collect, render


def require(condition, message):
    if not condition:
        raise ValueError(message)


def anchors(path):
    seen = {}
    result = set()
    for title in re.findall(r'^#{1,6} (.+?)\s*#*$', path.read_text(), re.M):
        slug = re.sub(r'[^\w\s-]', '', title.lower()).replace(' ', '-')
        n = seen.get(slug, 0)
        seen[slug] = n + 1
        result.add(slug + (f'-{n}' if n else ''))
    return result


def main():
    records = collect()
    require(len(records) == 100, 'Expected 100 recipes')
    require(len({r['id'] for r in records}) == 100, 'Duplicate IDs')
    require(sum(r['origin'] == 'upstream' for r in records) == 84, 'Expected 84 upstream recipes')
    require(json.loads((ROOT / 'data/catalog.json').read_text()) == records, 'Run catalog.py build')
    require((ROOT / 'prompts/README.md').read_text() == render(records), 'Stale prompt index')
    for r in records:
        if r['origin'] == 'flyne':
            body = (ROOT / r['path']).read_text()
            require(re.search(r'```text\n(.*?)```', body, re.S).group(1).strip() == r['prompt'], f"Prompt mismatch: {r['id']}")
            require('not tested' in body, f"Missing status: {r['id']}")
    manifest = json.loads((ROOT / 'data/upstream-manifest.json').read_text())
    require(len(manifest['files']) == 24, 'Missing upstream files')
    for entry in manifest['files']:
        path = ROOT / entry['local_path']
        require(hashlib.sha256(path.read_bytes()).hexdigest() == entry['local_sha256'], f'Import changed: {path}')
        prompts = '\n'.join(re.findall(r'```text\n(.*?)```', path.read_text(), re.S))
        require(hashlib.sha256(prompts.encode()).hexdigest() == entry['prompt_blocks_sha256'], f'Original prompts changed: {path}')
    require('Copyright (c) 2026 Flaq AI' in (ROOT / 'licenses/Flaq-AI-MIT.txt').read_text(), 'Missing upstream copyright')
    for suffix in ['', '_zh', '_ja', '_ko', '_es', '_fr', '_de', '_pt']:
        require((ROOT / f'README{suffix}.md').exists(), f'Missing language {suffix}')
    checked = 0
    for path in ROOT.rglob('*.md'):
        if '.git' in path.parts:
            continue
        body = re.sub(r'```.*?```', '', path.read_text(), flags=re.S)
        for raw in re.findall(r'\]\(([^)]+)\)', body):
            target = raw.split(' "')[0].strip('<>')
            if re.match(r'^[a-zA-Z][\w+.-]*:', target):
                continue
            relative, _, fragment = unquote(target).partition('#')
            dest = (path.parent / relative).resolve() if relative else path
            require(dest.exists(), f'Broken link in {path.relative_to(ROOT)}: {target}')
            if fragment and dest.suffix == '.md':
                require(fragment in anchors(dest), f'Broken anchor in {path.relative_to(ROOT)}: {target}')
            checked += 1
    print(f'PASS: 100 recipes, 24 attributed imports, 8 languages, {checked} local links')
    print('External URLs and model inference are not checked by this offline validator.')


if __name__ == '__main__':
    main()
