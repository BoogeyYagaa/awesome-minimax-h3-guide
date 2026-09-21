# 迁移对照 / Migration audit

对照源仓库固定版本 [`9fed21c`](https://github.com/flaqai/awesome-minimax-h3-video-prompts/tree/9fed21c196ffa5495b8f6d8de29cc77ba71eb66d)，逐项登记 **69 个文件**。本表说明复用、替换及已有对应内容，不表示把所有文件原样复制。

本次补入 8 份教程与模板文档、11 张参考图。24 个分类文件的 84 条提示词与源版本正文一致。目标仓库原有 16 条 Flyne 配方保留；新增 12 段入门练习放在社区案例页，单独计数。源封面由 Flyne 封面替代，Flaq 合作条款不迁入。

技术教程保留原有核验日期；导入不代表本地部署已经成功，也不代表每个示例支持免费入口。免费工具的本次界面核对见[快速开始](quick-start.md)。

[机器可读记录](../data/migration-audit.json) · [导入文件校验值](../data/supplemental-imports.json) · [许可说明](../THIRD_PARTY_NOTICES.md)

| 源文件 | 本项目对应内容 | 处理说明 |
|---|---|---|
| `.github/ISSUE_TEMPLATE/config.yml` | [CONTRIBUTING.md](../CONTRIBUTING.md) | 源仓库配置不直接覆盖本项目，贡献入口保留在本地指南。 |
| `.github/ISSUE_TEMPLATE/documentation.yml` | [CONTRIBUTING.md](../CONTRIBUTING.md) | 源仓库配置不直接覆盖本项目，贡献入口保留在本地指南。 |
| `.github/ISSUE_TEMPLATE/prompt-proposal.yml` | [CONTRIBUTING.md](../CONTRIBUTING.md) | 使用现有贡献说明与提示词模板。 |
| `.github/PULL_REQUEST_TEMPLATE.md` | [.github/pull_request_template.md](../.github/pull_request_template.md) | 保留 FlyneAI 现有管理文件，避免覆盖贡献规则或历史。 |
| `.gitignore` | [.gitignore](../.gitignore) | 保留 FlyneAI 现有管理文件，避免覆盖贡献规则或历史。 |
| `CHANGELOG.md` | [CHANGELOG.md](../CHANGELOG.md) | 保留 FlyneAI 现有管理文件，避免覆盖贡献规则或历史。 |
| `CODE_OF_CONDUCT.md` | [CODE_OF_CONDUCT.md](../CODE_OF_CONDUCT.md) | 保留 FlyneAI 现有管理文件，避免覆盖贡献规则或历史。 |
| `CONTRIBUTING.md` | [CONTRIBUTING.md](../CONTRIBUTING.md) | 保留 FlyneAI 现有管理文件，避免覆盖贡献规则或历史。 |
| `LICENSE` | [licenses/Flaq-AI-MIT.txt](../licenses/Flaq-AI-MIT.txt) | 上游许可全文保留；根目录许可覆盖 Flyne 新增内容。 |
| `README.md` | [README.md](../README.md) | 使用 FlyneAI 八语言入口，保留现有内容，补齐教程与案例导航。 |
| `README_de.md` | [README_de.md](../README_de.md) | 使用 FlyneAI 八语言入口，保留现有内容，补齐教程与案例导航。 |
| `README_es.md` | [README_es.md](../README_es.md) | 使用 FlyneAI 八语言入口，保留现有内容，补齐教程与案例导航。 |
| `README_fr.md` | [README_fr.md](../README_fr.md) | 使用 FlyneAI 八语言入口，保留现有内容，补齐教程与案例导航。 |
| `README_ja.md` | [README_ja.md](../README_ja.md) | 使用 FlyneAI 八语言入口，保留现有内容，补齐教程与案例导航。 |
| `README_ko.md` | [README_ko.md](../README_ko.md) | 使用 FlyneAI 八语言入口，保留现有内容，补齐教程与案例导航。 |
| `README_pt.md` | [README_pt.md](../README_pt.md) | 使用 FlyneAI 八语言入口，保留现有内容，补齐教程与案例导航。 |
| `README_zh.md` | [README_zh.md](../README_zh.md) | 使用 FlyneAI 八语言入口，保留现有内容，补齐教程与案例导航。 |
| `ROADMAP.md` | [ROADMAP.md](../ROADMAP.md) | 保留 FlyneAI 现有管理文件，避免覆盖贡献规则或历史。 |
| `assets/README.md` | [docs/reference-gallery.md](../docs/reference-gallery.md) | 图片用途、配方及制作说明映射到新的参考图目录。 |
| `assets/gallery/clay-repair-robot.webp` | [assets/gallery/clay-repair-robot.webp](../assets/gallery/clay-repair-robot.webp) | 保留署名及 MIT 许可；文档调整站内链接，参考图原样复用。 |
| `assets/gallery/dynamic-night-market-poster.webp` | [assets/gallery/dynamic-night-market-poster.webp](../assets/gallery/dynamic-night-market-poster.webp) | 保留署名及 MIT 许可；文档调整站内链接，参考图原样复用。 |
| `assets/gallery/honest-desk-lamp-demo.webp` | [assets/gallery/honest-desk-lamp-demo.webp](../assets/gallery/honest-desk-lamp-demo.webp) | 保留署名及 MIT 许可；文档调整站内链接，参考图原样复用。 |
| `assets/gallery/indoor-climbing-final-hold.webp` | [assets/gallery/indoor-climbing-final-hold.webp](../assets/gallery/indoor-climbing-final-hold.webp) | 保留署名及 MIT 许可；文档调整站内链接，参考图原样复用。 |
| `assets/gallery/midnight-observatory-tea.webp` | [assets/gallery/midnight-observatory-tea.webp](../assets/gallery/midnight-observatory-tea.webp) | 保留署名及 MIT 许可；文档调整站内链接，参考图原样复用。 |
| `assets/gallery/modular-lunch-jar-kit.webp` | [assets/gallery/modular-lunch-jar-kit.webp](../assets/gallery/modular-lunch-jar-kit.webp) | 保留署名及 MIT 许可；文档调整站内链接，参考图原样复用。 |
| `assets/gallery/paper-birds-storm-shelter.webp` | [assets/gallery/paper-birds-storm-shelter.webp](../assets/gallery/paper-birds-storm-shelter.webp) | 保留署名及 MIT 许可；文档调整站内链接，参考图原样复用。 |
| `assets/gallery/radial-cork-speaker.webp` | [assets/gallery/radial-cork-speaker.webp](../assets/gallery/radial-cork-speaker.webp) | 保留署名及 MIT 许可；文档调整站内链接，参考图原样复用。 |
| `assets/gallery/rain-washed-canal-morning.webp` | [assets/gallery/rain-washed-canal-morning.webp](../assets/gallery/rain-washed-canal-morning.webp) | 保留署名及 MIT 许可；文档调整站内链接，参考图原样复用。 |
| `assets/gallery/three-biome-museum-rail.webp` | [assets/gallery/three-biome-museum-rail.webp](../assets/gallery/three-biome-museum-rail.webp) | 保留署名及 MIT 许可；文档调整站内链接，参考图原样复用。 |
| `assets/gallery/topographic-map-archive.webp` | [assets/gallery/topographic-map-archive.webp](../assets/gallery/topographic-map-archive.webp) | 保留署名及 MIT 许可；文档调整站内链接，参考图原样复用。 |
| `assets/hero-minimax-h3-video-prompts.webp` | [assets/flyne-h3-cover.png](../assets/flyne-h3-cover.png) | 由 FlyneAI 专属封面替代，不复制 Flaq 仓库封面。 |
| `assets/minimax-h3-reference-image-prompts.md` | [assets/minimax-h3-reference-image-prompts.md](../assets/minimax-h3-reference-image-prompts.md) | 保留署名及 MIT 许可；文档调整站内链接，参考图原样复用。 |
| `docs/affiliate-program.md` | [README.md](../README.md) | 保留既有 FlyneAI 合作入口；不迁移 Flaq 的商业条款。 |
| `docs/api-workflow.md` | [docs/api-workflow.md](../docs/api-workflow.md) | 保留署名及 MIT 许可；文档调整站内链接，参考图原样复用。 |
| `docs/deployment-guide.md` | [docs/deployment-guide.md](../docs/deployment-guide.md) | 保留署名及 MIT 许可；文档调整站内链接，参考图原样复用。 |
| `docs/minimax-h3-overview.md` | [docs/model-guide.md](../docs/model-guide.md) | 继续使用现有模型说明，不重复叠加概述页。 |
| `docs/multilingual-prompting.md` | [docs/multilingual-prompting.md](../docs/multilingual-prompting.md) | 保留署名及 MIT 许可；文档调整站内链接，参考图原样复用。 |
| `docs/official-h3-examples.md` | [docs/official-h3-examples.md](../docs/official-h3-examples.md) | 保留官方媒体链接，导航改为 FlyneAI。 |
| `docs/originality-policy.md` | [docs/originality-policy.md](../docs/originality-policy.md) | 保留署名及 MIT 许可；文档调整站内链接，参考图原样复用。 |
| `docs/prompting-guide.md` | [docs/prompting-guide.md](../docs/prompting-guide.md) | 保留署名及 MIT 许可；文档调整站内链接，参考图原样复用。 |
| `docs/use-case-matrix.md` | [docs/use-case-matrix.md](../docs/use-case-matrix.md) | 保留署名及 MIT 许可；文档调整站内链接，参考图原样复用。 |
| `docs/x-community-showcase.md` | [docs/x-community-showcase.md](../docs/x-community-showcase.md) | 十二条视频与独立五秒练习，明确作者原文和练习区别。 |
| `docs/x-community-sources.json` | [data/community-sources.json](../data/community-sources.json) | 保留六条来源记录，扩展至十二条并添加视觉核对及练习。 |
| `prompts/01-brand-advertising.md` | [prompts/upstream/01-brand-advertising.md](../prompts/upstream/01-brand-advertising.md) | 与本次固定源版本逐块比较，提示词正文一致。 |
| `prompts/02-product-ecommerce.md` | [prompts/upstream/02-product-ecommerce.md](../prompts/upstream/02-product-ecommerce.md) | 与本次固定源版本逐块比较，提示词正文一致。 |
| `prompts/03-ugc-lifestyle.md` | [prompts/upstream/03-ugc-lifestyle.md](../prompts/upstream/03-ugc-lifestyle.md) | 与本次固定源版本逐块比较，提示词正文一致。 |
| `prompts/04-travel-hospitality.md` | [prompts/upstream/04-travel-hospitality.md](../prompts/upstream/04-travel-hospitality.md) | 与本次固定源版本逐块比较，提示词正文一致。 |
| `prompts/05-food-beverage.md` | [prompts/upstream/05-food-beverage.md](../prompts/upstream/05-food-beverage.md) | 与本次固定源版本逐块比较，提示词正文一致。 |
| `prompts/06-fashion-beauty.md` | [prompts/upstream/06-fashion-beauty.md](../prompts/upstream/06-fashion-beauty.md) | 与本次固定源版本逐块比较，提示词正文一致。 |
| `prompts/07-cinematic-storytelling.md` | [prompts/upstream/07-cinematic-storytelling.md](../prompts/upstream/07-cinematic-storytelling.md) | 与本次固定源版本逐块比较，提示词正文一致。 |
| `prompts/08-animation-stylized.md` | [prompts/upstream/08-animation-stylized.md](../prompts/upstream/08-animation-stylized.md) | 与本次固定源版本逐块比较，提示词正文一致。 |
| `prompts/09-action-sports.md` | [prompts/upstream/09-action-sports.md](../prompts/upstream/09-action-sports.md) | 与本次固定源版本逐块比较，提示词正文一致。 |
| `prompts/10-fantasy-scifi-vfx.md` | [prompts/upstream/10-fantasy-scifi-vfx.md](../prompts/upstream/10-fantasy-scifi-vfx.md) | 与本次固定源版本逐块比较，提示词正文一致。 |
| `prompts/11-ui-game-digital.md` | [prompts/upstream/11-ui-game-digital.md](../prompts/upstream/11-ui-game-digital.md) | 与本次固定源版本逐块比较，提示词正文一致。 |
| `prompts/12-transitions-comedy-social.md` | [prompts/upstream/12-transitions-comedy-social.md](../prompts/upstream/12-transitions-comedy-social.md) | 与本次固定源版本逐块比较，提示词正文一致。 |
| `prompts/13-music-performance-audio.md` | [prompts/upstream/13-music-performance-audio.md](../prompts/upstream/13-music-performance-audio.md) | 与本次固定源版本逐块比较，提示词正文一致。 |
| `prompts/14-education-documentary-science.md` | [prompts/upstream/14-education-documentary-science.md](../prompts/upstream/14-education-documentary-science.md) | 与本次固定源版本逐块比较，提示词正文一致。 |
| `prompts/15-architecture-interiors-real-estate.md` | [prompts/upstream/15-architecture-interiors-real-estate.md](../prompts/upstream/15-architecture-interiors-real-estate.md) | 与本次固定源版本逐块比较，提示词正文一致。 |
| `prompts/16-automotive-mobility.md` | [prompts/upstream/16-automotive-mobility.md](../prompts/upstream/16-automotive-mobility.md) | 与本次固定源版本逐块比较，提示词正文一致。 |
| `prompts/17-nature-animals-pets.md` | [prompts/upstream/17-nature-animals-pets.md](../prompts/upstream/17-nature-animals-pets.md) | 与本次固定源版本逐块比较，提示词正文一致。 |
| `prompts/18-industry-business-public-service.md` | [prompts/upstream/18-industry-business-public-service.md](../prompts/upstream/18-industry-business-public-service.md) | 与本次固定源版本逐块比较，提示词正文一致。 |
| `prompts/19-editing-continuation-localization.md` | [prompts/upstream/19-editing-continuation-localization.md](../prompts/upstream/19-editing-continuation-localization.md) | 与本次固定源版本逐块比较，提示词正文一致。 |
| `prompts/20-multireference-camera-transfer.md` | [prompts/upstream/20-multireference-camera-transfer.md](../prompts/upstream/20-multireference-camera-transfer.md) | 与本次固定源版本逐块比较，提示词正文一致。 |
| `prompts/21-character-dialogue-performance.md` | [prompts/upstream/21-character-dialogue-performance.md](../prompts/upstream/21-character-dialogue-performance.md) | 与本次固定源版本逐块比较，提示词正文一致。 |
| `prompts/22-motion-graphics-dynamic-posters.md` | [prompts/upstream/22-motion-graphics-dynamic-posters.md](../prompts/upstream/22-motion-graphics-dynamic-posters.md) | 与本次固定源版本逐块比较，提示词正文一致。 |
| `prompts/23-surreal-physics-optical-illusions.md` | [prompts/upstream/23-surreal-physics-optical-illusions.md](../prompts/upstream/23-surreal-physics-optical-illusions.md) | 与本次固定源版本逐块比较，提示词正文一致。 |
| `prompts/24-vertical-series-live-creator.md` | [prompts/upstream/24-vertical-series-live-creator.md](../prompts/upstream/24-vertical-series-live-creator.md) | 与本次固定源版本逐块比较，提示词正文一致。 |
| `prompts/README.md` | [prompts/README.md](../prompts/README.md) | 继续使用本项目自动生成的 100 条目录。 |
| `templates/README.md` | [templates/README.md](../templates/README.md) | 保留署名及 MIT 许可；文档调整站内链接，参考图原样复用。 |
