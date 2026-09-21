#!/usr/bin/env python3
"""Render the attributed X gallery from its source register, without network access."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def render(entries):
    lines = ['# MiniMax H3 on X · Flyne AI', '',
             '[English](../README.md) · [简体中文](../README_zh.md) · [Source register / 来源记录](../data/community-sources.json)', '',
             f'**{len(entries)} creator videos with prompt excerpts and bilingual notes.** Click each preview to watch the original video. Open the author post for the available prompt; XH3-008 is explicitly partial.', '',
             '每条案例都有视频入口、作者原帖、提示词短节选和中英解读。点击预览观看视频；完整可用文字见作者原帖，其中 XH3-008 只公开了部分提示词。', '',
             '[Try MiniMax H3 on Flyne AI](https://flyne.ai/model/minimax-h3/) · [Free no-sign-up trial / 免注册体验](https://flyne.ai/free-minimax-h3/)', '',
             '## Evidence and reuse / 核验与引用', '',
             'Post text and attached video metadata were checked on **2026-09-21** through the public FxTwitter reader because direct X requests were restricted. Discovery used the [TapVid index](https://tapvid.ai/video-prompts/minimax-h3); entries were then checked by post ID. Model identity is an author statement. This project did not regenerate or play back these videos. Dimensions describe uploaded files, not native model settings.', '',
             'XH3-001–006 reuse attributed editorial notes from [Flaq AI](https://github.com/flaqai/awesome-minimax-h3-video-prompts/tree/9fed21c196ffa5495b8f6d8de29cc77ba71eb66d); their frame observations are the upstream maintainer’s 2026-09-20 review, not a new Flyne review. XH3-007–012 are additional Flyne research.', '',
             '作者保留视频、预览图和提示词的权利，外部素材不适用本仓库 MIT 许可。视频和图片保留原站地址，不重新上传；外链失效时仍可通过帖子 ID 查找。社区案例不计入 100 条可复制配方。', '',
             '## Browse / 浏览', '', '| ID | Example / 案例 | Creator |', '|---|---|---|']
    for e in entries:
        anchor=re.sub(r'[^\w\s-]', '', f"{e['id']} {e['title']}".lower()).replace(' ', '-')
        lines.append(f"| {e['id']} | [{e['title']} · {e['title_zh']}](#{anchor}) | @{e['author']} |")
    for e in entries:
        lines += ['', f"## {e['id']} {e['title']}", '', f"**{e['title_zh']}**", '',
                  f"[![{e['title']} — @{e['author']}]({e['thumbnail_url']})]({e['source_url']}/video/1)", '',
                  f"[Watch on X]({e['source_url']}/video/1) · [MP4]({e['video_url']}) · [Author post + available prompt / 作者原帖与提示词]({e['prompt_url']})", '',
                  f"**@{e['author']}** · {e['published_at'][:10]} · {e['uploaded_width']} × {e['uploaded_height']} · {e['uploaded_duration_seconds']:.2f}s", '',
                  '**Prompt excerpt / 原文短节选:**', '', '> '+e['prompt_excerpt'], '',
                  '**Setup:** '+e['mode']+' '+e['mode_zh'], '',
                  '**What to learn:** '+e['lesson'], '', '**中文解读：** '+e['lesson_zh'], '',
                  ('**Upstream review / 上游核对：** ' if e['origin']=='flaq-mit-editorial' else '**Review limits / 核对边界：** ')+e['review']+' '+e['review_zh']]
    return '\n'.join(lines)+'\n'


if __name__ == '__main__':
    entries = json.loads((ROOT/'data/community-sources.json').read_text())['entries']
    (ROOT/'docs/x-community-showcase.md').write_text(render(entries))
    print(f'Built {len(entries)} community entries')
