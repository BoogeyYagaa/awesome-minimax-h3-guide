# Maintain the video gallery / 持续维护视频案例

The source of truth is [data/community-sources.json](../data/community-sources.json). The gallery is generated; edit the source record first.

1. Find an original X post. Search for `"MiniMax H3" "prompt"`, `"MiniMax H3" "プロンプト"`, or `"MiniMax H3" "提示词"`. Treat indexes as leads and check the author post separately.
2. Deduplicate by numeric post ID, because authors can change handles. Confirm the post actually mentions H3 and contains a video. Separate H3 from earlier Hailuo models.
3. Record author, original URL, posting date, check date, retrieval method, thumbnail and MP4 URLs. If direct X access fails, record the public reader used and the limitation. Never infer a prompt from a video.
4. Quote at most 25 words per source post. Link to the available author text; mark partial prompts explicitly. Do not copy full third-party prompts without appropriate permission.
5. Add English and Chinese notes explaining the technique, reference inputs and known limitations. File dimensions describe an upload, not necessarily native generation. Say exactly whether you read metadata, watched the video, reviewed audio or regenerated it.
6. Run `python3 scripts/build.py` and `python3 scripts/validate.py`. Submit the JSON and generated Markdown together.

新增案例时，先核对原帖，再填写来源记录；视频与提示词不能靠猜。作者没给完整文字，就标注“部分公开”。作者改名时按帖子编号去重。外链失效时先更新记录，不要擅自重新上传作者视频。

For a removed post, retain its ID and explain removal in the changelog; remove unavailable previews from the public gallery. Additions require human editorial review. The offline validator does not verify external availability or model performance.

Use the [issue template](../.github/ISSUE_TEMPLATE/community-video.yml) to suggest a case. The repository has no automatic collection or reposting job.

## Five-second exercises and visual review

Each entry can contain a `practice` record with a unique FX5 ID, English and Chinese prompts, a five-second target, one of the observed free-tool ratios, and `not-tested` status. Keep it a new learning scene; do not paraphrase a third-party prompt into purported Flyne authorship. The generated gallery keeps the original author excerpt separate.

Visual review records include method, sample count, video hash and observations. One-frame-per-second sampling cannot establish exact cuts, smooth motion or audio synchronization. Record those limits. Do not commit temporary third-party MP4s or contact sheets.


## 一次更新，生成所有入口

- 社区案例：修改 `data/community-sources.json`。
- 首页精选：修改 `data/featured-examples.json` 的分组、案例编号和选择理由；区分方法学习与偏差分析。生成脚本自动补齐解读和独立练习的直达链接。
- 八种语言首页：修改 `templates/readmes/*.md.tmpl`。`{{recipes}}`、`{{upstream}}`、`{{flyne}}`、`{{community}}` 等标记由生成脚本填入。
- 新增配方：同时更新配方 Markdown 和 `data/flyne-recipes.json`；引入内容的固定版本、署名和哈希校验仍需保留。

```sh
python3 scripts/build.py
python3 scripts/build.py --check
python3 scripts/validate.py
python3 -m unittest discover -s scripts -p 'test_*.py'
```

生成脚本同步八种语言的数量、提示词目录、社区案例目录和中英文首页精选。详细教程与历史变更记录中的旧日期和历史数量不会被自动改写。不要直接修改生成后的首页；自动检查会指出未同步的文件。

## 每周检查外链

[Check external links](https://github.com/flyneai/awesome-minimax-h3-guide/actions/workflows/external-links.yml) 每周一北京时间 09:23 检查社区原帖、提示词地址、视频、缩略图、官方示例媒体和两个 Flyne 入口。也可在 Actions 页面手动运行。定时任务可能延迟；仓库长期无活动时可能被 GitHub 停用，参见 [GitHub 定时任务说明](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)。

结果显示在该次运行摘要中，JSON 和 Markdown 报告保留 30 天。检查只读响应头，不下载完整视频，不自动删除条目或更改作者信息。

- `reachable`：地址可响应，媒体类型符合预期；不代表视频已播放或提示词完整。
- `restricted`：401、403 或 429，表示访问限制或限流，不判定内容被删除。
- `unavailable`：再次请求后仍为 404 或 410，列入人工复核并使任务失败。
- `unexpected-content`：视频或图片地址返回了其他内容类型，列入人工复核并使任务失败。
- `temporary-error`、`network-error`、`needs-review`：暂时错误或不确定结果，在报告中保留，不能当作永久失效。

本地检查：

```sh
python3 scripts/check_external_links.py --output-dir /tmp/flyne-link-report
```

检查任务只生成报告；发现异常后，人工查看原帖，再决定更换地址或移除预览。生成检查和外链检查分别运行，外站限流不会阻止正常文档提交。


## 首页图片与分类说明

首页使用 `assets/previews/` 中的轻量 WebP 文件，点击图片打开原图。原文件、许可和生成记录保留不变。封面最长边 1600 像素，卡片图最长边 640 像素，保持比例、不裁剪。质量参数为 82；变换记录和源文件、预览文件哈希保存在 `data/image-previews.json`。

仅重新生成图片时需要 Pillow，日常生成文档与自动检查不需要它：

```sh
python3 -m venv .venv
.venv/bin/pip install Pillow
.venv/bin/python scripts/preview_images.py
python3 scripts/build.py
python3 scripts/validate.py
```

分类中文名称与中英文用途维护在 `data/category-descriptions.json`；分类编号范围和数量由配方数据生成。新增分类时检查脚本会提示补齐说明。旧的 `catalog.py build` 和 `community.py` 命令仍可运行，但会转为完整生成；统一推荐 `python3 scripts/build.py`。
