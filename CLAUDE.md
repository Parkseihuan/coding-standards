# Claude Code 프로젝트 지침

> 이 파일은 Claude Code가 모든 프로젝트에서 참조하는 글로벌 코딩 표준입니다.
> 홈 디렉토리(~/.claude/)에 복사하여 사용하세요.

## 기본 원칙

1. **한국어 우선**: 주석, 커밋 메시지, 문서는 한국어로 작성
2. **단순함 추구**: 과도한 추상화 금지, 필요한 것만 구현
3. **일관성 유지**: 이 문서의 표준을 따름

---

## CSS 표준

### 필수 규칙
- **인라인 스타일 금지** - 모든 스타일은 CSS 파일로 분리
- **CSS 변수 사용** - `templates/css/variables.css` 참조
- **BEM 네이밍** 권장 (예: `.card__title`, `.btn--primary`)

### 색상 팔레트
```css
--color-primary: #667eea;      /* 메인 브랜드 색상 */
--color-primary-dark: #5a67d8;
--color-secondary: #764ba2;
--color-success: #10b981;
--color-warning: #f59e0b;
--color-danger: #ef4444;
```

### 파일 구조
```
css/
├── variables.css   # CSS 변수 정의
├── base.css        # 리셋 및 기본 스타일
├── components.css  # 버튼, 카드, 폼 등
└── utilities.css   # 유틸리티 클래스
```

---

## JavaScript 표준

### 필수 규칙
- **CONFIG 객체** 사용 - 모든 설정값은 상단에 정의
- **async/await** 사용 - 콜백 대신 Promise 사용
- **에러 처리** 필수 - try/catch로 모든 API 호출 감싸기

### 설정 패턴
```javascript
const CONFIG = {
  API: {
    BASE_URL: 'https://api.example.com',
    TIMEOUT: 10000,
    RETRY_COUNT: 3
  },
  UI: {
    DEBOUNCE_DELAY: 300,
    TOAST_DURATION: 3000
  }
};
```

### API 호출 패턴
```javascript
async function fetchWithRetry(url, options = {}, retries = 3) {
  // templates/js/utils.js 참조
}
```

---

## Python 백엔드 표준

### 필수 규칙
- **FastAPI 사용** - Flask 대신 FastAPI 우선
- **타입 힌트** 필수 - 모든 함수에 타입 명시
- **pydantic-settings** - 환경 변수 관리

### 프로젝트 구조
```
src/
├── main.py         # FastAPI 앱 진입점
├── config.py       # 설정 (pydantic-settings)
├── api/
│   ├── routes.py   # API 라우트
│   └── schemas.py  # Pydantic 스키마
├── services/       # 비즈니스 로직
└── utils/          # 유틸리티
```

### FastAPI 앱 패턴
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="앱 이름", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## Git 커밋 규칙

### 커밋 메시지 형식
```
<타입>: <제목> (한국어)

<본문> (선택사항)

Co-Authored-By: Claude <noreply@anthropic.com>
```

### 타입
- `feat`: 새 기능
- `fix`: 버그 수정
- `docs`: 문서 변경
- `style`: 코드 포맷팅
- `refactor`: 리팩토링
- `test`: 테스트 추가
- `chore`: 기타 변경

---

## 파일 네이밍

| 종류 | 규칙 | 예시 |
|------|------|------|
| HTML | kebab-case | `user-profile.html` |
| CSS | kebab-case | `variables.css` |
| JS | camelCase | `userProfile.js` |
| Python | snake_case | `user_profile.py` |
| 컴포넌트 | PascalCase | `UserProfile.js` |

---

## 프로젝트 시작 체크리스트

새 프로젝트 시작 시:
- [ ] README.md 생성
- [ ] .gitignore 설정
- [ ] CLAUDE.md 복사 (프로젝트 특화 내용 추가)
- [ ] CSS 변수 파일 복사 (`templates/css/variables.css`)
- [ ] config 파일 생성 (JS 또는 Python)
- [ ] .env.example 생성

---

## 참고 링크

- 전체 표준 문서: `CODING_STANDARDS.md`
- 템플릿 파일: `templates/` 디렉토리
- 코드 스니펫: `snippets/` 디렉토리
