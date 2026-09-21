# Awesome MiniMax H3 Guide · Flyne AI

[![Flyne AI MiniMax H3 field guide](assets/previews/flyne-h3-cover.webp)](assets/flyne-h3-cover.png)

<sub>AI-generated editorial cover; not an H3 output.</sub>

[English](README.md) · [简体中文](README_zh.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Français](README_fr.md) · [Deutsch](README_de.md) · [Português](README_pt.md)

A practical, source-backed library for making useful audiovisual clips with MiniMax H3: **100 prompts, production workflows, model selection and an evaluation protocol**. Published by [Flyne AI](https://flyne.ai/).

**84 prompts are attributed MIT-licensed imports; 16 are new Flyne AI recipes.** This is an independent community project. No recipe has been independently tested by this project; there are no generated-output or benchmark claims.

[Browse 100 prompts](prompts/README.md) · [Try H3 on Flyne AI](https://flyne.ai/model/minimax-h3/) · [H3 vs H3 Max](docs/model-guide.md) · [Sources](docs/sources.md)

[Five-second quick start](docs/quick-start.md) · [Reference images](docs/reference-gallery.md) · [Prompting guide](docs/prompting-guide.md) · [12 templates](templates/README.md) · [Deployment](docs/deployment-guide.md) · [Migration audit](docs/migration-audit.md)

[Choose a recipe by deliverable](docs/use-case-matrix.md) · [Prompts in other languages](docs/multilingual-prompting.md) · [API integration](docs/api-workflow.md)

**On this page:** [Write a prompt](#build-a-prompt-you-can-adapt) · [Creator examples](#watch-creator-videos-and-study-the-prompts) · [Reference images](#reference-images-for-your-next-shot) · [All categories](#all-24-recipe-categories) · [Official resources](#official-resources-and-downloads)

## Try MiniMax H3 on Flyne AI

| Recommended browser access | Free browser trial |
|---|---|
| [MiniMax H3](https://flyne.ai/model/minimax-h3/) | [Start with a quick online experiment](https://flyne.ai/free-minimax-h3/) |

The page advertises no-sign-up access. On 2026-09-21 the free interface showed controls for **5-second, 480p** clips. Start with the [five-second exercises](docs/quick-start.md); longer X examples may require other settings and inputs.

## Start with one usable shot

1. Pick a delivery problem from the table below.
2. Read the recipe's reference map. Use only inputs accepted by your selected interface.
3. Adapt the timing to its available duration. Start with one subject and one action.
4. Generate, inspect and fix one failure type at a time.
5. Save a [run record](templates/run-record.json); approve against the [quality rubric](docs/evaluation.md).

Quick text-only idea, FY-001 (conceptual):

```text
A five-second vertical shot of an unbranded coral desk lamp on a slate desk.
One finger presses its single button; a warm pool of light appears on a blank
notebook. The hand leaves and the lamp holds still. Fixed camera, soft daylight,
stable geometry, no captions or logos. The action must be clear with sound off.
```

[Full recipe, acceptance criteria and recovery](prompts/flyne/fy-001.md). Duration and aspect ratio are creative targets, not guaranteed API options.

## Build a prompt you can adapt

Start with the copyable shot above, then use this structure when your scene needs more control. Replace the brackets and remove fields that do not apply. Reference roles describe creative intent; upload only inputs supported by your tool.

```text
Reference map: [what each image, video or audio input controls; or none]
Deliverable: [audience, purpose, aspect ratio and available duration]
Scene: [subject, setting, lighting and visible style]
Timeline: [opening state → one action → settled ending]
Camera: [framing, movement and whether cuts are allowed]
Keep unchanged: [identity, product geometry, wardrobe and environment]
Sound intent: [ambience, effects, approved dialogue or silence]
Edit scope: [what may change and what must remain untouched]
Avoid: [specific likely defects, such as extra objects or changing labels]
```

For the lamp example: **no reference inputs → five-second vertical feature demo → button press → light on → still ending**. A fixed camera isolates the action; “one button” and “stable geometry” constrain product drift. Change the subject and its one visible action to build your own version.

| If the first result fails | Change in the next prompt | Check again |
|---|---|---|
| Too many actions or unfinished ending | Keep one action and reserve the last second for stillness | Does the action finish? |
| Product or character changes | Name the exact shape, color and features to preserve | Compare the beginning and end |
| Unexpected cuts or camera movement | Specify one continuous shot and one camera movement | Is the transition continuous? |
| Unreadable labels or subtitles | Leave blank space and add verified text during editing | Read at delivery size |

For image-guided work, describe **what moves and what stays fixed**. In the free interface observed on 2026-09-21, frame guidance needs both a start and an end image; a mood image or a multi-reference map is not a substitute for that pair. Keep required product parts, identity and composition consistent between endpoints. [Full prompting guide](docs/prompting-guide.md) · [First/last-frame template](templates/README.md#t03-first-and-last-frame-transition).

## Watch creator videos and study the prompts

12 X examples: video previews, original posts, short prompt excerpts and practical notes. The 6 selected examples appear below. Each of the 12 entries now includes a separate, copy-ready five-second Flyne exercise (untested).

[全部案例 / All examples](docs/x-community-showcase.md) · [官方示例 / Official examples](docs/official-h3-examples.md)

### Start with these techniques / 先看这三种方法

Study the framing and scene order, then try the separate five-second exercise. These creator clips were not generated by the exercises. / 先观察构图与场景顺序，再尝试独立的五秒练习；练习不是所示视频的原始提示词。

| Headphone commercial: macro to exploded view / 耳机广告：从材质微距到结构拆解 | Character entrance: detail to full silhouette / 角色登场：从局部揭示到完整轮廓 | Bangkok street-food travel vlog / 曼谷街头美食短片 |
|---|---|---|
| [![Headphone commercial: macro to exploded view — @LudovicCreator](https://pbs.twimg.com/ext_tw_video_thumb/2082783299395538944/pu/img/DXW1Eq1OUCaY8ssH.jpg)](https://x.com/LudovicCreator/status/2082783319075291312/video/1) | [![Character entrance: detail to full silhouette — @aimikoda](https://pbs.twimg.com/amplify_video_thumb/2086412141729402880/img/8hxZX-hc394yGe7P.jpg)](https://x.com/aimikoda/status/2086412223061135392/video/1) | [![Bangkok street-food travel vlog — @nawalsehar](https://pbs.twimg.com/amplify_video_thumb/2085233539185061888/img/ZAkMSVzHz9ihLPyD.jpg)](https://x.com/nawalsehar/status/2085233880353915217/video/1) |
| [@LudovicCreator · Post / 原帖](https://x.com/LudovicCreator/status/2082783319075291312) · [MP4](https://video.twimg.com/ext_tw_video/2082783299395538944/pu/vid/avc1/1280x720/2lMmYGBjYKPRAZ8M.mp4?tag=12) | [@aimikoda · Post / 原帖](https://x.com/aimikoda/status/2086412223061135392) · [MP4](https://video.twimg.com/amplify_video/2086412141729402880/vid/avc1/2160x2294/FS1GToZV1NqxgwuP.mp4?tag=29) | [@nawalsehar · Post / 原帖](https://x.com/nawalsehar/status/2085233880353915217) · [MP4](https://video.twimg.com/amplify_video/2085233539185061888/vid/avc1/2560x1440/jgQLrvA-NHvBJBx_.mp4?tag=29) |
| Learn a macro-to-wide reveal; treat the exploded internals as creative imagery. / 学习从微距到全景的产品展示，不把爆炸结构当作真实构造。 | Study detail-to-character framing; the uploaded layout includes a reference sheet. / 学习从局部到人物全貌的构图；上传画面包含参考图对照。 | Follow introduction, cooking detail and tasting; speech synchronization was not reviewed. / 学习介绍、烹饪特写、试吃的顺序；未核对口型和声音。 |
| [Notes / 查看解读](docs/x-community-showcase.md#xh3-002-headphone-commercial-macro-to-exploded-view) · [FX5-002 / 复制五秒练习](docs/x-community-showcase.md#fx5-002--ceramic-cup-reveal--陶瓷杯材质展示) | [Notes / 查看解读](docs/x-community-showcase.md#xh3-003-character-entrance-detail-to-full-silhouette) · [FX5-003 / 复制五秒练习](docs/x-community-showcase.md#fx5-003--courier-entrance--信使角色登场) | [Notes / 查看解读](docs/x-community-showcase.md#xh3-009-bangkok-street-food-travel-vlog) · [FX5-009 / 复制五秒练习](docs/x-community-showcase.md#fx5-009--market-food-detail--市集食物特写) |

### Learn from mismatches / 从偏差中学习

These examples show why the output needs checking against the prompt. / 这些案例用来说明为什么要对照提示词检查结果。

| Ordinary footage, impossible event: a useful mismatch / 日常影像与不可能事件：值得研究的偏差 | Beat-synced western title sequence / 踩点西部动画片头 | Mirror-side skincare demonstration / 镜前护肤演示 |
|---|---|---|
| [![Ordinary footage, impossible event: a useful mismatch — @cocktailpeanut](https://pbs.twimg.com/amplify_video_thumb/2086878515744669696/img/-jjYBSEiZo_2M_eS.jpg)](https://x.com/cocktailpeanut/status/2086879654116495564/video/1) | [![Beat-synced western title sequence — @doctorwasif](https://pbs.twimg.com/amplify_video_thumb/2085599599801077760/img/koDdEvAQb0L9RUpH.jpg)](https://x.com/doctorwasif/status/2085599659326935100/video/1) | [![Mirror-side skincare demonstration — @ZaraIrahh](https://pbs.twimg.com/amplify_video_thumb/2083010639748882432/img/l0l1V9NgcetYyhCQ.jpg)](https://x.com/ZaraIrahh/status/2083011066800242986/video/1) |
| [@cocktailpeanut · Post / 原帖](https://x.com/cocktailpeanut/status/2086879654116495564) · [MP4](https://video.twimg.com/amplify_video/2086878515744669696/vid/avc1/832x480/SWq-SdbO4yoiFzOO.mp4?tag=29) | [@doctorwasif · Post / 原帖](https://x.com/doctorwasif/status/2085599659326935100) · [MP4](https://video.twimg.com/amplify_video/2085599599801077760/vid/avc1/1920x1080/aQ8Mx5ImZmjNxrZR.mp4?tag=29) | [@ZaraIrahh · Post / 原帖](https://x.com/ZaraIrahh/status/2083011066800242986) · [MP4](https://video.twimg.com/amplify_video/2083010639748882432/vid/avc1/2560x1440/aZjO-LgvvLJfiCUF.mp4?tag=29) |
| Requested a falling rigid sky; the reviewed clip shows an advancing cloud or wave. / 原文要求天空像硬板坠落，采样画面却呈现推进的云浪。 | Good silhouette contrast, but title letters are visibly garbled; not a typography success example. / 剪影对比清楚，但标题字母明显异常，不作为准确文字生成范例。 | Compare the requested 9:16 format with the horizontal upload; no product efficacy was assessed. / 对比原文要求的 9:16 与横屏上传结果；未评价产品功效。 |
| [Notes / 查看解读](docs/x-community-showcase.md#xh3-006-ordinary-footage-impossible-event-a-useful-mismatch) · [FX5-006 / 复制五秒练习](docs/x-community-showcase.md#fx5-006--one-controlled-impossible-event--只安排一个不可能事件) | [Notes / 查看解读](docs/x-community-showcase.md#xh3-007-beat-synced-western-title-sequence) · [FX5-007 / 复制五秒练习](docs/x-community-showcase.md#fx5-007--two-beat-silhouette-study--两拍剪影练习) | [Notes / 查看解读](docs/x-community-showcase.md#xh3-011-mirror-side-skincare-demonstration) · [FX5-011 / 复制五秒练习](docs/x-community-showcase.md#fx5-011--one-product-hand-action--单次产品手部动作) |


XH3-008 publishes a partial prompt. Videos belong to their creators and were not regenerated by Flyne AI; external media are outside this repository’s MIT license.

### Turn a technique into a small exercise

Learn the headphone example’s macro-to-wide reveal before attempting exploded internals or complex cuts. This is the independently written **FX5-002 ceramic cup exercise**, not the creator’s prompt or the prompt behind the video above. Select text-only, 1:1 and five seconds; leave image inputs empty.

```text
A five-second studio shot of one unbranded ivory ceramic cup on a mint pedestal. Begin close to its speckled glaze, then slowly pull back to reveal the whole cup by second four. Hold for one second. The cup stays still with its handle on the right. Soft side light, stable reflections, quiet room tone. No cuts, steam, text or extra cups.
```

Check that the handle, rim and glaze stay consistent; the whole cup should appear by second four and hold for the last second. An attempt reached the queue, but no output was available for review; [observation record](docs/quick-start.md).

## Official examples / 官方示例

Official MiniMax previews, linked to their original skills; not FlyneAI outputs. / MiniMax 官方预览，链接到原始教程，不是 FlyneAI 生成结果。

| Product / 产品 | Animation / 动画 | Music / 音乐 |
|---|---|---|
| [![Official minimalist-product-ad-generator](https://raw.githubusercontent.com/MiniMax-AI/MiniMax-H3/main/assets/minimalist-product-ad-generator.gif)](https://github.com/MiniMax-AI/MiniMax-H3/tree/main/skills/minimalist-product-ad-generator) | [![Official 3d-animation-short-generator](https://raw.githubusercontent.com/MiniMax-AI/MiniMax-H3/main/assets/3d-animation-short-generator.gif)](https://github.com/MiniMax-AI/MiniMax-H3/tree/main/skills/3d-animation-short-generator) | [![Official music-video-subtitle-generator](https://raw.githubusercontent.com/MiniMax-AI/MiniMax-H3/main/assets/music-video-subtitle-generator.gif)](https://github.com/MiniMax-AI/MiniMax-H3/tree/main/skills/mv-subtitle-skill-confirmed) |

[Official source gallery / 完整官方案例](docs/official-h3-examples.md)

## Reference images for your next shot

Three Flyne AI illustrations plus eleven attributed reference stills, linked to recipes and image briefs. These are not H3 outputs.

| [FY-001 台灯 / Lamp](prompts/flyne/fy-001.md) | [FY-002 包款 / Bag](prompts/flyne/fy-002.md) | [FY-009 字幕背景 / Backdrop](prompts/flyne/fy-009.md) |
|---|---|---|
| [![FY-001](assets/previews/fy-001-lamp.webp)](assets/flyne/fy-001-lamp.png) | [![FY-002](assets/previews/fy-002-bag.webp)](assets/flyne/fy-002-bag.png) | [![FY-009](assets/previews/fy-009-backdrop.webp)](assets/flyne/fy-009-backdrop.png) |

AI-generated reference stills; not H3 outputs. / AI 生成参考图，不是 H3 视频结果。[使用说明 / Usage notes](assets/flyne-reference-briefs.md)

| BRD-001 · Brand/product first frame | UGC-001 · UGC creator/product first frame | TRV-001 · Travel/location first frame |
|---|---|---|
| [![Brand/product first frame](assets/previews/midnight-observatory-tea.webp)](assets/gallery/midnight-observatory-tea.webp) | [![UGC creator/product first frame](assets/previews/honest-desk-lamp-demo.webp)](assets/gallery/honest-desk-lamp-demo.webp) | [![Travel/location first frame](assets/previews/rain-washed-canal-morning.webp)](assets/gallery/rain-washed-canal-morning.webp) |
| [Prompt / 提示词](prompts/upstream/01-brand-advertising.md#brd-001-midnight-observatory-tea-launch) · [Image brief / 图片简报](assets/minimax-h3-reference-image-prompts.md#img-002-brand-and-product-midnight-observatory-tea) | [Prompt / 提示词](prompts/upstream/03-ugc-lifestyle.md#ugc-001-desk-lamp-honest-first-impression) · [Image brief / 图片简报](assets/minimax-h3-reference-image-prompts.md#img-003-ugc-and-lifestyle-honest-desk-lamp-demo) | [Prompt / 提示词](prompts/upstream/04-travel-hospitality.md#trv-001-rain-washed-canal-town-morning) · [Image brief / 图片简报](assets/minimax-h3-reference-image-prompts.md#img-004-travel-rain-washed-canal-morning) |

| ANI-002 · Animation character/environment reference | ACT-001 · Sports athlete/route reference | MRF-002 · Fictional product identity/material reference |
|---|---|---|
| [![Animation character/environment reference](assets/previews/clay-repair-robot.webp)](assets/gallery/clay-repair-robot.webp) | [![Sports athlete/route reference](assets/previews/indoor-climbing-final-hold.webp)](assets/gallery/indoor-climbing-final-hold.webp) | [![Fictional product identity/material reference](assets/previews/radial-cork-speaker.webp)](assets/gallery/radial-cork-speaker.webp) |
| [Prompt / 提示词](prompts/upstream/08-animation-stylized.md#ani-002-clay-repair-robot-finds-a-button) · [Image brief / 图片简报](assets/minimax-h3-reference-image-prompts.md#img-005-animation-clay-repair-robot-workshop) | [Prompt / 提示词](prompts/upstream/09-action-sports.md#act-001-indoor-climbing-final-move) · [Image brief / 图片简报](assets/minimax-h3-reference-image-prompts.md#img-006-sports-indoor-climbing-final-hold) | [Prompt / 提示词](prompts/upstream/20-multireference-camera-transfer.md#mrf-002-radial-cork-speaker-transfer-motion-grammar-not-content) · [Image brief / 图片简报](assets/minimax-h3-reference-image-prompts.md#img-007-product-radial-cork-speaker) |

| CHR-001 · Paper-craft character/environment reference | MRF-001 · Multi-reference one-take first frame | MOG-001 · Dynamic-poster final frame |
|---|---|---|
| [![Paper-craft character/environment reference](assets/previews/paper-birds-storm-shelter.webp)](assets/gallery/paper-birds-storm-shelter.webp) | [![Multi-reference one-take first frame](assets/previews/three-biome-museum-rail.webp)](assets/gallery/three-biome-museum-rail.webp) | [![Dynamic-poster final frame](assets/previews/dynamic-night-market-poster.webp)](assets/gallery/dynamic-night-market-poster.webp) |
| [Prompt / 提示词](prompts/upstream/21-character-dialogue-performance.md#chr-001-paper-birds-plan-for-the-storm) · [Image brief / 图片简报](assets/minimax-h3-reference-image-prompts.md#img-008-character-paper-birds-in-a-storm-shelter) | [Prompt / 提示词](prompts/upstream/20-multireference-camera-transfer.md#mrf-001-three-biome-museum-rail-in-one-take) · [Image brief / 图片简报](assets/minimax-h3-reference-image-prompts.md#img-009-multi-reference-three-biome-museum-rail) | [Prompt / 提示词](prompts/upstream/22-motion-graphics-dynamic-posters.md#mog-001-night-market-poster-builds-on-the-beat) · [Image brief / 图片简报](assets/minimax-h3-reference-image-prompts.md#img-010-motion-graphics-dynamic-night-market-poster) |

| SRL-001 · Practical-surreal first frame | VER-001 · Live-creator product reference |
|---|---|
| [![Practical-surreal first frame](assets/previews/topographic-map-archive.webp)](assets/gallery/topographic-map-archive.webp) | [![Live-creator product reference](assets/previews/modular-lunch-jar-kit.webp)](assets/gallery/modular-lunch-jar-kit.webp) |
| [Prompt / 提示词](prompts/upstream/23-surreal-physics-optical-illusions.md#srl-001-the-map-rises-into-a-landscape) · [Image brief / 图片简报](assets/minimax-h3-reference-image-prompts.md#img-011-surreal-physics-topographic-map-archive) | [Prompt / 提示词](prompts/upstream/24-vertical-series-live-creator.md#ver-001-honest-modular-lunch-jar-live-demo) · [Image brief / 图片简报](assets/minimax-h3-reference-image-prompts.md#img-012-live-creator-modular-lunch-jar-kit) |


[全部参考图及使用说明 / All reference images and usage notes](docs/reference-gallery.md)

## Choose a production problem

| Goal | Start here | Main acceptance check |
|---|---|---|
| Advertising and social hooks | [Brand library](prompts/upstream/01-brand-advertising.md), [silent hook](prompts/flyne/fy-001.md) | Clear action, no unsupported claims |
| Product and SKU variants | [Commerce library](prompts/upstream/02-product-ecommerce.md), [colorway comparison](prompts/flyne/fy-002.md) | Product geometry and materials |
| Customer support and training | [Latch demo](prompts/flyne/fy-003.md), [warehouse exceptions](prompts/flyne/fy-010.md) | Expert-verified procedure |
| Software and onboarding | [UI library](prompts/upstream/11-ui-game-digital.md), [empty state](prompts/flyne/fy-005.md) | Correct interface state |
| Localization and character | [Dialogue library](prompts/upstream/21-character-dialogue-performance.md), [bilingual greeting](prompts/flyne/fy-006.md) | Meaning, identity and timing |
| Interactive previsualization | [Museum branch](prompts/flyne/fy-007.md), [weather alternative](prompts/flyne/fy-015.md) | Consistent opening/closing state |
| Design and editorial motion | [Packaging](prompts/flyne/fy-008.md), [caption-safe backdrop](prompts/flyne/fy-009.md) | Feasibility and readability |
| Controlled edits and diagnostics | [Seasonal display](prompts/flyne/fy-012.md), [reference stress test](prompts/flyne/fy-016.md) | Changes stay within scope |

The imported collection also covers travel, food, fashion, cinema, animation, sports, VFX, music, education, architecture, mobility, pets, industry and vertical series. [Complete catalog](prompts/README.md) · [Use conditions](docs/recipe-usage.md).

## All 24 recipe categories

These categories preserve the 84 attributed source recipes; the task table above adds Flyne scenarios. Start with your subject rather than memorizing recipe IDs.

| Category | Recipes | Typical uses |
|---|---:|---|
| [Brand and Advertising](prompts/upstream/01-brand-advertising.md) | 3 | Product launches, local campaigns and aspect-ratio variants |
| [Product and E-commerce](prompts/upstream/02-product-ecommerce.md) | 3 | Product details, material studies and rotating packshots |
| [UGC and Lifestyle](prompts/upstream/03-ugc-lifestyle.md) | 3 | First impressions, everyday use and packing tests |
| [Travel and Hospitality](prompts/upstream/04-travel-hospitality.md) | 3 | Destinations, accommodation and market walks |
| [Food and Beverage](prompts/upstream/05-food-beverage.md) | 3 | Preparation, serving and food textures |
| [Fashion and Beauty](prompts/upstream/06-fashion-beauty.md) | 3 | Outfits, beauty details and styling transitions |
| [Cinematic Storytelling](prompts/upstream/07-cinematic-storytelling.md) | 3 | Character emotion, suspense and story beats |
| [Animation and Stylized](prompts/upstream/08-animation-stylized.md) | 3 | Paper craft, clay characters and ink scenes |
| [Action and Sports](prompts/upstream/09-action-sports.md) | 3 | Climbing, cycling and ball sports |
| [Fantasy, Sci-fi and VFX](prompts/upstream/10-fantasy-scifi-vfx.md) | 3 | Transformations, imagined environments and visual effects |
| [UI, Game and Digital Experience](prompts/upstream/11-ui-game-digital.md) | 3 | Software onboarding, device interfaces and game actions |
| [Transitions, Comedy and Social](prompts/upstream/12-transitions-comedy-social.md) | 3 | Match cuts, visual jokes and loops |
| [Music, Performance and Audio-Driven](prompts/upstream/13-music-performance-audio.md) | 4 | Singing, dance and rhythm visualization |
| [Education, Documentary and Science](prompts/upstream/14-education-documentary-science.md) | 4 | Science explanations, museum stories and instruction |
| [Architecture, Interiors and Real-Estate](prompts/upstream/15-architecture-interiors-real-estate.md) | 4 | Property tours, daylight and renovation previews |
| [Automotive and Mobility](prompts/upstream/16-automotive-mobility.md) | 4 | Vehicle interiors, cycling and rail journeys |
| [Nature, Animals and Pet](prompts/upstream/17-nature-animals-pets.md) | 4 | Wildlife, pet accessories and plant observation |
| [Industry, Business and Public-Service](prompts/upstream/18-industry-business-public-service.md) | 4 | Production, logistics, evacuation and service guidance |
| [Editing, Continuation and Localization](prompts/upstream/19-editing-continuation-localization.md) | 4 | Cleanup, continuation, localization and relighting |
| [Multi-Reference and Camera-Transfer](prompts/upstream/20-multireference-camera-transfer.md) | 4 | One-takes, camera-motion transfer and matched actions |
| [Character, Dialogue and Performance](prompts/upstream/21-character-dialogue-performance.md) | 4 | Character acting, bilingual dialogue and ensemble scenes |
| [Motion Graphics and Dynamic Poster](prompts/upstream/22-motion-graphics-dynamic-posters.md) | 4 | Poster assembly, feature cards and exhibition openings |
| [Surreal Physics and Optical-Illusion](prompts/upstream/23-surreal-physics-optical-illusions.md) | 4 | Material changes, time offsets and spatial illusions |
| [Vertical Series and Live-Creator](prompts/upstream/24-vertical-series-live-creator.md) | 4 | Product demonstrations, short drama, repair series and answers |

## H3 is not the same release as H3 Max

As checked on **2026-09-17**, H3-Base has downloadable FL2VA and Ref2VA weights. H3 Max is fal's hosted post-trained derivative; no public Max weights were found in the checked primary sources. The official full 2K workflow also includes hosted components. [Model guide and citations](docs/model-guide.md).

This repository's MIT license does not license model weights or grant service access. Read the current H3 Community License and the terms of your chosen route. Never assume a community quantization is Max or that a future release has already happened.

## Official resources and downloads

- [Official MiniMax H3 repository](https://github.com/MiniMax-AI/MiniMax-H3): release notes, runtime code and request examples.
- [Model card and weights](https://huggingface.co/MiniMaxAI/MiniMax-H3): license, revisions and runtime requirements.
- [Official capability and prompting examples](https://platform.minimaxi.com/docs/guides/video-prompt): creative workflows and examples.
- [Official video generation documentation](https://platform.minimaxi.com/docs/guides/video-generation): current modes and request fields.
- [Local deployment guide](docs/deployment-guide.md) · [API integration](docs/api-workflow.md) · [Official request/output comparisons](docs/official-h3-examples.md).

## Workflows and longer-term value

- [Browser, local and hosted workflows](docs/workflows.md): route selection, reference roles and multi-shot handoff.
- [Evaluation and cost](docs/evaluation.md): accepted-output rate, cost per usable clip and review criteria.
- [Ecosystem opportunities](docs/opportunities.md): reference libraries, localization, adaptation and optimization experiments.
- [Source register](docs/sources.md): primary links, review date and unresolved questions.
- [Roadmap](ROADMAP.md): what the community can verify and improve next.

Open weights can support adaptation and independent measurement. The practical asset is a repeatable workflow with evidence, not a larger untested prompt count. Opportunities in this guide are hypotheses to test, not promised commercial results.

## Offline search and maintenance

Requires Python 3.9+; no third-party packages or API keys.

```sh
python3 scripts/catalog.py search "product"
python3 scripts/catalog.py search "FX5-002" --origin exercise --show-prompt
python3 scripts/catalog.py search "客服" --origin flyne --show-prompt
python3 scripts/build.py
python3 scripts/validate.py
```

Search covers 100 recipes plus 12 separate five-second exercises. Use `--origin exercise` to filter exercises and `--show-prompt` to print both languages. Exercises remain untested and are distinct from the creator prompts.

[data/catalog.json](data/catalog.json) is machine-readable. Validation checks counts, unique IDs, local links, language pages and prompt provenance; it does not run a video model. Eight README languages are provided; detailed guides are mainly English, with Chinese or multilingual sections in selected guides, and canonical prompts are English.

## Flyne AI, attribution and contributions

[Flyne AI](https://flyne.ai/) is the project brand and browser workflow entry. Access, credits and supported modes follow the current product page; this repository does not promise permanent free generation or a Flyne H3 Max endpoint.

The 84 imported recipes remain credited to **Flaq AI**, pinned to a source commit, with unchanged prompt blocks and the complete original MIT license. New Flyne material is separately identified. [Attribution and import history](THIRD_PARTY_NOTICES.md).

Contribute a reproducible test, a new production scenario, a translation correction or an official-source update. See [CONTRIBUTING.md](CONTRIBUTING.md), [prompt template](templates/prompt.md) and [conduct](CODE_OF_CONDUCT.md).

[MIT](LICENSE) for Flyne additions · [upstream MIT](licenses/Flaq-AI-MIT.txt) for imported content. Independent of MiniMax; product names belong to their owners.

## Become a Flyne AI affiliate partner

We welcome creators, educators, reviewers and creative teams to become our partners! Share Flyne AI through your referral link and earn commission on eligible paid orders:

- **20%** on a referred user's first valid paid order.
- **10%** on subsequent valid paid orders placed within **60 days of that user's registration**.

[Join the Flyne AI Affiliate Program](https://flyne.ai/affiliate-program/). Commission eligibility, attribution and payouts follow the current program agreement and review process.

Questions or partnership enquiries? Contact us at [contact@flyne.ai](mailto:contact@flyne.ai).
