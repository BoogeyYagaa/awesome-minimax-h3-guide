#!/usr/bin/env python3
"""Check catalog consistency, attributed imports and local Markdown links."""
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import unquote
from catalog import ROOT, collect, render
from community import render as render_community


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
    community = json.loads((ROOT / 'data/community-sources.json').read_text())['entries']
    require(len({e['id'] for e in community}) == len(community), 'Duplicate community IDs')
    require(len({e['source_url'].split('/')[-1] for e in community}) == len(community), 'Duplicate X posts')
    require((ROOT / 'docs/x-community-showcase.md').read_text() == render_community(community), 'Run community.py')
    for e in community:
        require(re.fullmatch(r'https://x.com/\w+/status/\d+', e['source_url']), 'Invalid X source')
        require(e['video_url'].startswith('https://video.twimg.com/'), 'Missing original video')
        require(e['thumbnail_url'].startswith('https://pbs.twimg.com/'), 'Missing original thumbnail')
        require(len(e['prompt_excerpt'].split()) <= 25, 'Prompt excerpt exceeds 25 words')
        require(all(e.get(k) for k in ['author', 'checked_at', 'rights', 'verification', 'prompt_status', 'lesson_zh']), 'Missing provenance')
        practice = e.get('practice', {})
        require(practice.get('duration_seconds') == 5, 'Exercise must fit the five-second free route')
        require(practice.get('input_mode') == 'text-only', 'Exercise requires unsupported free-tool inputs')
        require(practice.get('aspect_ratio') in ['16:9', '9:16', '1:1'], 'Unsupported exercise ratio')
        require(practice.get('status') == 'not-tested', 'Exercise status requires independent evidence')
        require(all(0 < len(practice.get(k, '')) <= 2000 for k in ['prompt', 'prompt_zh']), 'Exercise missing or over free-tool limit')
        review = e.get('visual_review', {})
        require(review.get('sample_count', 0) > 0 and re.fullmatch(r'[0-9a-f]{64}', review.get('video_sha256', '')), 'Missing visual-review provenance')
    require(len({e['practice']['id'] for e in community}) == len(community), 'Duplicate exercise IDs')
    imports = json.loads((ROOT / 'data/supplemental-imports.json').read_text())
    for entry in imports['files']:
        require(hashlib.sha256((ROOT / entry['local_path']).read_bytes()).hexdigest() == entry['local_sha256'], f"Supplemental import changed: {entry['local_path']}")
    audit = json.loads((ROOT / 'data/migration-audit.json').read_text())
    require(audit['source_commit'] == imports['source_commit'], 'Migration source revisions differ')
    require(len({e['source_path'] for e in audit['files']}) == len(audit['files']), 'Duplicate migration rows')
    for entry in audit['files']:
        require((ROOT / entry['destination']).exists(), f"Missing migration destination: {entry['source_path']}")
    for suffix in ['', '_zh', '_ja', '_ko', '_es', '_fr', '_de', '_pt']:
        require((ROOT / f'README{suffix}.md').exists(), f'Missing language {suffix}')
        readme = (ROOT / f'README{suffix}.md').read_text()
        require(all(url in readme for url in ['https://flyne.ai/model/minimax-h3/', 'https://flyne.ai/free-minimax-h3/', 'docs/x-community-showcase.md', 'assets/flyne-h3-cover.png']), f'Missing Flyne entry or gallery in {suffix}')
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
    print(f'PASS: {len(community)} unique attributed community videos and current gallery')
    print(f"PASS: {len(community)} five-second exercises, {len(imports['files'])} supplemental imports, {len(audit['files'])} migration rows")
    print('External URLs and model inference are not checked by this offline validator.')


if __name__ == '__main__':
    main()
