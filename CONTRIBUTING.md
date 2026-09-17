# Contributing / 贡献指南

Useful contributions improve reproducibility: test a recipe, document a failed result, add a missing workflow, correct a translation, or update a claim with a primary source.

## Propose a prompt

1. Start from [the prompt template](templates/prompt.md). State the deliverable, reference roles, task family, timing, constraints, acceptance criteria and a recovery path.
2. Identify your authorship and the source/license of any reused text. Keep imported copyright and license notices. Do not describe a lightly rewritten imported recipe as independently authored.
3. Mark a new recipe `conceptual`. To mark it tested, include the exact provider/model, date, settings, prompt, licensed inputs, output location and defects in a [run record](templates/run-record.json).
4. Avoid unsupported product claims and unconsented identity or voice references. Use synthetic data in UI, training and support examples.
5. Keep generated examples distinct from official examples and reference images. Do not add an output gallery without reproducible provenance.

## Change the catalog

For FY entries, update both the Markdown recipe and its metadata/prompt in `data/flyne-recipes.json`. The validator checks that the prompt bodies agree. Run:

```sh
python3 scripts/catalog.py build
python3 scripts/validate.py
```

The current release expects 100 recipes (84 imported + 16 new). When adding a recipe, update documented counts, the banner and validator expectations together. Do not edit generated `data/catalog.json` or `prompts/README.md` by hand.

For upstream updates, review a fixed source revision, retain its license, compare each prompt, and update `data/upstream-manifest.json` deliberately. Never silently rewrite provenance hashes to hide a change. New source revisions should have a changelog entry.

## Update facts and translations

Add a provider-owned source, checked date and the specific claim supported. Separate release availability, announcements and predictions. Update all eight README entry pages when a shared fact changes. Detailed guides use English and Chinese summaries; translated entries should describe this scope accurately.

Run records may contain private inputs or account identifiers. Publish only material intended for public release, with secrets removed. Report exposed credentials privately to their owner and rotate them; do not post them in issues.

## 中文

欢迎补充真实生成记录、失败案例、场景及翻译。新增条目先标记为未实测；声称已测试时必须附模型版本、配置、素材来源、结果和问题。引入内容保留署名与许可证。事实更新使用官方来源并注明日期。提交前运行目录生成和检查脚本。

Contributions are accepted under the root MIT license for new work; existing third-party notices remain applicable. This repository is independent of MiniMax.
