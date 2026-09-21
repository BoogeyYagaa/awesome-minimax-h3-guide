# Source register / 信息来源

Last reviewed: **2026-09-17**. Sources were read on this date; no hosted generation or local model inference was performed. Provider statements remain provider statements. Use current pages when making a deployment decision.

| ID | Primary source | Supports / 核验范围 |
|---|---|---|
| S1 | [MiniMax H3 open-source announcement](https://www.minimax.io/news/minimax-h3-open-source) | Base versus hosted stages; release workflow |
| S2 | [MiniMaxAI/MiniMax-H3 model card](https://huggingface.co/MiniMaxAI/MiniMax-H3) | Checkpoints, components, runtime references |
| S3 | [H3 Community License](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE) | Model terms, distinct from this project's MIT |
| S4 | [MiniMax integration directory](https://github.com/MiniMax-AI/awesome-minimax-h3-integration) | Ecosystem discovery and hosted Max status |
| S5 | [fal: Introducing H3 Max](https://blog.fal.ai/introducing-h3-max-by-fal/) | fal post-training lineage; claims attributed to provider |
| S6 | [fal H3 Max T2V API](https://fal.ai/models/minimax/h3-max/text-to-video/api) | Endpoint-specific integration documentation |
| S7 | [ComfyUI H3 tutorial](https://docs.comfy.org/tutorials/video/minimax/minimax-h3) | Native workflow entry and commercial-licensing notice |
| S8 | [Flyne AI H3 page](https://flyne.ai/model/minimax-h3/) | Browser product entry; no inference verified |
| S9 | [MiniMax H3 code repository](https://github.com/MiniMax-AI/MiniMax-H3) | Official implementation and deployment links |
| S10 | [MiniMax H3 research introduction](https://www.minimax.io/blog/minimax-h3) | Model positioning and multimodal use-case context |
| S11 | [Flyne AI homepage](https://flyne.ai/) | Flyne brand and free-tool link discovery |

## Source material reused under MIT

The prompt library is pinned separately in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md) and [the import manifest](../data/upstream-manifest.json). Imported prompt blocks are licensed reuse, not newly authored Flyne material.

## Uncertainty log / 待核验事项

- No public H3 Max checkpoint was found in the checked primary sources. Recheck before claiming availability; absence today is not a prediction.
- Free-tool pages and pricing can change. No permanent free access or rate is promised.
- On 2026-09-21 command-line access to the free H3 page returned HTTP 403, but the unsigned-in browser rendered its input form and no-sign-up instructions. See [verified interface details](quick-start.md). No generation run or reliability measurement was performed.
- Model licensing and service-specific commercial rights must be read for the intended route; this project does not collapse them into one universal grant.
- All recipes remain untested by this project. No speed, quality, conversion or hardware claim is presented as our measurement.

更改事实时，请附上官方链接、核验日期、具体变化和受影响页面；推测应保留“假设/待核验”标记。不要将聚合站或营销页面当作模型开源的唯一证据。

## Gallery and product-entry update — 2026-09-21

- [X source register](../data/community-sources.json): 12 author posts and attached media checked using the public FxTwitter reader; discovery via TapVid. Follow-up: all 12 videos decoded and visually sampled at one frame per second; no continuous playback, audio review or independent generation.
- [Community gallery](x-community-showcase.md): short excerpts and available author-prompt links; XH3-008 is partial.
- [Official examples](official-h3-examples.md): MiniMax-hosted examples, kept separate from Flyne recipes.
- [Free MiniMax H3](https://flyne.ai/free-minimax-h3/): no-sign-up trial entry subsequently confirmed from the rendered browser page. [Main model page](https://flyne.ai/model/minimax-h3/): recommended browser entry. Quotas and available controls follow the service interface.

The original model-source review date above is unchanged; this update does not imply a full re-audit of model claims.
