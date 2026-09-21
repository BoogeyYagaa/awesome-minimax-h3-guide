#!/usr/bin/env python3
"""Render the attributed X gallery from its source register, without network access."""
import json
import re
from pathlib import Path
from catalog import collect

ROOT = Path(__file__).resolve().parents[1]


def render(entries):
    lines = ['# MiniMax H3 on X · Flyne AI', '',
             '[English](../README.md) · [简体中文](../README_zh.md) · [Source register / 来源记录](../data/community-sources.json)', '',
             f'**{len(entries)} creator videos with prompt excerpts and bilingual notes.** Click each preview to watch the original video. Open the author post for the available prompt; XH3-008 is explicitly partial.', '',
             '每条案例都有视频入口、作者原帖、提示词短节选和中英解读。点击预览观看视频；完整可用文字见作者原帖，其中 XH3-008 只公开了部分提示词。', '',
             '**Start here:** watch the author video, read the technique, then copy the separate 5-second Flyne exercise below each entry. These original exercises are untested and did not produce the linked videos. [Free-tool instructions](quick-start.md).', '',
             '**使用顺序：** 看作者视频 → 读解读 → 复制该条下方的 5 秒练习 → 去 FlyneAI 尝试。练习是本项目另写的入门场景，尚未实测，不是作者原文，也不是所示视频的生成提示词。', '',
             '[Try MiniMax H3 on Flyne AI](https://flyne.ai/model/minimax-h3/) · [Free no-sign-up trial / 免注册体验](https://flyne.ai/free-minimax-h3/)', '',
             '## Evidence and reuse / 核验与引用', '',
             'Post text and attached video metadata were checked on **2026-09-21** through the public FxTwitter reader because direct X requests were restricted. Discovery used the [TapVid index](https://tapvid.ai/video-prompts/minimax-h3); entries were then checked by post ID. Model identity is an author statement. Flyne subsequently decoded each linked video and inspected one frame per one-second interval across its duration (180 frames total). This is sampled visual review, not continuous playback, audio review or regeneration. Dimensions describe uploaded files, not native model settings.', '',
             'XH3-001–006 reuse attributed editorial notes from [Flaq AI](https://github.com/flaqai/awesome-minimax-h3-video-prompts/tree/9fed21c196ffa5495b8f6d8de29cc77ba71eb66d); their frame observations are the upstream maintainer’s 2026-09-20 review, not a new Flyne review. XH3-007–012 are additional Flyne research.', '',
             f'作者保留视频、预览图和提示词的权利，外部素材不适用本仓库 MIT 许可。视频和图片保留原站地址，不重新上传；外链失效时仍可通过帖子 ID 查找。社区案例不计入 {len(collect())} 条可复制配方。', '',
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
        if 'visual_review' in e:
            v=e['visual_review']
            lines += ['', '**Flyne visual review / Flyne 画面核对：** '+v['observation_zh'], '',
                      f"Method: {v['method']}; {v['sample_count']} sampled frames. Audio not reviewed; not regenerated."]
        if 'practice' in e:
            p=e['practice']
            lines += ['', f"### {p['id']} · {p['title']} / {p['title_zh']}", '',
                      f"**Flyne exercise, not tested / Flyne 练习，未实测** · 5s · {p['aspect_ratio']} · Text only / 纯文字", '',
                      'This is a separate learning exercise, not the author prompt or a reconstruction of the video. Leave image inputs empty.', '',
                      '这是独立练习，不是作者原文，也不是视频复现。图片输入留空；在工具界面选择上方比例。', '',
                      '```text', p['prompt'], '```', '', '**中文可复制版：**', '', '```text', p['prompt_zh'], '```', '',
                      '**Check / 检查：** '+p['check']+' '+p['check_zh'], '',
                      '[Try this exercise / 尝试这段练习](https://flyne.ai/free-minimax-h3/) · [Advanced H3 / 进阶入口](https://flyne.ai/model/minimax-h3/)', '',
                      'Copy the prompt manually; these links do not prefill or submit a generation. / 手动复制提示词；链接不会自动填写或提交生成。']
    return '\n'.join(lines)+'\n'


if __name__ == '__main__':
    from build import outputs
    for relative, body in outputs().items():
        (ROOT / relative).write_text(body)
    print('Built all guide pages; preferred command: python3 scripts/build.py')
