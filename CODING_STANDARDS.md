# 프로젝트 코딩 표준 가이드라인

> 16개 GitHub 프로젝트 분석 결과 기반 일관성 있는 개발 표준

**작성일**: 2026-01-27
**적용 대상**: 모든 신규 및 기존 프로젝트

---

## 1. 현재 프로젝트 분석 결과

### 1.1 기술 스택 분포

| 프로젝트 | 프론트엔드 | 백엔드 | CSS | DB |
|---------|-----------|--------|-----|-----|
| chatbot-gyomu | HTML/JS | Apps Script | 인라인 | Google Sheets |
| RAG | - | FastAPI | - | ChromaDB |
| Faculty-status | HTML | Express | CSS 파일 | MongoDB |
| Law-Tracking | HTML | Flask | CSS 파일 | MongoDB |
| faculty-review | HTML/JS | - | CSS 파일 | - |
| Status-of-professors | HTML/JS | Flask | CSS 파일 | JSON |
| Placement-chart | HTML/JS | - | CSS 파일 | LocalStorage |
| document-review | HTML/JS | Chrome API | CSS 파일 | Chrome Storage |
| document-review-rag | - | Python | - | - |
| API-Test | HTML | Node.js | CSS 파일 | - |
| MarkDown | - | - | - | JSON |
| University-Accreditation | - | Python | - | - |
| retirement-system | HTML | - | **인라인** | - |
| Severance-pay | HTML | - | **인라인** | - |
| work-planner | HTML | - | **인라인** | - |
| yiu-attendance | HTML | - | **인라인** | - |

### 1.2 발견된 문제점

#### CSS 스타일링 불일치
```
❌ 인라인 스타일: 4개 프로젝트 (retirement-system, Severance-pay, work-planner, yiu-attendance)
❌ CSS 파일 분리: 8개 프로젝트
❌ CSS 변수 사용: 일부만
❌ 반응형 디자인: 일관성 없음
```

#### 프론트엔드 불일치
```
❌ 모두 바닐라 JS (프레임워크 없음)
❌ 모듈 시스템 미사용
❌ 빌드 도구 미사용
❌ 컴포넌트 재사용 없음
```

#### 백엔드 불일치
```
❌ Python: Flask vs FastAPI 혼재
❌ JavaScript: Express vs 순수 Node.js 혼재
❌ Google Apps Script: 별도 패턴
```

#### 배포 불일치
```
❌ GitHub Pages, Render, Cloud Run, Vercel, Netlify 혼재
❌ 환경 변수 관리 방식 불일치
```

---

## 2. 권장 기술 스택 (2026 기준)

### 2.1 프로젝트 유형별 권장 스택

#### Type A: 간단한 계산기/도구 (Single Page)
```
프론트엔드: HTML5 + CSS3 + 바닐라 JS
CSS 프레임워크: Bootstrap 5.3 또는 Pico CSS
배포: GitHub Pages
예시: retirement-system, Severance-pay, work-planner, yiu-attendance
```

#### Type B: 대시보드/관리 시스템 (Multi Page)
```
프론트엔드: HTML5 + CSS3 + 바닐라 JS (또는 Alpine.js)
CSS 프레임워크: Bootstrap 5.3 + CSS 변수
백엔드: Python FastAPI 또는 Flask
DB: SQLite (로컬) 또는 MongoDB Atlas (클라우드)
배포: GitHub Pages (프론트) + Render (백엔드)
예시: faculty-review, Status-of-professors, Placement-chart
```

#### Type C: AI/RAG 시스템
```
프론트엔드: HTML5 + 바닐라 JS
백엔드: Python FastAPI
벡터 DB: ChromaDB (로컬) 또는 Pinecone (클라우드)
AI: Google Gemini API
배포: Cloud Run + Cloudflare Tunnel (개발용)
예시: RAG, chatbot-gyomu, document-review-rag
```

#### Type D: Chrome Extension
```
프론트엔드: HTML5 + CSS3 + 바닐라 JS
Manifest: V3
저장소: Chrome Storage API
배포: Chrome Web Store
예시: document-review
```

---

## 3. CSS 표준

### 3.1 파일 구조
```
프로젝트/
├── css/
│   ├── variables.css    # CSS 커스텀 프로퍼티
│   ├── base.css         # 리셋 및 기본 스타일
│   ├── components.css   # 버튼, 카드, 폼 등
│   ├── layout.css       # 그리드, 컨테이너
│   └── utilities.css    # 유틸리티 클래스
└── index.html
```

### 3.2 CSS 변수 표준 (variables.css)
```css
:root {
  /* 색상 팔레트 - 용인대 브랜딩 */
  --color-primary: #667eea;
  --color-primary-dark: #5a67d8;
  --color-secondary: #764ba2;
  --color-success: #10b981;
  --color-warning: #f59e0b;
  --color-danger: #ef4444;
  --color-info: #3b82f6;

  /* 그레이 스케일 */
  --color-gray-50: #f9fafb;
  --color-gray-100: #f3f4f6;
  --color-gray-200: #e5e7eb;
  --color-gray-300: #d1d5db;
  --color-gray-400: #9ca3af;
  --color-gray-500: #6b7280;
  --color-gray-600: #4b5563;
  --color-gray-700: #374151;
  --color-gray-800: #1f2937;
  --color-gray-900: #111827;

  /* 타이포그래피 */
  --font-family-sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
                      'Noto Sans KR', sans-serif;
  --font-family-mono: 'Consolas', 'Monaco', monospace;

  --font-size-xs: 0.75rem;   /* 12px */
  --font-size-sm: 0.875rem;  /* 14px */
  --font-size-base: 1rem;    /* 16px */
  --font-size-lg: 1.125rem;  /* 18px */
  --font-size-xl: 1.25rem;   /* 20px */
  --font-size-2xl: 1.5rem;   /* 24px */

  /* 간격 */
  --spacing-1: 0.25rem;  /* 4px */
  --spacing-2: 0.5rem;   /* 8px */
  --spacing-3: 0.75rem;  /* 12px */
  --spacing-4: 1rem;     /* 16px */
  --spacing-5: 1.25rem;  /* 20px */
  --spacing-6: 1.5rem;   /* 24px */
  --spacing-8: 2rem;     /* 32px */

  /* 테두리 반경 */
  --radius-sm: 0.25rem;
  --radius-md: 0.5rem;
  --radius-lg: 0.75rem;
  --radius-xl: 1rem;
  --radius-full: 9999px;

  /* 그림자 */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
  --shadow-xl: 0 20px 25px rgba(0, 0, 0, 0.15);

  /* 트랜지션 */
  --transition-fast: 150ms ease;
  --transition-normal: 250ms ease;
  --transition-slow: 350ms ease;
}

/* 다크 모드 지원 (선택사항) */
@media (prefers-color-scheme: dark) {
  :root {
    --color-gray-50: #111827;
    --color-gray-100: #1f2937;
    /* ... */
  }
}
```

### 3.3 기본 스타일 (base.css)
```css
/* CSS 리셋 */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  font-size: 16px;
  scroll-behavior: smooth;
}

body {
  font-family: var(--font-family-sans);
  font-size: var(--font-size-base);
  line-height: 1.6;
  color: var(--color-gray-800);
  background-color: var(--color-gray-50);
  -webkit-font-smoothing: antialiased;
}

/* 링크 기본 스타일 */
a {
  color: var(--color-primary);
  text-decoration: none;
  transition: color var(--transition-fast);
}

a:hover {
  color: var(--color-primary-dark);
}

/* 버튼 기본 스타일 */
button {
  cursor: pointer;
  font-family: inherit;
  font-size: inherit;
  border: none;
  background: none;
}

/* 이미지 반응형 */
img {
  max-width: 100%;
  height: auto;
  display: block;
}

/* 테이블 기본 */
table {
  border-collapse: collapse;
  width: 100%;
}
```

### 3.4 버튼 컴포넌트 (components.css 일부)
```css
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--spacing-2);
  padding: var(--spacing-2) var(--spacing-4);
  font-size: var(--font-size-sm);
  font-weight: 500;
  border-radius: var(--radius-md);
  transition: all var(--transition-fast);
  cursor: pointer;
  border: 1px solid transparent;
}

.btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.btn-primary {
  background: var(--color-primary);
  color: white;
}

.btn-primary:hover:not(:disabled) {
  background: var(--color-primary-dark);
  transform: translateY(-1px);
  box-shadow: var(--shadow-md);
}

.btn-secondary {
  background: var(--color-gray-100);
  color: var(--color-gray-700);
  border-color: var(--color-gray-300);
}

.btn-secondary:hover:not(:disabled) {
  background: var(--color-gray-200);
}

.btn-success { background: var(--color-success); color: white; }
.btn-danger { background: var(--color-danger); color: white; }

/* 크기 변형 */
.btn-sm { padding: var(--spacing-1) var(--spacing-2); font-size: var(--font-size-xs); }
.btn-lg { padding: var(--spacing-3) var(--spacing-6); font-size: var(--font-size-lg); }
```

---

## 4. JavaScript 표준

### 4.1 파일 구조
```
프로젝트/
├── js/
│   ├── config.js        # 설정 상수
│   ├── utils.js         # 유틸리티 함수
│   ├── api.js           # API 호출
│   ├── components/      # UI 컴포넌트
│   │   ├── modal.js
│   │   └── toast.js
│   └── main.js          # 진입점
└── index.html
```

### 4.2 설정 파일 표준 (config.js)
```javascript
// config.js - 모든 설정을 한 곳에서 관리
const CONFIG = {
  // API 엔드포인트
  API: {
    BASE_URL: 'https://api.example.com',
    TIMEOUT: 10000,
    RETRY_COUNT: 3,
    RETRY_DELAY: 1000
  },

  // UI 설정
  UI: {
    DEBOUNCE_DELAY: 300,
    TOAST_DURATION: 3000,
    ANIMATION_DURATION: 250
  },

  // 저장소 키
  STORAGE: {
    USER_PREFS: 'app_user_prefs',
    CACHE_PREFIX: 'app_cache_'
  },

  // 기능 플래그
  FEATURES: {
    DARK_MODE: true,
    DEBUG: false
  }
};

// 환경별 설정 오버라이드
if (location.hostname === 'localhost') {
  CONFIG.API.BASE_URL = 'http://localhost:8080';
  CONFIG.FEATURES.DEBUG = true;
}

Object.freeze(CONFIG);
```

### 4.3 유틸리티 함수 표준 (utils.js)
```javascript
// utils.js - 공통 유틸리티 함수

/**
 * HTML 이스케이프
 * @param {string} text - 이스케이프할 텍스트
 * @returns {string} 이스케이프된 텍스트
 */
function escapeHtml(text) {
  const div = document.createElement('div');
  div.textContent = text;
  return div.innerHTML;
}

/**
 * 디바운스 함수
 * @param {Function} func - 실행할 함수
 * @param {number} wait - 대기 시간 (ms)
 * @returns {Function} 디바운스된 함수
 */
function debounce(func, wait = CONFIG.UI.DEBOUNCE_DELAY) {
  let timeout;
  return function executedFunction(...args) {
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(this, args), wait);
  };
}

/**
 * 날짜 포맷팅
 * @param {Date|string} date - 날짜
 * @param {string} format - 포맷 ('short' | 'long' | 'time')
 * @returns {string} 포맷된 날짜 문자열
 */
function formatDate(date, format = 'short') {
  const d = new Date(date);
  const options = {
    short: { year: 'numeric', month: '2-digit', day: '2-digit' },
    long: { year: 'numeric', month: 'long', day: 'numeric', weekday: 'long' },
    time: { hour: '2-digit', minute: '2-digit' }
  };
  return d.toLocaleDateString('ko-KR', options[format]);
}

/**
 * 숫자 포맷팅 (천 단위 콤마)
 * @param {number} num - 숫자
 * @returns {string} 포맷된 문자열
 */
function formatNumber(num) {
  return new Intl.NumberFormat('ko-KR').format(num);
}

/**
 * 로컬 스토리지 헬퍼
 */
const Storage = {
  get(key, defaultValue = null) {
    try {
      const item = localStorage.getItem(key);
      return item ? JSON.parse(item) : defaultValue;
    } catch {
      return defaultValue;
    }
  },

  set(key, value) {
    try {
      localStorage.setItem(key, JSON.stringify(value));
      return true;
    } catch {
      return false;
    }
  },

  remove(key) {
    localStorage.removeItem(key);
  }
};
```

### 4.4 API 호출 표준 (api.js)
```javascript
// api.js - API 호출 래퍼

/**
 * 재시도 로직이 포함된 fetch 래퍼
 */
async function fetchWithRetry(url, options = {}, retries = CONFIG.API.RETRY_COUNT) {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), CONFIG.API.TIMEOUT);

  try {
    const response = await fetch(url, {
      ...options,
      signal: controller.signal,
      headers: {
        'Content-Type': 'application/json',
        ...options.headers
      }
    });

    clearTimeout(timeoutId);

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    return await response.json();

  } catch (error) {
    clearTimeout(timeoutId);

    if (retries > 0 && !error.name.includes('Abort')) {
      console.warn(`Retrying... (${CONFIG.API.RETRY_COUNT - retries + 1})`);
      await new Promise(r => setTimeout(r, CONFIG.API.RETRY_DELAY));
      return fetchWithRetry(url, options, retries - 1);
    }

    throw error;
  }
}

/**
 * API 클라이언트
 */
const API = {
  async get(endpoint) {
    return fetchWithRetry(`${CONFIG.API.BASE_URL}${endpoint}`);
  },

  async post(endpoint, data) {
    return fetchWithRetry(`${CONFIG.API.BASE_URL}${endpoint}`, {
      method: 'POST',
      body: JSON.stringify(data)
    });
  },

  async put(endpoint, data) {
    return fetchWithRetry(`${CONFIG.API.BASE_URL}${endpoint}`, {
      method: 'PUT',
      body: JSON.stringify(data)
    });
  },

  async delete(endpoint) {
    return fetchWithRetry(`${CONFIG.API.BASE_URL}${endpoint}`, {
      method: 'DELETE'
    });
  }
};
```

---

## 5. Python 백엔드 표준

### 5.1 프로젝트 구조
```
프로젝트/
├── src/
│   ├── __init__.py
│   ├── main.py          # FastAPI 앱
│   ├── config.py        # 설정
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py    # API 라우트
│   │   └── schemas.py   # Pydantic 스키마
│   ├── services/
│   │   └── *.py         # 비즈니스 로직
│   └── utils/
│       └── *.py         # 유틸리티
├── tests/
├── requirements.txt
├── requirements-dev.txt
├── .env.example
├── Dockerfile
└── README.md
```

### 5.2 FastAPI 템플릿 (main.py)
```python
"""
FastAPI 애플리케이션 진입점
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from src.config import settings
from src.api.routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """앱 시작/종료 이벤트"""
    # 시작 시 실행
    print(f"Starting {settings.APP_NAME}...")
    yield
    # 종료 시 실행
    print("Shutting down...")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    lifespan=lifespan
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(router, prefix="/api/v1")


@app.get("/health")
async def health_check():
    """상태 확인 엔드포인트"""
    return {
        "status": "healthy",
        "version": settings.VERSION
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "src.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )
```

### 5.3 설정 관리 (config.py)
```python
"""
설정 관리 - pydantic-settings 사용
"""
from pydantic_settings import BaseSettings
from typing import List
from functools import lru_cache


class Settings(BaseSettings):
    """애플리케이션 설정"""

    # 기본 설정
    APP_NAME: str = "MyApp"
    VERSION: str = "1.0.0"
    DEBUG: bool = False

    # 서버 설정
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # CORS
    CORS_ORIGINS: List[str] = ["*"]

    # API 키
    GEMINI_API_KEY: str = ""

    # 데이터베이스
    DATABASE_URL: str = "sqlite:///./data.db"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    """설정 인스턴스 (캐시됨)"""
    return Settings()


settings = get_settings()
```

### 5.4 requirements.txt 템플릿
```
# Core
fastapi>=0.109.0
uvicorn[standard]>=0.27.0
pydantic>=2.5.0
pydantic-settings>=2.1.0

# Database (선택)
# sqlalchemy>=2.0.0
# chromadb>=0.4.22

# Google APIs (선택)
# google-generativeai>=0.3.2
# google-api-python-client>=2.108.0

# Utilities
python-dotenv>=1.0.0
httpx>=0.26.0

# Development
# pytest>=7.4.0
# black>=23.0.0
# ruff>=0.1.0
```

---

## 6. 배포 표준

### 6.1 GitHub Pages (프론트엔드)
```yaml
# .github/workflows/deploy.yml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./
```

### 6.2 Render (백엔드)
```yaml
# render.yaml
services:
  - type: web
    name: my-api
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn src.main:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: GEMINI_API_KEY
        sync: false
```

### 6.3 Docker 표준
```dockerfile
# Dockerfile
FROM python:3.12-slim

WORKDIR /app

# 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스 복사
COPY src/ ./src/

# 포트 노출
EXPOSE 8000

# 실행
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 7. 프로젝트 체크리스트

### 신규 프로젝트 시작 시
- [ ] README.md 작성
- [ ] .gitignore 설정
- [ ] CSS 변수 파일 생성 (variables.css)
- [ ] config.js 또는 config.py 생성
- [ ] .env.example 생성
- [ ] 폴더 구조 정리

### 기존 프로젝트 리팩토링 시
- [ ] 인라인 CSS → 분리된 CSS 파일
- [ ] CSS 변수 적용
- [ ] JavaScript 모듈화
- [ ] API 호출 표준화
- [ ] 에러 처리 추가
- [ ] 반응형 디자인 확인

---

## 8. 마이그레이션 우선순위

### 높음 (즉시 적용)
1. **retirement-system** - 인라인 CSS → CSS 파일 분리
2. **Severance-pay** - 인라인 CSS → CSS 파일 분리
3. **work-planner** - 인라인 CSS → CSS 파일 분리
4. **yiu-attendance** - 인라인 CSS → CSS 파일 분리

### 중간 (1개월 내)
5. **chatbot-gyomu** - CSS 변수 통일, JS 모듈화
6. **Law-Tracking** - Flask → FastAPI 마이그레이션 검토
7. **Status-of-professors** - CSS 정리

### 낮음 (3개월 내)
8. **faculty-review** - 전체 리팩토링
9. **Faculty-status** - 백엔드 현대화

---

## 9. 참고 자료

- [MDN Web Docs](https://developer.mozilla.org/ko/)
- [FastAPI 공식 문서](https://fastapi.tiangolo.com/)
- [CSS Custom Properties](https://developer.mozilla.org/ko/docs/Web/CSS/--*)
- [Google Gemini API](https://ai.google.dev/docs)

---

**문서 버전**: 1.0
**최종 수정**: 2026-01-27
