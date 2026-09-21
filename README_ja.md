# Awesome MiniMax H3 Guide · Flyne AI

![Flyne AI MiniMax H3 field guide](assets/flyne-h3-cover.png)

<sub>表紙は AI 生成のイメージ画像で、H3 の出力ではありません。</sub>

[English](README.md) · [简体中文](README_zh.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Français](README_fr.md) · [Deutsch](README_de.md) · [Português](README_pt.md)

## Flyne AI で MiniMax H3 を使う

| おすすめのブラウザー版 | 登録不要の無料体験 |
|---|---|
| [MiniMax H3](https://flyne.ai/model/minimax-h3/) | [オンラインですぐに試す](https://flyne.ai/free-minimax-h3/) |

## 動画とプロンプトを見る

X の作例 12 件。動画、原投稿、短い抜粋と解説を掲載。

[全部案例 / All examples](docs/x-community-showcase.md) · [官方示例 / Official examples](docs/official-h3-examples.md)


## 実用的な動画制作のための MiniMax H3 ガイド

100 件のプロンプト、制作手順、モデル選択、品質・コスト評価をまとめた Flyne AI のコミュニティ資料です。84 件は出典を明記した MIT ライセンスの再利用、16 件は Flyne AI の新規案です。本プロジェクトでは生成結果を検証していません。

[プロンプト一覧](prompts/README.md) · [Flyne AI で試す](https://flyne.ai/model/minimax-h3/) · [モデルの詳細](docs/model-guide.md)

## 使い始める

納品物に合うレシピを選び、参照素材の役割を確認します。利用画面が受け付ける入力だけを使い、まず一つの被写体と動作に絞ってください。生成後は形状・動き・音声を確認し、問題を一つずつ修正して実行記録を残します。

[Run record](templates/run-record.json) · [Prompt template](templates/prompt.md)

## 用途別の入口

| ID | 用途別の入口 |
|---|---|
| FY-002 | [商品バリエーション](prompts/flyne/fy-002.md) |
| FY-003 | [カスタマーサポート](prompts/flyne/fy-003.md) |
| FY-006 | [多言語対応](prompts/flyne/fy-006.md) |
| FY-009 | [字幕用背景](prompts/flyne/fy-009.md) |
| FY-016 | [参照制御の評価](prompts/flyne/fy-016.md) |

## モデルと公開状況

2026-09-17 時点では H3-Base の重みを取得できます。H3 Max は fal が追加学習したホスト型モデルで、確認した一次資料では公開重みが見つかりませんでした。公式の完全な 2K ワークフローにもホスト型の処理が含まれます。リポジトリの MIT とモデルの Community License は別です。

[モデルの詳細](docs/model-guide.md) · [出典](docs/sources.md)

## 資料と検索

- [制作手順](docs/workflows.md)
- [品質とコスト](docs/evaluation.md)
- [今後の活用仮説](docs/opportunities.md)
- [出典](docs/sources.md)

Python 3.9+:

```sh
python3 scripts/catalog.py search "product"
python3 scripts/catalog.py search "FY-002" --show-prompt
python3 scripts/catalog.py build
python3 scripts/validate.py
```

[JSON catalog](data/catalog.json)

## クレジットと参加

元の 84 件の著作権表示と MIT ライセンスは Flaq AI に帰属します。軽い言い換えを独自制作とは扱いません。新規案は未検証です。README は 8 言語、詳しいガイドは英語と中国語の要約、プロンプト本文は英語です。Flyne AI の料金・入力モード・利用条件は現在の製品画面で確認してください。

[第三者の権利表示](THIRD_PARTY_NOTICES.md) · [貢献ガイド](CONTRIBUTING.md) · [MIT](LICENSE) · [Flaq AI MIT](licenses/Flaq-AI-MIT.txt)

## Flyne AI のアフィリエイトパートナーになりませんか

クリエイター、教育者、レビュアー、制作チームの皆さまの参加を歓迎します！専用の紹介リンクで Flyne AI を紹介し、対象となる有効な有料注文に応じた報酬を受け取れます。

- 紹介したユーザーの初回の有効な有料注文：**20%**。
- そのユーザーの登録から **60 日以内**の、その後の有効な有料注文：**10%**。

[Flyne AI アフィリエイトプログラムに参加](https://flyne.ai/affiliate-program/)。対象注文、成果の帰属、支払いは、最新の規約と審査に従います。

ご質問や提携のご相談は [contact@flyne.ai](mailto:contact@flyne.ai) までご連絡ください。
