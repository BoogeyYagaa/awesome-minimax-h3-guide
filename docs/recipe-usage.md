# 先选使用入口 / Choose a compatible route

本页按 **2026-09-21 已查看的免费界面**标注配方使用条件：5 秒、480p、16:9 / 9:16 / 1:1、纯文字或首尾两张图片。标签说明输入是否符合已观察到的界面，不表示生成成功或效果合格。产品以后可能变化，以当前页面为准。

| 目录标签 | 怎么使用 | 例子 |
|---|---|---|
| Free text / 免费文字 | 无需图片，可从免费入口尝试 | [FY-001 台灯](../prompts/flyne/fy-001.md) |
| Both frames / 准备首尾图 | 先备好有权使用的首帧和尾帧；这条配方使用同一张桌面静帧作为两端输入 | [FY-004 菜单循环](../prompts/flyne/fy-004.md) |
| Shorten first / 先缩短时长 | 原方案为 6 秒，需要自行简化成 5 秒；原文保留 | [FY-009 字幕背景](../prompts/flyne/fy-009.md) |
| Confirm support / 确认平台支持 | 按条目准备人物、产品、视频或音频参考，并确认所选平台支持其用途和时长 | [FY-002 商品配色](../prompts/flyne/fy-002.md)、引入配方 |

**多张参考图不等于首尾帧。** 例如 FY-002 的包款图决定外形，色卡决定材质颜色；把这两张图分别当首帧与尾帧，会改变原来的任务含义。免费入口不能直接承接这类多参考工作流。

[免费工具](https://flyne.ai/free-minimax-h3/) · [FlyneAI H3 进阶入口](https://flyne.ai/model/minimax-h3/) · [五秒入门练习](quick-start.md)

进阶入口也需要逐项确认支持范围，本仓库没有把所有多参考、编辑、声音控制能力都当作 FlyneAI 已支持功能。参考图只提供其中一个素材时，配方旁边会说明还缺什么。

## 按条件搜索

```sh
python3 scripts/catalog.py search "" --route free-text
python3 scripts/catalog.py search "" --route free-frames
python3 scripts/catalog.py search "FY-002" --show-prompt
```

`data/recipe-usage.json` 保存每条配方的输入、目标时长与使用条件。配方内容、标签和实际界面发生变化时需一起复核。

## English

Labels describe compatibility with the observed free interface, not verified video quality. Text-only five-second recipes can be tried without images; frame-conditioned recipes need both endpoint images. Longer text recipes need timing adaptation. Multi-reference, source-video editing, audio references and longer sequences require a route whose current controls support those exact roles. The advanced Flyne link is a starting point for checking, not a claim that it supports every recipe. Input roles and target formats are searchable metadata; original prompts remain unchanged.
