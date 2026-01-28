# Coding Standards

> 모든 프로젝트에서 일관된 코드 품질을 유지하기 위한 표준 문서 및 템플릿

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

## 폴더 구조

```
coding-standards/
├── CLAUDE.md              # Claude Code 글로벌 지침
├── CODING_STANDARDS.md    # 전체 표준 문서
├── templates/
│   ├── css/
│   │   ├── variables.css  # CSS 커스텀 프로퍼티
│   │   └── base.css       # 기본 스타일
│   ├── js/
│   │   ├── config.js      # 설정 템플릿
│   │   └── utils.js       # 유틸리티 함수
│   └── python/
│       ├── main.py        # FastAPI 앱 템플릿
│       └── config.py      # 설정 관리
├── snippets/              # 자주 쓰는 코드 조각
└── checklists/            # 프로젝트 체크리스트
```

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

## 업데이트

표준 문서는 지속적으로 업데이트됩니다. 주기적으로 pull 하여 최신 상태를 유지하세요:

```bash
cd coding-standards
git pull origin main
```

---

**최종 수정**: 2026-01-28
