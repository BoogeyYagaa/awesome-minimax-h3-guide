# Maintain the video gallery / 持续维护视频案例

The source of truth is [data/community-sources.json](../data/community-sources.json). The gallery is generated; edit the source record first.

1. Find an original X post. Search for `"MiniMax H3" "prompt"`, `"MiniMax H3" "プロンプト"`, or `"MiniMax H3" "提示词"`. Treat indexes as leads and check the author post separately.
2. Deduplicate by numeric post ID, because authors can change handles. Confirm the post actually mentions H3 and contains a video. Separate H3 from earlier Hailuo models.
3. Record author, original URL, posting date, check date, retrieval method, thumbnail and MP4 URLs. If direct X access fails, record the public reader used and the limitation. Never infer a prompt from a video.
4. Quote at most 25 words per source post. Link to the available author text; mark partial prompts explicitly. Do not copy full third-party prompts without appropriate permission.
5. Add English and Chinese notes explaining the technique, reference inputs and known limitations. File dimensions describe an upload, not necessarily native generation. Say exactly whether you read metadata, watched the video, reviewed audio or regenerated it.
6. Run `python3 scripts/community.py` and `python3 scripts/validate.py`. Submit the JSON and generated Markdown together.

新增案例时，先核对原帖，再填写来源记录；视频与提示词不能靠猜。作者没给完整文字，就标注“部分公开”。作者改名时按帖子编号去重。外链失效时先更新记录，不要擅自重新上传作者视频。

For a removed post, retain its ID and explain removal in the changelog; remove unavailable previews from the public gallery. Additions require human editorial review. The offline validator does not verify external availability or model performance.

Use the [issue template](../.github/ISSUE_TEMPLATE/community-video.yml) to suggest a case. The repository has no automatic collection or reposting job.
