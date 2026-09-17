# Evaluate usable outputs / 质量与成本评估

This protocol is an original proposal. No benchmark results have been collected.

## A small reproducible comparison

Select six briefs: product geometry, single-person movement, two-speaker dialogue, camera transfer, localized text, and background-only editing. Generate three attempts per brief per candidate route. Keep input files, intent, duration and framing comparable. Record seeds when supported; the same seed across different models does not imply comparable noise.

Label videos anonymously, randomize order, and have two reviewers score independently. Report disagreement and sample size. Keep failed jobs and rejected outputs in the denominator; do not compare a best-of-ten result with a single baseline sample.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Required action | Missing | Partial | Complete and ordered |
| Identity / geometry | Major drift | Visible minor drift | Stable at delivery size |
| Temporal continuity | Breaking artifacts | Repairable defect | Clean motion and cuts |
| Audio / timing | Missing or wrong | Usable after repair | Correct and aligned |
| Composition | Unusable crop | Needs reframe | Fits placement |

**Proposed gate:** at least 8/10, with no zero in the first three dimensions. Rights problems, false product claims, unusable required text or an incorrect critical instruction override the numeric score and fail the clip. These are project thresholds, not model guarantees. Add domain-specific checks before evaluating safety-sensitive material.

## Cost formulas

```text
pass_rate = accepted_outputs / all_attempts
cost_per_accepted_clip = (generation + retries + editing + review + allocated_infrastructure) / accepted_outputs
cost_per_accepted_second = total_cost / accepted_final_seconds
```

Use a consistent currency and time period. If there are no accepted outputs, the unit cost is undefined; never report zero. Include idle GPU time in a realistic self-hosted utilization scenario. Capture p50/p95 end-to-end latency only when the sample size is meaningful; for a tiny trial publish the individual times instead.

For business A/B tests, hold placement, audience, landing page and spend rules constant. Evaluate conversion and retention separately from video-quality scores. Better-looking videos do not establish a conversion lift.

## 中文说明

建议用 6 类任务、每种路线每类 3 次尝试，保留失败样本。两位评审盲评动作完成度、主体稳定性、时序、声音、构图；8/10 是本项目建议门槛，不是模型成绩。版权、事实及关键操作错误直接判不合格。

成本以“每条合格成片”和“每秒合格成片”计算，纳入重试、剪辑、审核及基础设施。没有合格输出时成本不可计算。不要把推理时长当端到端等待时间，也不要把平台排行榜转化为自身效果保证。

Use [run-record.json](../templates/run-record.json) and [evaluation.csv](../templates/evaluation.csv). The CSV is an empty logging template, not benchmark data.
