#!/usr/bin/env python3
"""Generate catalogs, gallery and README pages from maintained source files."""
import argparse
import json
import re
from catalog import ROOT, collect, collect_exercises, render
from community import render as render_community


def heading_anchor(text):
    return re.sub(r'[^\w\s-]', '', text.lower()).replace(' ', '-')


def featured_gallery(entries):
    lines = []
    for start in range(0, len(entries), 3):
        row = entries[start:start + 3]
        lines += ['| ' + ' | '.join(e['title'] + ' / ' + e['title_zh'] for e in row) + ' |',
                  '|' + '---|' * len(row),
                  '| ' + ' | '.join(f"[![{e['title']} — @{e['author']}]({e['thumbnail_url']})]({e['source_url']}/video/1)" for e in row) + ' |',
                  '| ' + ' | '.join(f"[@{e['author']} · Post / 原帖]({e['source_url']}) · [MP4]({e['video_url']})" for e in row) + ' |',
                  '| ' + ' | '.join(e.get('selection_note', '') for e in row) + ' |',
                  '| ' + ' | '.join(case_links(e) for e in row) + ' |', '']
    return '\n'.join(lines)


def case_links(entry):
    case = heading_anchor(f"{entry['id']} {entry['title']}")
    p = entry['practice']
    practice = heading_anchor(f"{p['id']} · {p['title']} / {p['title_zh']}")
    return (f"[Notes / 查看解读](docs/x-community-showcase.md#{case}) · "
            f"[{p['id']} / 复制五秒练习](docs/x-community-showcase.md#{practice})")


def outputs():
    records = collect()
    entries = json.loads((ROOT / 'data/community-sources.json').read_text())['entries']
    # Explicit selection is stable when new community examples are added.
    groups = json.loads((ROOT / 'data/featured-examples.json').read_text())['groups']
    by_id = {e['id']: e for e in entries}
    selected, sections = [], []
    for group in groups:
        rows = [dict(by_id[item['id']], selection_note=item['note']) for item in group['examples']]
        selected.extend(rows)
        sections += ['### ' + group['title'], '', group['description'], '', featured_gallery(rows)]
    if len(selected) != len({e['id'] for e in selected}):
        raise ValueError('Duplicate featured IDs')
    values = dict(recipes=len(records), upstream=sum(r['origin'] == 'upstream' for r in records),
                  flyne=sum(r['origin'] == 'flyne' for r in records), community=len(entries),
                  exercises=len(collect_exercises()), featured=len(selected),
                  featured_gallery='\n'.join(sections))
    result = {'data/catalog.json': json.dumps(records, ensure_ascii=False, indent=2) + '\n',
              'prompts/README.md': render(records),
              'docs/x-community-showcase.md': render_community(entries)}
    templates = sorted((ROOT / 'templates/readmes').glob('*.md.tmpl'))
    expected = {f'README{suffix}.md.tmpl' for suffix in ['', '_zh', '_ja', '_ko', '_es', '_fr', '_de', '_pt']}
    if {p.name for p in templates} != expected:
        raise ValueError('Expected one template for each of the eight README languages')
    for template in templates:
        body = re.sub(r'\{\{(\w+)\}\}', lambda m: str(values[m[1]]), template.read_text())
        result[template.name.removesuffix('.tmpl')] = body
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    stale = []
    for relative, body in outputs().items():
        path = ROOT / relative
        if args.check:
            if not path.exists() or path.read_text() != body:
                stale.append(relative)
        else:
            path.write_text(body)
    if stale:
        raise SystemExit('Run python3 scripts/build.py: ' + ', '.join(stale))
    print('Generated content is current' if args.check else 'Built catalogs, gallery and eight README pages')


if __name__ == '__main__':
    main()
