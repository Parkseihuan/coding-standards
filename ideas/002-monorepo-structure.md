# IDEA-002: 모노레포 구조 도입

- **상태**: 초안
- **제안일**: 2026-01-28
- **제안자**: 개발팀
- **관련 아이디어**: [IDEA-001](./001-typescript-adoption.md)
- **전환된 ADR**: -

---

## 배경

현재 16개의 개별 GitHub 저장소가 있으며, 공통 코드(CSS 변수, 유틸리티 함수 등)가
각 프로젝트에 복사되어 있어 동기화가 어렵습니다.

## 아이디어 요약

관련 프로젝트들을 하나의 모노레포로 통합하여 관리합니다.

```
yiu-projects/
├── packages/
│   ├── common-css/       # 공통 CSS
│   ├── common-utils/     # 공통 유틸리티
│   └── common-config/    # 공통 설정
├── apps/
│   ├── retirement-system/
│   ├── severance-pay/
│   ├── work-planner/
│   └── chatbot-gyomu/
├── package.json          # 워크스페이스 설정
└── turbo.json            # Turborepo 설정
```

## 예상 이점

- [ ] 공통 코드 단일 소스
- [ ] 의존성 버전 통일
- [ ] 일괄 배포 가능
- [ ] 코드 리뷰 효율화

## 예상 문제점 / 리스크

- [ ] 초기 설정 복잡
- [ ] 저장소 크기 증가
- [ ] CI/CD 파이프라인 재구성 필요
- [ ] Git 히스토리 관리 복잡

## 참고 자료

- [Turborepo 공식 문서](https://turbo.build/repo)
- [모노레포 vs 멀티레포](https://monorepo.tools/)

## 논의 기록

| 날짜 | 내용 | 결론 |
|------|------|------|
| 2026-01-28 | 초안 작성 | 규모 분석 필요 |

## 최종 결정

> 검토 대기 중
