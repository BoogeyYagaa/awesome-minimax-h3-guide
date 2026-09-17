# H3, H3 Max and open weights / 模型与开放权重

Verified: **2026-09-17**. Source IDs refer to the [source register](sources.md). Availability is a dated observation, not a promise about future releases.

| Component | Access at verification | Practical role |
|---|---|---|
| H3-Base FL2VA | Downloadable weights | Text-only or first/last-frame audiovisual generation |
| H3-Base Ref2VA | Downloadable weights | Generation guided by image, video and audio references |
| H3-Context-IR | Hosted in the documented official pipeline | Prepares complex context before generation |
| H3-Regenerate-2K | Hosted in the documented official pipeline | Regenerates a base result using the original context |
| H3 Max | fal-hosted post-trained H3 derivative; no public weights found | Evaluate as a managed production service |

Base/task distinctions: [official model card](https://huggingface.co/MiniMaxAI/MiniMax-H3) (S2). Max access status: [MiniMax integration directory](https://github.com/MiniMax-AI/awesome-minimax-h3-integration#hosted--the-h3-max-family) (S4); lineage: [fal announcement](https://blog.fal.ai/introducing-h3-max-by-fal/) (S5).

H3's official release describes native audio/video, 4–15-second outputs and a local 768p base stage. The full official 2K route includes hosted components. “H3 is open” therefore does not imply that every component of the service can run offline. [MiniMax release announcement](https://www.minimax.io/news/minimax-h3-open-source) (S1).

## What “H3 Max open source” currently means

H3 Max was built on H3's open-weight foundation. That is different from downloadable Max weights. Do not label community quantizations, Turbo LoRAs or acceleration adapters as “H3 Max open source.” A future release should be marked available only after a provider-owned model repository, actual weight files, license and runnable inference instructions exist together. Social posts or plans alone are not a release. No future release date is asserted here.

fal reports improvements in instruction following, aesthetics and serving speed. Treat those as provider claims until reproduced on your workload; this repository publishes no measured speedup or ranking. [fal announcement](https://blog.fal.ai/introducing-h3-max-by-fal/) (S5).

## License boundary

The repository is MIT. H3 weights use the **MiniMax H3 Community License**, not this repository's MIT license. The checked license includes territorial restrictions, additional commercial conditions and use restrictions; inspect the exact version for your deployment. The ComfyUI guide separately describes commercial licensing through Comfy. Do not turn these into an unconditional “free commercial use everywhere” claim. Resolve your location, use and service route against the current terms. [Model license](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE) (S3), [ComfyUI guide](https://docs.comfy.org/tutorials/video/minimax/minimax-h3) (S7).

## 选择建议（中文）

- **只有文字或首尾帧**：从 FL2VA 路线开始，把时长与分镜压缩到一个可验证的动作。
- **必须保持人物、产品或动作参考**：评估 Ref2VA；每个素材只承担明确的参考角色。
- **需要本地控制与定制**：评估 H3-Base、兼容运行时及许可；硬件成本应包含文本编码器、VAE、内存、磁盘和运行维护。
- **需要托管交付**：比较具体端点的质量、排队时延与每条合格成片成本。H3 Max 属于这一类，不是本地权重的别名。
- **需要 2K**：官方完整流程含托管环节；敏感素材不能因“本地 Base”而自动视为全程不出域。

关键结论：目前可下载的是 H3-Base；本次核验未发现 H3 Max 公共权重。若未来开放，以模型文件、许可证、推理代码及来源四项证据更新，而非把发布计划当作已开源。
