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
    usage = json.loads((ROOT / 'data/recipe-usage.json').read_text())
    for record in records:
        record['usage'] = usage[record['id']]
    return records


def collect_exercises():
    """Keep learning exercises separate from the 100-recipe import catalog."""
    entries = json.loads((ROOT / 'data/community-sources.json').read_text())['entries']
    records = []
    for entry in entries:
        p = entry['practice']
        anchor = re.sub(r'[^\w\s-]', '', f"{entry['id']} {entry['title']}".lower()).replace(' ', '-')
        records.append(dict(p, origin='exercise',
                            path='docs/x-community-showcase.md#' + anchor))
    return records


def search_records(query, origin=None):
    return [r for r in collect() + collect_exercises()
            if (not origin or r['origin'] == origin)
            and query.casefold() in json.dumps(r, ensure_ascii=False).casefold()]


ROUTE_LABELS = {
    'free-text': 'Free text / 免费文字',
    'free-frames': 'Both frames / 准备首尾图',
    'adapt-duration': 'Shorten first / 先缩短时长',
    'confirm-route': 'Confirm support / 确认平台支持',
}


def category_navigation(records):
    categories = {}
    for r in records:
        if r['origin'] == 'upstream':
            path = r['path'].split('#')[0]
            categories.setdefault(path, {'name': r['category'], 'count': 0})['count'] += 1
    lines = ['## Browse by category / 按分类浏览', '',
             '| Category / 分类 | Recipes / 数量 |', '|---|---:|',
             f"| [Flyne original scenarios / Flyne 原创场景](#flyne-ai-additions--新增场景) | {sum(r['origin'] == 'flyne' for r in records)} |"]
    for path, group in categories.items():
        lines.append(f"| [{group['name']}](../{path}) | {group['count']} |")
    return lines + ['', '[Use conditions / 选择使用入口](../docs/recipe-usage.md): matching a form does not establish generation quality.', '']


def render(records):
    upstream = sum(r['origin'] == 'upstream' for r in records)
    flyne = len(records) - upstream
    exercises = len(collect_exercises())
    lines = ['# Prompt catalog / 提示词目录', '',
             f'**{len(records)} recipes**: {upstream} attributed MIT imports + {flyne} Flyne AI additions. All are untested by this project.', '',
             f'{upstream} 条引入内容保留原作者署名；{flyne} 条新增内容为概念方案，尚未实测。时长和画幅是创作目标，实际取决于所选平台。', '',
             '[Model selection](../docs/model-guide.md) · [Workflows](../docs/workflows.md) · [Evaluation](../docs/evaluation.md) · [Attribution](../THIRD_PARTY_NOTICES.md)', '',
             'Search offline: `python3 scripts/catalog.py search "product"` from the repository root.', '',
             f'Search includes the {len(records)} recipes plus {exercises} separate, untested five-second exercises: `python3 scripts/catalog.py search "FX5-002" --origin exercise --show-prompt`. Exercises are stored in [community-sources.json](../data/community-sources.json); they did not produce the linked creator videos.', '',
             f'搜索覆盖 {len(records)} 条配方和另列的 {exercises} 条五秒练习；练习尚未实测，不是社区视频的原始提示词。', '',
             *category_navigation(records),
             '## Flyne AI additions / 新增场景', '',
             '| ID | Recipe | Task | Category | Use conditions / 使用条件 |', '|---|---|---|---|---|']
    for r in records:
        if r['origin'] == 'flyne':
            lines.append(f"| {r['id']} | [{r['title']} · {r['title_zh']}](../{r['path']}) | {r['task']} | {r['category']} | {ROUTE_LABELS[r['usage']['route']]} |")
    lines += ['', '## Attributed upstream library / 引入内容', '',
              'Copyright © 2026 Flaq AI. [MIT license](../licenses/Flaq-AI-MIT.txt). Source revisions are linked in each file.', '',
              '| ID | Recipe | Category | Use conditions / 使用条件 |', '|---|---|---|---|']
    for r in records:
        if r['origin'] == 'upstream':
            lines.append(f"| {r['id']} | [{r['title']}](../{r['path']}) | {r['category']} | {ROUTE_LABELS[r['usage']['route']]} |")
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('build')
    search = sub.add_parser('search')
    search.add_argument('query')
    search.add_argument('--origin', choices=['upstream', 'flyne', 'exercise'])
    search.add_argument('--route', choices=list(ROUTE_LABELS))
    search.add_argument('--show-prompt', action='store_true')
    args = parser.parse_args()
    records = collect()
    if args.command == 'build':
        (ROOT / 'data/catalog.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
        (ROOT / 'prompts/README.md').write_text(render(records))
        print(f'Built {len(records)} recipes')
        return
    matches = search_records(args.query, args.origin)
    if args.route:
        matches = [r for r in matches if r.get('usage', {}).get('route') == args.route]
    for r in matches:
        print(f"{r['id']} | {r['title']} | {r['origin']} | {r['path']}")
        print(f"Status: {r['status']}")
        if r.get('usage'):
            print(f"Use: {ROUTE_LABELS[r['usage']['route']]} | Target: {r['usage']['target']}")
            print(f"Inputs: {r['usage']['inputs']}")
        if args.show_prompt:
            print(r['prompt'] + '\n')
            if r.get('prompt_zh'):
                print(r['prompt_zh'] + '\n')
    print(f'{len(matches)} matches')


if __name__ == '__main__':
    main()
