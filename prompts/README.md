# Prompt catalog / 提示词目录

**100 recipes**: 84 attributed MIT imports + 16 Flyne AI additions. All are untested by this project.

84 条引入内容保留原作者署名；16 条新增内容为概念方案，尚未实测。时长和画幅是创作目标，实际取决于所选平台。

[Model selection](../docs/model-guide.md) · [Workflows](../docs/workflows.md) · [Evaluation](../docs/evaluation.md) · [Attribution](../THIRD_PARTY_NOTICES.md)

Search offline: `python3 scripts/catalog.py search "product"` from the repository root.

Search includes the 100 recipes plus 12 separate, untested five-second exercises: `python3 scripts/catalog.py search "FX5-002" --origin exercise --show-prompt`. Exercises are stored in [community-sources.json](../data/community-sources.json); they did not produce the linked creator videos.

搜索覆盖 100 条配方和另列的 12 条五秒练习；练习尚未实测，不是社区视频的原始提示词。

## Browse by category / 按分类浏览

| Category / 分类 | Recipes / 数量 |
|---|---:|
| [Flyne original scenarios / Flyne 原创场景](#flyne-ai-additions--新增场景) | 16 |
| [Brand and Advertising Video Prompts](../prompts/upstream/01-brand-advertising.md) | 3 |
| [Product and E-commerce Video Prompts](../prompts/upstream/02-product-ecommerce.md) | 3 |
| [UGC and Lifestyle Video Prompts](../prompts/upstream/03-ugc-lifestyle.md) | 3 |
| [Travel and Hospitality Video Prompts](../prompts/upstream/04-travel-hospitality.md) | 3 |
| [Food and Beverage Video Prompts](../prompts/upstream/05-food-beverage.md) | 3 |
| [Fashion and Beauty Video Prompts](../prompts/upstream/06-fashion-beauty.md) | 3 |
| [Cinematic Storytelling Video Prompts](../prompts/upstream/07-cinematic-storytelling.md) | 3 |
| [Animation and Stylized Video Prompts](../prompts/upstream/08-animation-stylized.md) | 3 |
| [Action and Sports Video Prompts](../prompts/upstream/09-action-sports.md) | 3 |
| [Fantasy, Sci-fi and VFX Video Prompts](../prompts/upstream/10-fantasy-scifi-vfx.md) | 3 |
| [UI, Game and Digital Experience Video Prompts](../prompts/upstream/11-ui-game-digital.md) | 3 |
| [Transitions, Comedy and Social Video Prompts](../prompts/upstream/12-transitions-comedy-social.md) | 3 |
| [Music, Performance and Audio-Driven Video Prompts](../prompts/upstream/13-music-performance-audio.md) | 4 |
| [Education, Documentary and Science Video Prompts](../prompts/upstream/14-education-documentary-science.md) | 4 |
| [Architecture, Interiors and Real-Estate Video Prompts](../prompts/upstream/15-architecture-interiors-real-estate.md) | 4 |
| [Automotive and Mobility Video Prompts](../prompts/upstream/16-automotive-mobility.md) | 4 |
| [Nature, Animals and Pet Video Prompts](../prompts/upstream/17-nature-animals-pets.md) | 4 |
| [Industry, Business and Public-Service Video Prompts](../prompts/upstream/18-industry-business-public-service.md) | 4 |
| [Editing, Continuation and Localization Video Prompts](../prompts/upstream/19-editing-continuation-localization.md) | 4 |
| [Multi-Reference and Camera-Transfer Video Prompts](../prompts/upstream/20-multireference-camera-transfer.md) | 4 |
| [Character, Dialogue and Performance Video Prompts](../prompts/upstream/21-character-dialogue-performance.md) | 4 |
| [Motion Graphics and Dynamic Poster Video Prompts](../prompts/upstream/22-motion-graphics-dynamic-posters.md) | 4 |
| [Surreal Physics and Optical-Illusion Video Prompts](../prompts/upstream/23-surreal-physics-optical-illusions.md) | 4 |
| [Vertical Series and Live-Creator Video Prompts](../prompts/upstream/24-vertical-series-live-creator.md) | 4 |

[Use conditions / 选择使用入口](../docs/recipe-usage.md): matching a form does not establish generation quality.

## Flyne AI additions / 新增场景

| ID | Recipe | Task | Category | Use conditions / 使用条件 |
|---|---|---|---|---|
| FY-001 | [Silent feature reveal · 静音信息流功能展示](../prompts/flyne/fy-001.md) | t2va | social | Free text / 免费文字 |
| FY-002 | [SKU colorway comparison · 同款商品配色对比](../prompts/flyne/fy-002.md) | ref2va | commerce | Confirm support / 确认平台支持 |
| FY-003 | [Customer support latch close-up · 客服卡扣操作演示](../prompts/flyne/fy-003.md) | ref2va | support | Confirm support / 确认平台支持 |
| FY-004 | [Menu availability loop · 餐饮菜单氛围循环](../prompts/flyne/fy-004.md) | fl2va | hospitality | Both frames / 准备首尾图 |
| FY-005 | [SaaS empty-state onboarding · 软件空状态引导](../prompts/flyne/fy-005.md) | ref2va | software | Confirm support / 确认平台支持 |
| FY-006 | [Two-language service greeting · 双语服务欢迎短片](../prompts/flyne/fy-006.md) | ref2va | localization | Confirm support / 确认平台支持 |
| FY-007 | [Branching museum guide · 博物馆分支导览](../prompts/flyne/fy-007.md) | ref2va | interactive | Confirm support / 确认平台支持 |
| FY-008 | [Packaging assembly previsualization · 包装组装预演](../prompts/flyne/fy-008.md) | ref2va | design | Confirm support / 确认平台支持 |
| FY-009 | [Accessible caption-safe event backdrop · 字幕友好的活动背景](../prompts/flyne/fy-009.md) | t2va | accessibility | Shorten first / 先缩短时长 |
| FY-010 | [Warehouse exception training · 仓储异常识别培训](../prompts/flyne/fy-010.md) | ref2va | training | Confirm support / 确认平台支持 |
| FY-011 | [Pet accessory scale check · 宠物配件尺寸展示](../prompts/flyne/fy-011.md) | ref2va | pets | Confirm support / 确认平台支持 |
| FY-012 | [Seasonal storefront update · 店铺季节视觉更新](../prompts/flyne/fy-012.md) | ref2va | retail | Confirm support / 确认平台支持 |
| FY-013 | [Crowdfunding prototype disclosure · 众筹原型概念说明](../prompts/flyne/fy-013.md) | fl2va | prototype | Confirm support / 确认平台支持 |
| FY-014 | [Local craft macro process · 地方工艺微距记录概念](../prompts/flyne/fy-014.md) | ref2va | craft | Confirm support / 确认平台支持 |
| FY-015 | [Weather-contingency storyboard · 天气备选分镜](../prompts/flyne/fy-015.md) | ref2va | previsualization | Confirm support / 确认平台支持 |
| FY-016 | [Reference-role stress test · 多参考角色隔离测试](../prompts/flyne/fy-016.md) | ref2va | evaluation | Confirm support / 确认平台支持 |

## Attributed upstream library / 引入内容

Copyright © 2026 Flaq AI. [MIT license](../licenses/Flaq-AI-MIT.txt). Source revisions are linked in each file.

| ID | Recipe | Category | Use conditions / 使用条件 |
|---|---|---|---|
| BRD-001 | [Midnight Observatory Tea Launch](../prompts/upstream/01-brand-advertising.md#brd-001-midnight-observatory-tea-launch) | Brand and Advertising Video Prompts | Confirm support / 确认平台支持 |
| BRD-002 | [Community Cinema Opening Night](../prompts/upstream/01-brand-advertising.md#brd-002-community-cinema-opening-night) | Brand and Advertising Video Prompts | Confirm support / 确认平台支持 |
| BRD-003 | [One Campaign, Three Aspect Ratios](../prompts/upstream/01-brand-advertising.md#brd-003-one-campaign-three-aspect-ratios) | Brand and Advertising Video Prompts | Confirm support / 确认平台支持 |
| PRD-001 | [Modular Hiking Lantern Feature Demo](../prompts/upstream/02-product-ecommerce.md#prd-001-modular-hiking-lantern-feature-demo) | Product and E-commerce Video Prompts | Confirm support / 确认平台支持 |
| PRD-002 | [Ceramic Diffuser Material Film](../prompts/upstream/02-product-ecommerce.md#prd-002-ceramic-diffuser-material-film) | Product and E-commerce Video Prompts | Confirm support / 确认平台支持 |
| PRD-003 | [Marketplace Rotation Without Geometry Drift](../prompts/upstream/02-product-ecommerce.md#prd-003-marketplace-rotation-without-geometry-drift) | Product and E-commerce Video Prompts | Confirm support / 确认平台支持 |
| UGC-001 | [Desk Lamp Honest First Impression](../prompts/upstream/03-ugc-lifestyle.md#ugc-001-desk-lamp-honest-first-impression) | UGC and Lifestyle Video Prompts | Confirm support / 确认平台支持 |
| UGC-002 | [Balcony Herb Kit Weekend Routine](../prompts/upstream/03-ugc-lifestyle.md#ugc-002-balcony-herb-kit-weekend-routine) | UGC and Lifestyle Video Prompts | Confirm support / 确认平台支持 |
| UGC-003 | [Commuter Sling Real-World Packing Test](../prompts/upstream/03-ugc-lifestyle.md#ugc-003-commuter-sling-real-world-packing-test) | UGC and Lifestyle Video Prompts | Confirm support / 确认平台支持 |
| TRV-001 | [Rain-Washed Canal Town Morning](../prompts/upstream/04-travel-hospitality.md#trv-001-rain-washed-canal-town-morning) | Travel and Hospitality Video Prompts | Confirm support / 确认平台支持 |
| TRV-002 | [Volcanic Island Guesthouse Reveal](../prompts/upstream/04-travel-hospitality.md#trv-002-volcanic-island-guesthouse-reveal) | Travel and Hospitality Video Prompts | Confirm support / 确认平台支持 |
| TRV-003 | [First-Person Night Market Wayfinding](../prompts/upstream/04-travel-hospitality.md#trv-003-first-person-night-market-wayfinding) | Travel and Hospitality Video Prompts | Confirm support / 确认平台支持 |
| FNB-001 | [Dawn Bakery Lamination Sequence](../prompts/upstream/05-food-beverage.md#fnb-001-dawn-bakery-lamination-sequence) | Food and Beverage Video Prompts | Confirm support / 确认平台支持 |
| FNB-002 | [Clear Broth Noodle Service](../prompts/upstream/05-food-beverage.md#fnb-002-clear-broth-noodle-service) | Food and Beverage Video Prompts | Confirm support / 确认平台支持 |
| FNB-003 | [Sparkling Botanical Tea Macro Ad](../prompts/upstream/05-food-beverage.md#fnb-003-sparkling-botanical-tea-macro-ad) | Food and Beverage Video Prompts | Confirm support / 确认平台支持 |
| FSH-001 | [Wind-Study Eyewear Editorial](../prompts/upstream/06-fashion-beauty.md#fsh-001-wind-study-eyewear-editorial) | Fashion and Beauty Video Prompts | Confirm support / 确认平台支持 |
| FSH-002 | [Mineral Lip Color Texture Study](../prompts/upstream/06-fashion-beauty.md#fsh-002-mineral-lip-color-texture-study) | Fashion and Beauty Video Prompts | Confirm support / 确认平台支持 |
| FSH-003 | [Four-Look Textile Transition](../prompts/upstream/06-fashion-beauty.md#fsh-003-four-look-textile-transition) | Fashion and Beauty Video Prompts | Confirm support / 确认平台支持 |
| CIN-001 | [The Unsent Library Letter](../prompts/upstream/07-cinematic-storytelling.md#cin-001-the-unsent-library-letter) | Cinematic Storytelling Video Prompts | Confirm support / 确认平台支持 |
| CIN-002 | [Last Train Platform Farewell](../prompts/upstream/07-cinematic-storytelling.md#cin-002-last-train-platform-farewell) | Cinematic Storytelling Video Prompts | Confirm support / 确认平台支持 |
| CIN-003 | [Rooftop Weather Signal Mystery](../prompts/upstream/07-cinematic-storytelling.md#cin-003-rooftop-weather-signal-mystery) | Cinematic Storytelling Video Prompts | Confirm support / 确认平台支持 |
| ANI-001 | [Paper-Cut Wetland Food Web](../prompts/upstream/08-animation-stylized.md#ani-001-paper-cut-wetland-food-web) | Animation and Stylized Video Prompts | Confirm support / 确认平台支持 |
| ANI-002 | [Clay Repair Robot Finds a Button](../prompts/upstream/08-animation-stylized.md#ani-002-clay-repair-robot-finds-a-button) | Animation and Stylized Video Prompts | Confirm support / 确认平台支持 |
| ANI-003 | [Ink Fish Becomes a City Tram](../prompts/upstream/08-animation-stylized.md#ani-003-ink-fish-becomes-a-city-tram) | Animation and Stylized Video Prompts | Confirm support / 确认平台支持 |
| ACT-001 | [Indoor Climbing Final Move](../prompts/upstream/09-action-sports.md#act-001-indoor-climbing-final-move) | Action and Sports Video Prompts | Confirm support / 确认平台支持 |
| ACT-002 | [Rain Circuit Bicycle Corner](../prompts/upstream/09-action-sports.md#act-002-rain-circuit-bicycle-corner) | Action and Sports Video Prompts | Confirm support / 确认平台支持 |
| ACT-003 | [Table Tennis Rally in One Take](../prompts/upstream/09-action-sports.md#act-003-table-tennis-rally-in-one-take) | Action and Sports Video Prompts | Confirm support / 确认平台支持 |
| VFX-001 | [Glasshouse Grows a Night Sky](../prompts/upstream/10-fantasy-scifi-vfx.md#vfx-001-glasshouse-grows-a-night-sky) | Fantasy, Sci-fi and VFX Video Prompts | Confirm support / 确认平台支持 |
| VFX-002 | [Miniature Rain Collector City](../prompts/upstream/10-fantasy-scifi-vfx.md#vfx-002-miniature-rain-collector-city) | Fantasy, Sci-fi and VFX Video Prompts | Confirm support / 确认平台支持 |
| VFX-003 | [Constellation Dress Performance](../prompts/upstream/10-fantasy-scifi-vfx.md#vfx-003-constellation-dress-performance) | Fantasy, Sci-fi and VFX Video Prompts | Confirm support / 确认平台支持 |
| DIG-001 | [Focus Timer Product Walkthrough](../prompts/upstream/11-ui-game-digital.md#dig-001-focus-timer-product-walkthrough) | UI, Game and Digital Experience Video Prompts | Confirm support / 确认平台支持 |
| DIG-002 | [Electric Bicycle Dashboard Modes](../prompts/upstream/11-ui-game-digital.md#dig-002-electric-bicycle-dashboard-modes) | UI, Game and Digital Experience Video Prompts | Confirm support / 确认平台支持 |
| DIG-003 | [Tactical Garden Game Inventory](../prompts/upstream/11-ui-game-digital.md#dig-003-tactical-garden-game-inventory) | UI, Game and Digital Experience Video Prompts | Confirm support / 确认平台支持 |
| SOC-001 | [Three Rooms, One Rolling Orange](../prompts/upstream/12-transitions-comedy-social.md#soc-001-three-rooms-one-rolling-orange) | Transitions, Comedy and Social Video Prompts | Confirm support / 确认平台支持 |
| SOC-002 | [Office Plant Quietly Takes Over](../prompts/upstream/12-transitions-comedy-social.md#soc-002-office-plant-quietly-takes-over) | Transitions, Comedy and Social Video Prompts | Confirm support / 确认平台支持 |
| SOC-003 | [Alien at the Self-Service Laundry](../prompts/upstream/12-transitions-comedy-social.md#soc-003-alien-at-the-self-service-laundry) | Transitions, Comedy and Social Video Prompts | Confirm support / 确认平台支持 |
| MUS-001 | [Rooftop Trio Live Session](../prompts/upstream/13-music-performance-audio.md#mus-001-rooftop-trio-live-session) | Music, Performance and Audio-Driven Video Prompts | Confirm support / 确认平台支持 |
| MUS-002 | [Multilingual Station Duet](../prompts/upstream/13-music-performance-audio.md#mus-002-multilingual-station-duet) | Music, Performance and Audio-Driven Video Prompts | Confirm support / 确认平台支持 |
| MUS-003 | [Dance Rehearsal to Stage Match Cut](../prompts/upstream/13-music-performance-audio.md#mus-003-dance-rehearsal-to-stage-match-cut) | Music, Performance and Audio-Driven Video Prompts | Confirm support / 确认平台支持 |
| MUS-004 | [Sound-to-Shape Album Loop](../prompts/upstream/13-music-performance-audio.md#mus-004-sound-to-shape-album-loop) | Music, Performance and Audio-Driven Video Prompts | Confirm support / 确认平台支持 |
| EDU-001 | [Tidal Marsh Carbon Explainer](../prompts/upstream/14-education-documentary-science.md#edu-001-tidal-marsh-carbon-explainer) | Education, Documentary and Science Video Prompts | Confirm support / 确认平台支持 |
| EDU-002 | [Museum Object Story Without Reconstruction Claims](../prompts/upstream/14-education-documentary-science.md#edu-002-museum-object-story-without-reconstruction-claims) | Education, Documentary and Science Video Prompts | Confirm support / 确认平台支持 |
| EDU-003 | [Safe Workshop Procedure: Drill-Press Setup](../prompts/upstream/14-education-documentary-science.md#edu-003-safe-workshop-procedure-drill-press-setup) | Education, Documentary and Science Video Prompts | Confirm support / 确认平台支持 |
| EDU-004 | [Microscopic World to Everyday Scale](../prompts/upstream/14-education-documentary-science.md#edu-004-microscopic-world-to-everyday-scale) | Education, Documentary and Science Video Prompts | Confirm support / 确认平台支持 |
| ARC-001 | [Honest Small-Apartment Walkthrough](../prompts/upstream/15-architecture-interiors-real-estate.md#arc-001-honest-small-apartment-walkthrough) | Architecture, Interiors and Real-Estate Video Prompts | Confirm support / 确认平台支持 |
| ARC-002 | [Courtyard Cafe Morning-to-Evening Study](../prompts/upstream/15-architecture-interiors-real-estate.md#arc-002-courtyard-cafe-morning-to-evening-study) | Architecture, Interiors and Real-Estate Video Prompts | Confirm support / 确认平台支持 |
| ARC-003 | [Renovation Concept With Before/After Boundary](../prompts/upstream/15-architecture-interiors-real-estate.md#arc-003-renovation-concept-with-beforeafter-boundary) | Architecture, Interiors and Real-Estate Video Prompts | Confirm support / 确认平台支持 |
| ARC-004 | [Smart-Home Evening Sequence](../prompts/upstream/15-architecture-interiors-real-estate.md#arc-004-smart-home-evening-sequence) | Architecture, Interiors and Real-Estate Video Prompts | Confirm support / 确认平台支持 |
| MOB-001 | [Electric City Car Interior Demo](../prompts/upstream/16-automotive-mobility.md#mob-001-electric-city-car-interior-demo) | Automotive and Mobility Video Prompts | Confirm support / 确认平台支持 |
| MOB-002 | [Cargo Bicycle Rain-Test Film](../prompts/upstream/16-automotive-mobility.md#mob-002-cargo-bicycle-rain-test-film) | Automotive and Mobility Video Prompts | Confirm support / 确认平台支持 |
| MOB-003 | [Night Train Sleeper Service](../prompts/upstream/16-automotive-mobility.md#mob-003-night-train-sleeper-service) | Automotive and Mobility Video Prompts | Confirm support / 确认平台支持 |
| MOB-004 | [Sidewalk Delivery Robot Handoff](../prompts/upstream/16-automotive-mobility.md#mob-004-sidewalk-delivery-robot-handoff) | Automotive and Mobility Video Prompts | Confirm support / 确认平台支持 |
| NAT-001 | [Urban Fox Dawn Observation](../prompts/upstream/17-nature-animals-pets.md#nat-001-urban-fox-dawn-observation) | Nature, Animals and Pet Video Prompts | Confirm support / 确认平台支持 |
| NAT-002 | [Senior Dog Raincoat Fit Check](../prompts/upstream/17-nature-animals-pets.md#nat-002-senior-dog-raincoat-fit-check) | Nature, Animals and Pet Video Prompts | Confirm support / 确认平台支持 |
| NAT-003 | [Balcony Tomato Growth Diary](../prompts/upstream/17-nature-animals-pets.md#nat-003-balcony-tomato-growth-diary) | Nature, Animals and Pet Video Prompts | Confirm support / 确认平台支持 |
| NAT-004 | [Tide-Pool Macro Field Note](../prompts/upstream/17-nature-animals-pets.md#nat-004-tide-pool-macro-field-note) | Nature, Animals and Pet Video Prompts | Confirm support / 确认平台支持 |
| IND-001 | [Small-Batch Assembly Process](../prompts/upstream/18-industry-business-public-service.md#ind-001-small-batch-assembly-process) | Industry, Business and Public-Service Video Prompts | Confirm support / 确认平台支持 |
| IND-002 | [Cold-Chain Parcel Journey](../prompts/upstream/18-industry-business-public-service.md#ind-002-cold-chain-parcel-journey) | Industry, Business and Public-Service Video Prompts | Confirm support / 确认平台支持 |
| IND-003 | [Inclusive Emergency-Exit Reminder](../prompts/upstream/18-industry-business-public-service.md#ind-003-inclusive-emergency-exit-reminder) | Industry, Business and Public-Service Video Prompts | Confirm support / 确认平台支持 |
| IND-004 | [Bilingual Service-Desk Welcome](../prompts/upstream/18-industry-business-public-service.md#ind-004-bilingual-service-desk-welcome) | Industry, Business and Public-Service Video Prompts | Confirm support / 确认平台支持 |
| EDT-001 | [Clear the Background, Preserve the Lead](../prompts/upstream/19-editing-continuation-localization.md#edt-001-clear-the-background-preserve-the-lead) | Editing, Continuation and Localization Video Prompts | Confirm support / 确认平台支持 |
| EDT-002 | [Extend a Repair-Café Closing Moment](../prompts/upstream/19-editing-continuation-localization.md#edt-002-extend-a-repair-café-closing-moment) | Editing, Continuation and Localization Video Prompts | Confirm support / 确认平台支持 |
| EDT-003 | [Localize a Product Tutorial Without Re-Shooting](../prompts/upstream/19-editing-continuation-localization.md#edt-003-localize-a-product-tutorial-without-re-shooting) | Editing, Continuation and Localization Video Prompts | Confirm support / 确认平台支持 |
| EDT-004 | [Relight an Office Demo, Change Nothing Else](../prompts/upstream/19-editing-continuation-localization.md#edt-004-relight-an-office-demo-change-nothing-else) | Editing, Continuation and Localization Video Prompts | Confirm support / 确认平台支持 |
| MRF-001 | [Three-Biome Museum Rail in One Take](../prompts/upstream/20-multireference-camera-transfer.md#mrf-001-three-biome-museum-rail-in-one-take) | Multi-Reference and Camera-Transfer Video Prompts | Confirm support / 确认平台支持 |
| MRF-002 | [Radial Cork Speaker: Transfer Motion Grammar, Not Content](../prompts/upstream/20-multireference-camera-transfer.md#mrf-002-radial-cork-speaker-transfer-motion-grammar-not-content) | Multi-Reference and Camera-Transfer Video Prompts | Confirm support / 确认平台支持 |
| MRF-003 | [Four Workshops, One Copper Thread](../prompts/upstream/20-multireference-camera-transfer.md#mrf-003-four-workshops-one-copper-thread) | Multi-Reference and Camera-Transfer Video Prompts | Confirm support / 确认平台支持 |
| MRF-004 | [Field Water-Filter Setup from Verified References](../prompts/upstream/20-multireference-camera-transfer.md#mrf-004-field-water-filter-setup-from-verified-references) | Multi-Reference and Camera-Transfer Video Prompts | Confirm support / 确认平台支持 |
| CHR-001 | [Paper Birds Plan for the Storm](../prompts/upstream/21-character-dialogue-performance.md#chr-001-paper-birds-plan-for-the-storm) | Character, Dialogue and Performance Video Prompts | Confirm support / 确认平台支持 |
| CHR-002 | [The First New Root](../prompts/upstream/21-character-dialogue-performance.md#chr-002-the-first-new-root) | Character, Dialogue and Performance Video Prompts | Confirm support / 确认平台支持 |
| CHR-003 | [Bilingual Radio-Repair Handoff](../prompts/upstream/21-character-dialogue-performance.md#chr-003-bilingual-radio-repair-handoff) | Character, Dialogue and Performance Video Prompts | Confirm support / 确认平台支持 |
| CHR-004 | [One Extra Meal: Three-Person Ensemble](../prompts/upstream/21-character-dialogue-performance.md#chr-004-one-extra-meal-three-person-ensemble) | Character, Dialogue and Performance Video Prompts | Confirm support / 确认平台支持 |
| MOG-001 | [Night-Market Poster Builds on the Beat](../prompts/upstream/22-motion-graphics-dynamic-posters.md#mog-001-night-market-poster-builds-on-the-beat) | Motion Graphics and Dynamic Poster Video Prompts | Confirm support / 确认平台支持 |
| MOG-002 | [Modular Product Feature Cards](../prompts/upstream/22-motion-graphics-dynamic-posters.md#mog-002-modular-product-feature-cards) | Motion Graphics and Dynamic Poster Video Prompts | Confirm support / 确认平台支持 |
| MOG-003 | [Museum Object Silhouette Opener](../prompts/upstream/22-motion-graphics-dynamic-posters.md#mog-003-museum-object-silhouette-opener) | Motion Graphics and Dynamic Poster Video Prompts | Confirm support / 确认平台支持 |
| MOG-004 | [Material-Swatch Motion Identity](../prompts/upstream/22-motion-graphics-dynamic-posters.md#mog-004-material-swatch-motion-identity) | Motion Graphics and Dynamic Poster Video Prompts | Confirm support / 确认平台支持 |
| SRL-001 | [The Map Rises into a Landscape](../prompts/upstream/23-surreal-physics-optical-illusions.md#srl-001-the-map-rises-into-a-landscape) | Surreal Physics and Optical-Illusion Video Prompts | Confirm support / 确认平台支持 |
| SRL-002 | [The Shadow Finishes First](../prompts/upstream/23-surreal-physics-optical-illusions.md#srl-002-the-shadow-finishes-first) | Surreal Physics and Optical-Illusion Video Prompts | Confirm support / 确认平台支持 |
| SRL-003 | [The Puddle Sees the Rain First](../prompts/upstream/23-surreal-physics-optical-illusions.md#srl-003-the-puddle-sees-the-rain-first) | Surreal Physics and Optical-Illusion Video Prompts | Confirm support / 确认平台支持 |
| SRL-004 | [One Sphere, Four Materials](../prompts/upstream/23-surreal-physics-optical-illusions.md#srl-004-one-sphere-four-materials) | Surreal Physics and Optical-Illusion Video Prompts | Confirm support / 确认平台支持 |
| VER-001 | [Honest Modular Lunch-Jar Live Demo](../prompts/upstream/24-vertical-series-live-creator.md#ver-001-honest-modular-lunch-jar-live-demo) | Vertical Series and Live-Creator Video Prompts | Confirm support / 确认平台支持 |
| VER-002 | [The Wrong Parcel, the Right Neighbor](../prompts/upstream/24-vertical-series-live-creator.md#ver-002-the-wrong-parcel-the-right-neighbor) | Vertical Series and Live-Creator Video Prompts | Confirm support / 确认平台支持 |
| VER-003 | [One Tool, Three Bicycle Fixes](../prompts/upstream/24-vertical-series-live-creator.md#ver-003-one-tool-three-bicycle-fixes) | Vertical Series and Live-Creator Video Prompts | Confirm support / 确认平台支持 |
| VER-004 | [Ceramic Creator Answers One Real Question](../prompts/upstream/24-vertical-series-live-creator.md#ver-004-ceramic-creator-answers-one-real-question) | Vertical Series and Live-Creator Video Prompts | Confirm support / 确认平台支持 |
