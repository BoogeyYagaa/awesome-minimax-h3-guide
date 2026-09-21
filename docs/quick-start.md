# 先做一条 5 秒视频 / Make a five-second clip

从[社区案例页](x-community-showcase.md)选择一个效果，往下找到 **FX5 练习**，复制英文或中文提示词，然后打开 [FlyneAI 免注册体验工具](https://flyne.ai/free-minimax-h3/)。这 12 段练习都是另外编写的简单场景，不是视频作者的完整提示词，也没有经过本项目生成测试。

## 免费入口怎么用

2026-09-21 在未登录浏览器中读取到的界面：

| 项目 | 当前界面 |
|---|---|
| 时长与清晰度 | 5 秒、480p |
| 画幅 | 16:9、9:16、1:1 |
| 文字输入 | 最多 2000 字符 |
| 图片输入 | 可不上传；使用图片引导时上传两张，先首帧、后尾帧 |
| 注册 | 页面明确说明无需注册 |
| 提交前步骤 | 页面说明需完成验证 |

1. 复制练习提示词。先保持单场景、单动作，不要直接塞入 15 秒的复杂分镜。
2. 图片输入留空，在界面选择练习标明的画幅。
3. 提交后按页面提示完成验证。如果显示 `Queued: waiting to start generation.`，表示请求正在排队，还没有视频结果；保留当前页面等待，不要重复提交同一条。
4. 检查主体是否改变、动作是否完成、结尾是否稳定；有声音要求时另行试听。
5. 一次只改一个问题，把实际提示词、设置和结果记入[运行记录](../templates/run-record.json)。

2026-09-21 补充尝试：在已有登录状态的浏览器中提交了 FX5-002（陶瓷杯、纯文字、1:1），人工完成验证后页面显示排队。该观察不证明免注册生成成功，也不证明视频质量。

以上是界面与提交状态核对，不是成功生成记录。服务设置以后可能变化，以实际界面为准。点击仓库链接不会自动填入提示词，也不会自动提交生成。

## 什么时候用进阶入口

需要更多设置时，打开 [FlyneAI MiniMax H3](https://flyne.ai/model/minimax-h3/)，先确认界面提供的模式和输入。社区案例里的音频参考、多人物参考或长分镜，不代表免费入口支持这些输入。

| 你想做什么 | 先看什么 |
|---|---|
| 试一个简单效果 | [12 段 5 秒练习](x-community-showcase.md) |
| 找完整生产场景 | [100 条配方目录](../prompts/README.md) |
| 自己组织提示词 | [写法指南](prompting-guide.md)、[12 种模板](../templates/README.md) |
| 准备首帧和参考素材 | [参考图目录](reference-gallery.md) |
| 在本地运行模型 | [部署指南](deployment-guide.md)，先核对文中的版本日期 |

## English

Choose an FX5 exercise in the [community gallery](x-community-showcase.md), copy either language version and open the [free tool](https://flyne.ai/free-minimax-h3/). Leave image inputs empty and select the stated ratio. The unsigned-in interface inspected on 2026-09-21 showed five-second, 480p output, a 2000-character prompt limit and ratios 16:9, 9:16 and 1:1. Optional frame guidance requires both endpoint images. Follow the page verification step.

The exercises are original Flyne learning scenes, not author-prompt transcriptions or prompts that produced the linked community videos. A signed-in attempt with FX5-002 (text only, 1:1) reached the free queue after manual verification on 2026-09-21; no generated output had been reviewed at that observation. The unsigned-in interface check and this signed-in submission are separate observations. If the page says `Queued: waiting to start generation.`, keep the page open and wait; do not resubmit the same prompt. For other modes, check the [advanced H3 interface](https://flyne.ai/model/minimax-h3/) rather than assuming a community example fits the free tool.
