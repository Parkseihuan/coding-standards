# Architecture Decision Records (ADR)

> 코딩 표준 및 아키텍처 결정의 히스토리를 관리합니다.

## ADR이란?

**Architecture Decision Record**는 중요한 아키텍처/설계 결정을 문서화하는 방법입니다.
각 결정에 대해 **왜** 그 결정을 내렸는지, **어떤 대안**이 있었는지, **결과**가 무엇인지를 기록합니다.

## 상태 정의

| 상태 | 설명 |
|------|------|
| `제안됨` | 검토 중인 결정 |
| `수락됨` | 현재 적용 중인 결정 |
| `폐기됨` | 더 이상 사용하지 않는 결정 |
| `대체됨` | 다른 ADR로 대체된 결정 (링크 포함) |

## ADR 목록

<!-- AUTO-GENERATED-START -->
| 번호 | 제목 | 상태 | 날짜 | 관련 ADR |
|------|------|------|------|----------|
| [ADR-0001](0001-css-inline-style-prohibition.md) | 인라인 스타일 금지 정책 | 수락됨 | 2026-01-27 | - |
| [ADR-0002](0002-python-src-structure.md) | Python src/ 패키지 구조 강제 | 수락됨 | 2026-01-27 | - |
| [ADR-0003](0003-fastapi-over-flask.md) | FastAPI 우선 채택 | 수락됨 | 2026-01-27 | [ADR-0002](0002-*.md) |
<!-- AUTO-GENERATED-END -->

## ADR 작성 방법

1. `_template.md`를 복사하여 새 파일 생성
2. 파일명: `NNNN-<짧은-제목>.md` (예: `0004-use-typescript.md`)
3. 내용 작성 후 커밋
4. `scripts/generate-summary.py` 실행하여 목록 자동 업데이트

## 관련 링크

- [ADR GitHub 공식 저장소](https://adr.github.io/)
- [Michael Nygard의 ADR 소개](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
