# Awesome MiniMax H3 Guide · Flyne AI

![Flyne AI MiniMax H3 field guide](assets/flyne-h3-cover.png)

<sub>封面为 AI 生成的展示配图，不是 H3 生成结果。</sub>

[English](README.md) · [简体中文](README_zh.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Français](README_fr.md) · [Deutsch](README_de.md) · [Português](README_pt.md)

面向实际交付的 MiniMax H3 音视频创作指南：**100 条提示词、模型选型、部署路线、质量与成本评估**，由 [Flyne AI](https://flyne.ai/) 品牌发布。

**84 条为注明来源的 MIT 授权引入内容，16 条为 Flyne AI 新增方案。** 本项目为独立社区资源，所有提示词均尚未由本项目独立实测，不宣称已获得对应视频效果或性能成绩。

[浏览全部 100 条](prompts/README.md) · [在 Flyne AI 使用 H3](https://flyne.ai/model/minimax-h3/) · [H3 与 H3 Max 区别](docs/model-guide.md) · [来源清单](docs/sources.md)

[5 秒上手教程](docs/quick-start.md) · [参考图目录](docs/reference-gallery.md) · [提示词写法](docs/prompting-guide.md) · [12 种模板](templates/README.md) · [本地部署](docs/deployment-guide.md) · [迁移对照](docs/migration-audit.md)

## 在 Flyne AI 使用 MiniMax H3

| 推荐的在线使用入口 | 免注册免费体验 |
|---|---|
| [MiniMax H3](https://flyne.ai/model/minimax-h3/) | [直接在线尝试 MiniMax H3](https://flyne.ai/free-minimax-h3/) |

2026-09-21 核对的免费界面提供 **5 秒、480p** 视频。建议从 [5 秒练习](docs/quick-start.md)开始；X 上的长视频可能使用不同设置与输入。

## 从一条可用镜头开始

1. 按交付目标选择提示词，不只按画面风格选择。
2. 查看参考素材分工，只使用当前界面支持的输入类型。
3. 根据平台可选时长调整分镜，第一轮只安排一个主体和一个动作。
4. 检查动作、产品结构、人物一致性与声音，每次修复一类问题。
5. 用[运行记录](templates/run-record.json)保存配置，以[质量评估表](docs/evaluation.md)验收。

可直接尝试的文字示例，FY-001 中文改写，未实测：

```text
五秒竖屏镜头：一盏无品牌的珊瑚色小台灯放在深灰桌面上。
一根手指按下台灯唯一的圆形按钮，温暖的光照亮空白笔记本。
手离开后，台灯保持静止。固定机位、柔和日光，灯体结构不变。
不要字幕、标志或多余按钮。即使静音，也能清楚理解开灯的动作。
```

[完整英文方案、验收标准与失败修复](prompts/flyne/fy-001.md)。时长与画幅是创作目标，具体以平台选项为准。

## 看视频，学提示词

12 条 X 社区案例，包含视频预览、作者原帖、提示词短节选与解读。下方展示新增的 6 条；全部 12 条案例均附独立编写、可直接复制的 5 秒 Flyne 练习，尚未实测。

[全部案例 / All examples](docs/x-community-showcase.md) · [官方示例 / Official examples](docs/official-h3-examples.md)

| 踩点西部动画片头 | 赛博杂志风音乐短片 | 曼谷街头美食短片 |
|---|---|---|
| [![Beat-synced western title sequence — @doctorwasif](https://pbs.twimg.com/amplify_video_thumb/2085599599801077760/img/koDdEvAQb0L9RUpH.jpg)](https://x.com/doctorwasif/status/2085599659326935100/video/1) | [![Cyber-grunge music-video texture — @Just_sharon7](https://pbs.twimg.com/amplify_video_thumb/2082710677236703232/img/vrShOLVqmbVPIngR.jpg)](https://x.com/Just_sharon7/status/2082711476347998615/video/1) | [![Bangkok street-food travel vlog — @nawalsehar](https://pbs.twimg.com/amplify_video_thumb/2085233539185061888/img/ZAkMSVzHz9ihLPyD.jpg)](https://x.com/nawalsehar/status/2085233880353915217/video/1) |
| [@doctorwasif · 原帖与提示词](https://x.com/doctorwasif/status/2085599659326935100) · [MP4](https://video.twimg.com/amplify_video/2085599599801077760/vid/avc1/1920x1080/aQ8Mx5ImZmjNxrZR.mp4?tag=29) | [@Just_sharon7 · 原帖与提示词](https://x.com/Just_sharon7/status/2082711476347998615) · [MP4](https://video.twimg.com/amplify_video/2082710677236703232/vid/avc1/2560x1440/yMtktSF0xjjMkSvB.mp4?tag=29) | [@nawalsehar · 原帖与提示词](https://x.com/nawalsehar/status/2085233880353915217) · [MP4](https://video.twimg.com/amplify_video/2085233539185061888/vid/avc1/2560x1440/jgQLrvA-NHvBJBx_.mp4?tag=29) |

| 参考图引导航拍路线 | 镜前护肤演示 | 海边晨间短片：延后自拍开场 |
|---|---|---|
| [![Reference-guided Barcelona drone route — @Diplomeme](https://pbs.twimg.com/amplify_video_thumb/2083056439854309376/img/DFzzmaMiGh2jLSVR.jpg)](https://x.com/Diplomeme/status/2083056488122380671/video/1) | [![Mirror-side skincare demonstration — @ZaraIrahh](https://pbs.twimg.com/amplify_video_thumb/2083010639748882432/img/l0l1V9NgcetYyhCQ.jpg)](https://x.com/ZaraIrahh/status/2083011066800242986/video/1) | [![Seaside morning with a delayed selfie reveal — @ayzalnooor24521](https://pbs.twimg.com/amplify_video_thumb/2086670800896266240/img/4IImBjQW816qaJPZ.jpg)](https://x.com/ayzalnooor24521/status/2086671141998059973/video/1) |
| [@Diplomeme · 原帖与提示词](https://x.com/Diplomeme/status/2083056488122380671) · [MP4](https://video.twimg.com/amplify_video/2083056439854309376/vid/avc1/1078x1288/s-5o20hibEjMgXgq.mp4?tag=29) | [@ZaraIrahh · 原帖与提示词](https://x.com/ZaraIrahh/status/2083011066800242986) · [MP4](https://video.twimg.com/amplify_video/2083010639748882432/vid/avc1/2560x1440/aZjO-LgvvLJfiCUF.mp4?tag=29) | [@ayzalnooor24521 · 原帖与提示词](https://x.com/ayzalnooor24521/status/2086671141998059973) · [MP4](https://video.twimg.com/amplify_video/2086670800896266240/vid/avc1/1088x720/cuQvyUS43S25Vss3.mp4?tag=29) |

XH3-008 只公开了部分提示词。视频由社区作者发布，未由 Flyne AI 重新生成；外部素材不适用本仓库 MIT 许可。

## 为下一条镜头准备参考图

11 张注明来源的参考图，每张对应提示词与制作说明。图片不是 H3 生成结果。

| Product / 产品 | Character / 角色 | Travel / 旅行 |
|---|---|---|
| [![Product](assets/gallery/midnight-observatory-tea.webp)](docs/reference-gallery.md) | [![Character](assets/gallery/clay-repair-robot.webp)](docs/reference-gallery.md) | [![Travel](assets/gallery/rain-washed-canal-morning.webp)](docs/reference-gallery.md) |

[全部参考图 / All reference images](docs/reference-gallery.md)

## 按使用场景选择

| 交付目标 | 推荐入口 | 核心验收点 |
|---|---|---|
| 广告、品牌、信息流开头 | [品牌库](prompts/upstream/01-brand-advertising.md)、[静音功能展示](prompts/flyne/fy-001.md) | 动作清楚、宣传主张真实 |
| 电商 SKU、商品配色 | [商品库](prompts/upstream/02-product-ecommerce.md)、[配色对比](prompts/flyne/fy-002.md) | 外形、材质、五金件一致 |
| 客服与员工培训 | [卡扣演示](prompts/flyne/fy-003.md)、[仓储异常](prompts/flyne/fy-010.md) | 专业人员确认操作准确 |
| SaaS 产品引导 | [UI 库](prompts/upstream/11-ui-game-digital.md)、[空状态引导](prompts/flyne/fy-005.md) | 界面状态与真实产品一致 |
| 双语服务、角色对话 | [对话库](prompts/upstream/21-character-dialogue-performance.md)、[双语欢迎](prompts/flyne/fy-006.md) | 语义、口型、人物稳定 |
| 互动叙事与拍摄预演 | [博物馆分支](prompts/flyne/fy-007.md)、[天气备选](prompts/flyne/fy-015.md) | 分支方向与镜头衔接 |
| 包装、活动与视觉设计 | [包装预演](prompts/flyne/fy-008.md)、[字幕背景](prompts/flyne/fy-009.md) | 可实现性与可读性 |
| 局部编辑与模型测试 | [季节橱窗](prompts/flyne/fy-012.md)、[参考角色测试](prompts/flyne/fy-016.md) | 不改动指定区域之外的内容 |

引入库还覆盖旅游、餐饮、时尚、电影、动画、运动、特效、音乐、教育、建筑、交通、宠物、工业与竖屏短剧。[完整目录](prompts/README.md)。

## 先分清 H3 与 H3 Max

截至 **2026-09-17**，官方 H3-Base 提供 FL2VA、Ref2VA 开放权重；H3 Max 是 fal 基于 H3 后训练的托管版本，本次核验未发现其公共权重。官方完整 2K 流程还包含托管组件。详见[模型指南及官方来源](docs/model-guide.md)。

因此，“H3 开放权重”不等于“Max 已经开源”，也不等于完整产品链路都能离线运行。本仓库 MIT 许可不覆盖模型权重；部署及商用需核对 H3 Community License 与对应服务条款。

## 让提示词变成可持续工作流

- [浏览器、本地和托管路线](docs/workflows.md)：选模式、分配素材角色、串联多镜头。
- [质量与成本评估](docs/evaluation.md)：合格率、每条可用视频成本、失败原因。
- [后续价值与研究方向](docs/opportunities.md)：产品参考库、本地化、定制、加速与互动原型。
- [来源与待核验事项](docs/sources.md)：记录官方链接、核验日期和事实边界。
- [维护路线图](ROADMAP.md)：优先补实测、兼容性与翻译，而非空泛增加数量。

开放权重的价值在于可评估、可适配与可探索的工程空间。是否值得投入，需要实际合格率、维护负担与成本验证；本文不承诺模型未来版本或商业收益。

## 离线检索与项目维护

需要 Python 3.9+，无需额外依赖或 API key。

```sh
python3 scripts/catalog.py search "product"
python3 scripts/catalog.py search "FX5-002" --origin exercise --show-prompt
python3 scripts/catalog.py search "客服" --origin flyne --show-prompt
python3 scripts/catalog.py build
python3 scripts/validate.py
```

搜索覆盖 100 条配方和另列的 12 条五秒练习。`--origin exercise` 只查练习，`--show-prompt` 显示中英文提示词；练习尚未实测，与社区视频的作者原文分开。

[结构化目录](data/catalog.json)可用于后续网站或工具。校验脚本检查数量、唯一 ID、站内链接、8 种语言入口及引入内容一致性，不执行模型推理。README 支持英、中、日、韩、西、法、德、葡；详细指南为英文并附中文说明，提示词正文以英文为准。

## Flyne AI、来源与贡献

[Flyne AI](https://flyne.ai/) 是本项目品牌及浏览器体验入口。实际额度、费用、模式和可用性以产品页面为准，不承诺永久免费，也不声称 Flyne 已提供 H3 Max 接口。

84 条引入提示词保留 **Flaq AI** 原始署名、固定版本来源和完整 MIT 许可证；没有通过改几个词将其冒充原创。新增指南、16 条新场景及工具独立标注。[第三方声明](THIRD_PARTY_NOTICES.md)。

欢迎提交真实运行记录、新场景、翻译修正与官方资料更新。参见[贡献指南](CONTRIBUTING.md)、[提示词模板](templates/prompt.md)和[行为准则](CODE_OF_CONDUCT.md)。

Flyne 新增内容采用 [MIT](LICENSE)，引入内容保留[上游 MIT](licenses/Flaq-AI-MIT.txt)。项目不代表 MiniMax 官方，产品名称属于各自权利人。

## 欢迎成为 Flyne AI 联盟合作伙伴

欢迎内容创作者、教育者、工具评测者和创意团队成为我们的合作伙伴！通过专属推荐链接分享 Flyne AI，即可按规则获得有效付费订单的推广佣金：

- 推荐用户的首笔有效付费订单：**20% 佣金**。
- 该用户注册后 **60 天内**的后续有效付费订单：**10% 佣金**。

[了解并加入 Flyne AI 联盟计划](https://flyne.ai/affiliate-program/)。订单资格、归因及佣金结算以当前联盟协议和审核结果为准。

如有问题或合作意向，欢迎联系：[contact@flyne.ai](mailto:contact@flyne.ai)。
