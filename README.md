# Coding Standards

> 모든 프로젝트에서 일관된 코드 품질을 유지하기 위한 표준 문서, 템플릿, 그리고 결정 히스토리

## 레포지토리 구조

```
coding-standards/
├── CLAUDE.md              # Claude Code 글로벌 지침
├── CODING_STANDARDS.md    # 전체 표준 문서
├── CHANGELOG.md           # 변경 이력 (자동 생성)
├── RELATIONS.md           # ADR 관계도 (자동 생성)
│
├── decisions/             # Architecture Decision Records (ADR)
│   ├── README.md          # ADR 목록 및 가이드
│   ├── _template.md       # ADR 작성 템플릿
│   └── 0001-*.md          # 각 결정 문서
│
├── ideas/                 # 아이디어 & 개선 제안
│   ├── README.md          # 아이디어 목록
│   ├── _template.md       # 아이디어 작성 템플릿
│   └── 001-*.md           # 각 아이디어 문서
│
├── templates/             # 코드 템플릿
│   ├── css/
│   ├── js/
│   └── python/
│
├── scripts/               # 자동화 스크립트
│   └── generate_summary.py  # 요약 자동 생성
│
├── snippets/              # 자주 쓰는 코드 조각
└── checklists/            # 프로젝트 체크리스트
```

## 핵심 기능

### 1. ADR (Architecture Decision Records)

중요한 아키텍처/설계 결정을 문서화합니다:
- **왜** 그 결정을 내렸는지
- **어떤 대안**이 있었는지
- **결과**가 무엇인지

[ADR 목록 보기](./decisions/README.md)

### 2. 아이디어 관리

새로운 아이디어를 체계적으로 관리합니다:
- 초안 → 검토중 → 채택됨/거절됨
- 채택된 아이디어는 ADR로 전환

[아이디어 목록 보기](./ideas/README.md)

### 3. 자동 요약 생성

```bash
python scripts/generate_summary.py
```

실행 시 자동으로:
- `CHANGELOG.md` 생성 (날짜별 변경 이력)
- `RELATIONS.md` 생성 (ADR 관계도)
- 각 README.md의 목록 업데이트

## 사용 방법

### 1. Claude Code와 함께 사용

`CLAUDE.md` 파일을 홈 디렉토리에 복사하면 Claude Code가 모든 프로젝트에서 자동으로 참조합니다:

```bash
# Windows
copy CLAUDE.md %USERPROFILE%\.claude\CLAUDE.md

# Mac/Linux
cp CLAUDE.md ~/.claude/CLAUDE.md
```

### 2. 새 프로젝트 시작 시

필요한 템플릿을 복사하여 사용:

```bash
# CSS 변수 복사
copy templates\css\variables.css 프로젝트\css\

# JavaScript 설정 복사
copy templates\js\config.js 프로젝트\js\

# Python FastAPI 템플릿 복사
copy templates\python\* 프로젝트\src\
```

## 빠른 시작

### 새 결정 기록하기

1. `decisions/_template.md`를 복사
2. `decisions/NNNN-<제목>.md`로 저장
3. 내용 작성 후 커밋
4. `python scripts/generate_summary.py` 실행

### 새 아이디어 제안하기

1. `ideas/_template.md`를 복사
2. `ideas/NNN-<제목>.md`로 저장
3. 내용 작성 후 커밋

## 핵심 표준 요약

### CSS
- 인라인 스타일 금지
- CSS 변수 사용 (`variables.css`)
- 색상: `--color-primary: #667eea`

### JavaScript
- `CONFIG` 객체로 설정 관리
- `fetchWithRetry` 패턴으로 API 호출
- async/await 사용

### Python
- FastAPI 사용 (Flask 대신)
- pydantic-settings로 환경 변수 관리
- 타입 힌트 필수

## 프로젝트 체크리스트

새 프로젝트 시작 시:

- [ ] README.md 생성
- [ ] .gitignore 설정
- [ ] CSS 변수 파일 복사
- [ ] config 파일 생성
- [ ] .env.example 생성
- [ ] CLAUDE.md 복사 (선택)

## 관련 프로젝트

이 표준을 적용한 프로젝트들:

- [chatbot-gyomu](https://github.com/Parkseihuan/chatbot-gyomu) - AI 챗봇
- [RAG](https://github.com/Parkseihuan/RAG) - RAG 시스템

## 워크플로우

```
아이디어 제안 → 검토 → 채택 → ADR 작성 → 구현
     ↓           ↓
   거절됨      보류됨
```

1. **아이디어 제안**: `ideas/` 폴더에 새 아이디어 작성
2. **검토**: 팀에서 논의 및 피드백
3. **채택**: 아이디어가 수락되면 ADR로 전환
4. **ADR 작성**: `decisions/` 폴더에 공식 결정 문서 작성
5. **구현**: 코딩 표준에 반영

## 관련 문서

- [CHANGELOG.md](./CHANGELOG.md) - 날짜별 변경 이력
- [RELATIONS.md](./RELATIONS.md) - ADR 관계도 (Mermaid 다이어그램)
- [decisions/README.md](./decisions/README.md) - ADR 목록 및 가이드
- [ideas/README.md](./ideas/README.md) - 아이디어 목록

## 업데이트

표준 문서는 지속적으로 업데이트됩니다. 주기적으로 pull 하여 최신 상태를 유지하세요:

```bash
cd coding-standards
git pull origin main

# 요약 재생성
python scripts/generate_summary.py
```

---

**최종 수정**: 2026-02-02
