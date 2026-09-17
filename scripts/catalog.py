#!/usr/bin/env python3
"""Build or search the offline prompt catalog; no third-party dependencies."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def collect():
    records = []
    for path in sorted((ROOT / 'prompts/upstream').glob('*.md')):
        text = path.read_text()
        category = re.search(r'^# (.+)', text, re.M).group(1)
        for match in re.finditer(r'^## ([A-Z]+-\d{3}) ([^\n]+)\n(.*?)(?=^## |\Z)', text, re.M | re.S):
            recipe_id, title, body = match.groups()
            prompt = re.search(r'```text\n(.*?)```', body, re.S)
            if not prompt:
                raise ValueError(f'Missing prompt: {recipe_id}')
            anchor = re.sub(r'[^\w\s-]', '', f'{recipe_id} {title}'.lower()).replace(' ', '-')
            records.append(dict(id=recipe_id, title=title, category=category,
                                task='see-recipe', origin='upstream', status='not-tested-by-flyne',
                                path=str(path.relative_to(ROOT)) + '#' + anchor,
                                prompt=prompt.group(1).strip()))
    records.extend(json.loads((ROOT / 'data/flyne-recipes.json').read_text()))
    return records


def render(records):
    lines = ['# Prompt catalog / 提示词目录', '',
             f'**{len(records)} recipes**: 84 attributed MIT imports + 16 Flyne AI additions. All are untested by this project.', '',
             '84 条引入内容保留原作者署名；16 条新增内容为概念方案，尚未实测。时长和画幅是创作目标，实际取决于所选平台。', '',
             '[Model selection](../docs/model-guide.md) · [Workflows](../docs/workflows.md) · [Evaluation](../docs/evaluation.md) · [Attribution](../THIRD_PARTY_NOTICES.md)', '',
             'Search offline: `python3 scripts/catalog.py search "product"` from the repository root.', '',
             '## Flyne AI additions / 新增场景', '',
             '| ID | Recipe | Task | Category |', '|---|---|---|---|']
    for r in records:
        if r['origin'] == 'flyne':
            lines.append(f"| {r['id']} | [{r['title']} · {r['title_zh']}](../{r['path']}) | {r['task']} | {r['category']} |")
    lines += ['', '## Attributed upstream library / 引入内容', '',
              'Copyright © 2026 Flaq AI. [MIT license](../licenses/Flaq-AI-MIT.txt). Source revisions are linked in each file.', '',
              '| ID | Recipe | Category |', '|---|---|---|']
    for r in records:
        if r['origin'] == 'upstream':
            lines.append(f"| {r['id']} | [{r['title']}](../{r['path']}) | {r['category']} |")
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('build')
    search = sub.add_parser('search')
    search.add_argument('query')
    search.add_argument('--origin', choices=['upstream', 'flyne'])
    search.add_argument('--show-prompt', action='store_true')
    args = parser.parse_args()
    records = collect()
    if args.command == 'build':
        (ROOT / 'data/catalog.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
        (ROOT / 'prompts/README.md').write_text(render(records))
        print(f'Built {len(records)} recipes')
        return
    matches = [r for r in records if (not args.origin or r['origin'] == args.origin)
               and args.query.casefold() in json.dumps(r, ensure_ascii=False).casefold()]
    for r in matches:
        print(f"{r['id']} | {r['title']} | {r['origin']} | {r['path']}")
        if args.show_prompt:
            print(r['prompt'] + '\n')
    print(f'{len(matches)} matches')


if __name__ == '__main__':
    main()
