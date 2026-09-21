# From a brief to an approved clip / 实用工作流

These are proposed production workflows, not measured H3 results. Start with [model selection](model-guide.md).

Choose by task: [deliverable-to-recipe matrix](use-case-matrix.md) · [reusable production templates](../templates/README.md) · [localized prompt examples](multilingual-prompting.md). For implementation: [local deployment walkthrough](deployment-guide.md) · [API integration flow](api-workflow.md) · [official scripts and example outputs](official-h3-examples.md).

## 1. Browser workflow on Flyne AI

1. Choose a recipe from the [catalog](../prompts/README.md). For a first attempt, use FY-001 without references or take one short beat from an imported recipe.
2. Open [Flyne AI's H3 page](https://flyne.ai/model/minimax-h3/). Select the available mode, duration and aspect ratio in the current interface.
3. Replace placeholders and remove instructions for inputs the selected interface does not accept. Ref2VA recipes are not automatically compatible with a text/image-only page.
4. Generate a structural draft. Review product geometry and movement before adding dialogue, typography or transitions.
5. Save the exact prompt, model label, settings, input rights and output in a [run record](../templates/run-record.json). Change one variable per retry.

The unsigned-in [free H3 page](https://flyne.ai/free-minimax-h3/) was inspected in a browser on 2026-09-21. It showed five-second 480p output, three aspect ratios and optional two-frame guidance. Start with the [quick-start guide](quick-start.md) and a five-second exercise. A separate signed-in attempt with FX5-002 reached the free queue after manual verification on 2026-09-21, as recorded in the [quick start](quick-start.md). No generated output was available for review at that observation. The unsigned-in interface check and signed-in submission are separate observations; neither establishes no-signup generation success, service reliability, API compatibility or H3 Max availability.

## 2. Local H3-Base

- Choose a runtime through the [official H3 repository](https://github.com/MiniMax-AI/MiniMax-H3) and its linked deployment recipes. Pin the runtime commit and model revision before installation.
- For a visual first run, use [ComfyUI's native H3 tutorial](https://docs.comfy.org/tutorials/video/minimax/minimax-h3): select a template, install its matching components, then run a short baseline before extensions.
- For serving or research, follow the currently linked SGLang, vLLM or diffusers integration. Do not mix file layouts between runtimes.
- Budget the transformer, text encoder, image/video VAE, audio VAE, activations, host offload and disk together. A weight file's size is not peak VRAM. Quantized variants are a separate evaluation track.
- Record peak memory, cold/warm latency and output failures. Add adapters only after the baseline is reproducible.

Illustrative download command from the official release, **not executed here**:

```sh
# Requires the Hugging Face CLI and sufficient disk space.
# Check the model license and access requirements first.
hf download MiniMaxAI/MiniMax-H3 --include "FL2VA/*" --local-dir MiniMax-H3
```

This obtains checkpoint files; it is not a complete install or inference command. Use the runtime-specific instructions for inference. [Official release](https://www.minimax.io/news/minimax-h3-open-source).

## 3. Hosted H3 Max

Start at the provider's [T2V API schema](https://fal.ai/models/minimax/h3-max/text-to-video/api), [I2V schema](https://fal.ai/models/minimax/h3-max/image-to-video/api), or [reference endpoint](https://fal.ai/models/minimax/h3-max/reference-to-video). The endpoint and request fields belong to fal, not Flyne.

Keep keys on the server. Save request IDs before polling; cap concurrency and retry budgets. A retry can create another billable generation. Record queue time separately from inference and download time. For webhooks, use the provider's current verification mechanism. This repository makes no paid calls.

## 4. Multi-shot delivery

Create a shot ledger before generation: shot ID, opening/closing state, identity reference, camera direction, dialogue and cut point. Select a stable end frame for the next shot; inspect the join for pose, light, lens and sound discontinuities. Generate short shots independently and edit the sequence. A longer final film is an edited workflow, not a claim of arbitrary-length native generation.

## 中文执行清单

1. 先确定交付目标，再选文字、首尾帧或多参考路线；平台没有的输入能力不能靠提示词补出来。
2. 素材角色写清楚：图片 A 管产品外形，图片 B 管环境，视频 C 只管运镜，音频 D 只管节奏。
3. 第一轮只验证动作与主体稳定性；第二轮修复最严重的问题；文字及精确字幕必要时后期制作。
4. 每条镜头记录开头状态和结束状态，多镜头保持人物、镜头方向与光线连续。
5. 本地部署先跑基线再做量化、蒸馏或 LoRA；托管工作流记录请求编号，设置预算并区分排队与推理。
6. 上线前按[评估表](evaluation.md)复核，并保存可复现记录。
