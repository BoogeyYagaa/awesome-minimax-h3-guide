# Awesome MiniMax H3 Guide · Flyne AI

![Flyne AI MiniMax H3 field guide](assets/flyne-h3-cover.png)

<sub>표지는 AI로 만든 소개 이미지이며 H3 출력이 아닙니다.</sub>

[English](README.md) · [简体中文](README_zh.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Français](README_fr.md) · [Deutsch](README_de.md) · [Português](README_pt.md)

[5초 시작 안내](docs/quick-start.md) · [참고 이미지](docs/reference-gallery.md) · [프롬프트 작성](docs/prompting-guide.md) · [템플릿 12개](templates/README.md) · [로컬 실행](docs/deployment-guide.md)

## Flyne AI에서 MiniMax H3 사용

| 추천 온라인 이용 경로 | 가입 없이 무료 체험 |
|---|---|
| [MiniMax H3](https://flyne.ai/model/minimax-h3/) | [온라인에서 바로 시험하기](https://flyne.ai/free-minimax-h3/) |

2026-09-21에 확인한 무료 도구는 **5초·480p** 영상을 제공합니다. [5초 연습](docs/quick-start.md)부터 시작하세요.

## 영상과 프롬프트 보기

X 사례 12개: 영상, 원문, 짧은 발췌와 해설.

[全部案例 / All examples](docs/x-community-showcase.md) · [官方示例 / Official examples](docs/official-h3-examples.md)


## 실제 영상 제작을 위한 MiniMax H3 가이드

Flyne AI가 정리한 커뮤니티 자료입니다. 프롬프트 100개와 제작 흐름, 모델 선택, 품질·비용 평가를 제공합니다. 84개는 출처를 표시한 MIT 라이선스 재사용 자료이며, 16개는 Flyne AI의 신규 제안입니다. 이 프로젝트에서 생성 결과를 검증한 것은 아닙니다.

[전체 프롬프트](prompts/README.md) · [Flyne AI에서 사용](https://flyne.ai/model/minimax-h3/) · [모델 상세](docs/model-guide.md)

## 시작하기

납품 목적에 맞는 레시피를 고르고 참조 자료의 역할을 확인하세요. 선택한 화면이 지원하는 입력만 사용하고, 처음에는 피사체 하나와 동작 하나로 시작합니다. 결과의 형태·움직임·소리를 검토하고 한 번에 한 종류의 문제를 수정한 뒤 실행 기록을 남깁니다.

[Run record](templates/run-record.json) · [Prompt template](templates/prompt.md)

## 용도별 시작점

| ID | 용도별 시작점 |
|---|---|
| FY-002 | [상품 색상 변형](prompts/flyne/fy-002.md) |
| FY-003 | [고객 지원](prompts/flyne/fy-003.md) |
| FY-006 | [다국어 안내](prompts/flyne/fy-006.md) |
| FY-009 | [자막용 배경](prompts/flyne/fy-009.md) |
| FY-016 | [참조 제어 평가](prompts/flyne/fy-016.md) |

## 모델과 공개 상태

2026-09-17 기준 H3-Base 가중치는 다운로드할 수 있습니다. H3 Max는 fal이 후속 학습한 호스팅 모델이며, 확인한 1차 자료에서 공개 가중치를 찾지 못했습니다. 공식 전체 2K 작업 흐름에도 호스팅 단계가 포함됩니다. 저장소의 MIT 라이선스와 모델의 Community License는 별개입니다.

[모델 상세](docs/model-guide.md) · [출처](docs/sources.md)

## 문서와 검색

- [제작 흐름](docs/workflows.md)
- [품질과 비용](docs/evaluation.md)
- [향후 활용 가설](docs/opportunities.md)
- [출처](docs/sources.md)

Python 3.9+:

```sh
python3 scripts/catalog.py search "product"
python3 scripts/catalog.py search "FY-002" --show-prompt
python3 scripts/catalog.py build
python3 scripts/validate.py
```

[JSON catalog](data/catalog.json)

## 출처 표시와 참여

기존 84개 프롬프트의 저작권 표시와 MIT 라이선스는 Flaq AI에 귀속됩니다. 단순한 표현 변경을 독창적 제작으로 취급하지 않습니다. 신규 제안은 미검증 상태입니다. README는 8개 언어, 상세 가이드는 영어와 중국어 요약, 프롬프트 본문은 영어입니다. Flyne AI의 요금·입력 모드·접근 조건은 현재 제품 화면을 확인하세요.

[제3자 권리 표시](THIRD_PARTY_NOTICES.md) · [기여 안내](CONTRIBUTING.md) · [MIT](LICENSE) · [Flaq AI MIT](licenses/Flaq-AI-MIT.txt)

## Flyne AI 제휴 파트너가 되어 주세요

크리에이터, 교육자, 리뷰어, 제작 팀의 참여를 환영합니다! 전용 추천 링크로 Flyne AI를 소개하고, 조건에 맞는 유효한 유료 주문에 대해 수수료를 받을 수 있습니다.

- 추천 사용자의 첫 유효 유료 주문: **20%**.
- 해당 사용자 가입 후 **60일 이내**의 후속 유효 유료 주문: **10%**.

[Flyne AI 제휴 프로그램 참여하기](https://flyne.ai/affiliate-program/). 주문 자격, 추천 귀속 및 지급은 현재 제휴 약관과 심사 결과에 따릅니다.

질문이나 제휴 문의는 [contact@flyne.ai](mailto:contact@flyne.ai)로 연락해 주세요.
