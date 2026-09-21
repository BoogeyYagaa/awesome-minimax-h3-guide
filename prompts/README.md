# Prompt catalog / 提示词目录

**100 recipes**: 84 attributed MIT imports + 16 Flyne AI additions. All are untested by this project.

84 条引入内容保留原作者署名；16 条新增内容为概念方案，尚未实测。时长和画幅是创作目标，实际取决于所选平台。

[Choose by deliverable / 按目标选配方](../docs/use-case-matrix.md) · [Multilingual prompts / 多语言示例](../docs/multilingual-prompting.md) · [Model selection](../docs/model-guide.md) · [Workflows](../docs/workflows.md) · [Evaluation](../docs/evaluation.md) · [Attribution](../THIRD_PARTY_NOTICES.md)

Search offline: `python3 scripts/catalog.py search "product"` from the repository root.

Search includes the 100 recipes plus 12 separate, untested five-second exercises: `python3 scripts/catalog.py search "FX5-002" --origin exercise --show-prompt`. Exercises are stored in [community-sources.json](../data/community-sources.json); they did not produce the linked creator videos.

搜索覆盖 100 条配方和另列的 12 条五秒练习；练习尚未实测，不是社区视频的原始提示词。

## Browse by category / 按分类浏览

| Category / 分类 | IDs / 编号 | Typical use / 常见用途 | Recipes / 数量 |
|---|---|---|---:|
| [Flyne original scenarios / Flyne 原创场景](#flyne-ai-additions--新增场景) | FY-001–FY-016 | Product, support and editing / 商品、客服与内容制作 | 16 |
| [Brand and Advertising Video Prompts / 品牌广告](../prompts/upstream/01-brand-advertising.md) | BRD-001–BRD-003 | Product launches, local campaigns and aspect-ratio variants / 产品发布、门店活动、跨画幅广告 | 3 |
| [Product and E-commerce Video Prompts / 商品电商](../prompts/upstream/02-product-ecommerce.md) | PRD-001–PRD-003 | Product details, material studies and rotating packshots / 商品细节、材质展示、旋转展示 | 3 |
| [UGC and Lifestyle Video Prompts / 生活分享](../prompts/upstream/03-ugc-lifestyle.md) | UGC-001–UGC-003 | First impressions, everyday use and packing tests / 开箱体验、日常使用、收纳测试 | 3 |
| [Travel and Hospitality Video Prompts / 旅行住宿](../prompts/upstream/04-travel-hospitality.md) | TRV-001–TRV-003 | Destinations, accommodation and market walks / 目的地介绍、住宿展示、市场漫游 | 3 |
| [Food and Beverage Video Prompts / 餐饮饮品](../prompts/upstream/05-food-beverage.md) | FNB-001–FNB-003 | Preparation, serving and food textures / 制作过程、上菜镜头、食物质感 | 3 |
| [Fashion and Beauty Video Prompts / 时尚美妆](../prompts/upstream/06-fashion-beauty.md) | FSH-001–FSH-003 | Outfits, beauty details and styling transitions / 服装展示、妆容特写、造型切换 | 3 |
| [Cinematic Storytelling Video Prompts / 电影叙事](../prompts/upstream/07-cinematic-storytelling.md) | CIN-001–CIN-003 | Character emotion, suspense and story beats / 人物情绪、悬疑片段、故事转折 | 3 |
| [Animation and Stylized Video Prompts / 风格动画](../prompts/upstream/08-animation-stylized.md) | ANI-001–ANI-003 | Paper craft, clay characters and ink scenes / 纸艺、黏土角色、水墨场景 | 3 |
| [Action and Sports Video Prompts / 动作运动](../prompts/upstream/09-action-sports.md) | ACT-001–ACT-003 | Climbing, cycling and ball sports / 攀岩、自行车、球类动作 | 3 |
| [Fantasy, Sci-fi and VFX Video Prompts / 幻想与特效](../prompts/upstream/10-fantasy-scifi-vfx.md) | VFX-001–VFX-003 | Transformations, imagined environments and visual effects / 物体变化、幻想场景、视觉特效 | 3 |
| [UI, Game and Digital Experience Video Prompts / 界面与游戏](../prompts/upstream/11-ui-game-digital.md) | DIG-001–DIG-003 | Software onboarding, device interfaces and game actions / 软件引导、设备界面、游戏操作 | 3 |
| [Transitions, Comedy and Social Video Prompts / 转场与喜剧](../prompts/upstream/12-transitions-comedy-social.md) | SOC-001–SOC-003 | Match cuts, visual jokes and loops / 匹配剪辑、视觉笑点、循环短片 | 3 |
| [Music, Performance and Audio-Driven Video Prompts / 音乐与表演](../prompts/upstream/13-music-performance-audio.md) | MUS-001–MUS-004 | Singing, dance and rhythm visualization / 演唱、舞蹈、音乐节奏可视化 | 4 |
| [Education, Documentary and Science Video Prompts / 教育与科普](../prompts/upstream/14-education-documentary-science.md) | EDU-001–EDU-004 | Science explanations, museum stories and instruction / 科学解释、博物馆介绍、操作教学 | 4 |
| [Architecture, Interiors and Real-Estate Video Prompts / 建筑与室内](../prompts/upstream/15-architecture-interiors-real-estate.md) | ARC-001–ARC-004 | Property tours, daylight and renovation previews / 房屋参观、光照变化、装修预演 | 4 |
| [Automotive and Mobility Video Prompts / 交通与出行](../prompts/upstream/16-automotive-mobility.md) | MOB-001–MOB-004 | Vehicle interiors, cycling and rail journeys / 汽车内饰、自行车、列车体验 | 4 |
| [Nature, Animals and Pet Video Prompts / 自然与宠物](../prompts/upstream/17-nature-animals-pets.md) | NAT-001–NAT-004 | Wildlife, pet accessories and plant observation / 野生动物、宠物用品、植物观察 | 4 |
| [Industry, Business and Public-Service Video Prompts / 工业与公共服务](../prompts/upstream/18-industry-business-public-service.md) | IND-001–IND-004 | Production, logistics, evacuation and service guidance / 生产流程、物流、疏散与服务说明 | 4 |
| [Editing, Continuation and Localization Video Prompts / 视频编辑与延续](../prompts/upstream/19-editing-continuation-localization.md) | EDT-001–EDT-004 | Cleanup, continuation, localization and relighting / 背景清理、续拍、语言适配、重新打光 | 4 |
| [Multi-Reference and Camera-Transfer Video Prompts / 多参考与运镜](../prompts/upstream/20-multireference-camera-transfer.md) | MRF-001–MRF-004 | One-takes, camera-motion transfer and matched actions / 一镜到底、镜头运动迁移、动作衔接 | 4 |
| [Character, Dialogue and Performance Video Prompts / 角色与对话](../prompts/upstream/21-character-dialogue-performance.md) | CHR-001–CHR-004 | Character acting, bilingual dialogue and ensemble scenes / 人物表演、双语对话、多人场景 | 4 |
| [Motion Graphics and Dynamic Poster Video Prompts / 动态图形与海报](../prompts/upstream/22-motion-graphics-dynamic-posters.md) | MOG-001–MOG-004 | Poster assembly, feature cards and exhibition openings / 海报组装、功能卡片、展览片头 | 4 |
| [Surreal Physics and Optical-Illusion Video Prompts / 超现实与错觉](../prompts/upstream/23-surreal-physics-optical-illusions.md) | SRL-001–SRL-004 | Material changes, time offsets and spatial illusions / 材质变化、时间错位、空间错觉 | 4 |
| [Vertical Series and Live-Creator Video Prompts / 竖屏连载与直播](../prompts/upstream/24-vertical-series-live-creator.md) | VER-001–VER-004 | Product demonstrations, short drama, repair series and answers / 产品演示、短剧、维修连载、问答 | 4 |

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
