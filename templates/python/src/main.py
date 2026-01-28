"""
FastAPI 애플리케이션 진입점

실행 방법:
    uvicorn src.main:app --reload
"""
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.config import settings, validate_settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    """앱 시작/종료 이벤트 핸들러"""
    # ===== 시작 시 실행 =====
    print(f"🚀 {settings.APP_NAME} v{settings.VERSION} 시작...")

    # 설정 검증 (프로덕션에서 필수)
    if not settings.DEBUG:
        try:
            validate_settings()
        except ValueError as e:
            print(f"⚠️ 설정 경고: {e}")

    # 데이터베이스 연결 등 초기화
    # await database.connect()

    yield

    # ===== 종료 시 실행 =====
    print("👋 서버 종료 중...")

    # 리소스 정리
    # await database.disconnect()


# ==================== FastAPI 앱 생성 ====================

app = FastAPI(
    title=settings.APP_NAME,
    description="API 설명을 여기에 작성",
    version=settings.VERSION,
    lifespan=lifespan,
    docs_url="/docs" if settings.DEBUG else None,
    redoc_url="/redoc" if settings.DEBUG else None,
)


# ==================== 미들웨어 ====================

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==================== 예외 핸들러 ====================

@app.exception_handler(404)
async def not_found_handler(request: Request, exc: HTTPException) -> JSONResponse:
    """404 에러 핸들러"""
    return JSONResponse(
        status_code=404,
        content={
            "error": "Not Found",
            "message": "요청한 리소스를 찾을 수 없습니다",
            "path": str(request.url.path)
        }
    )


@app.exception_handler(500)
async def server_error_handler(request: Request, exc: Exception) -> JSONResponse:
    """500 에러 핸들러"""
    # 프로덕션에서는 상세 에러 숨김
    detail = str(exc) if settings.DEBUG else "서버 오류가 발생했습니다"

    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "message": detail
        }
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    """일반 HTTP 예외 핸들러"""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "status_code": exc.status_code
        }
    )


# ==================== 운영 엔드포인트 ====================

@app.get("/health")
async def health_check():
    """
    서버 상태 확인

    로드밸런서/k8s 헬스체크용
    """
    return {
        "status": "healthy",
        "app": settings.APP_NAME,
        "version": settings.VERSION
    }


@app.get("/")
async def root():
    """루트 엔드포인트"""
    return {
        "message": f"{settings.APP_NAME}에 오신 것을 환영합니다!",
        "version": settings.VERSION,
        "docs": "/docs" if settings.DEBUG else "비활성화됨"
    }


# ==================== API 라우트 (예시) ====================
# 실제 프로젝트에서는 src/api/routes.py로 분리 권장

@app.get("/api/v1/items")
async def get_items(page: int = 1, limit: int = 10):
    """아이템 목록 조회"""
    # 페이지네이션 제한
    limit = min(limit, settings.MAX_ITEMS_PER_PAGE)

    # TODO: 실제 로직 구현
    return {
        "items": [
            {"id": 1, "name": "아이템 1"},
            {"id": 2, "name": "아이템 2"},
        ],
        "page": page,
        "limit": limit,
        "total": 2
    }


@app.get("/api/v1/items/{item_id}")
async def get_item(item_id: int):
    """아이템 상세 조회"""
    if item_id <= 0:
        raise HTTPException(status_code=400, detail="유효하지 않은 ID입니다")

    # TODO: 실제 로직 구현
    return {
        "id": item_id,
        "name": f"아이템 {item_id}",
        "description": "설명"
    }


@app.post("/api/v1/items")
async def create_item(data: dict):
    """아이템 생성"""
    # TODO: Pydantic 스키마로 검증 (src/api/schemas.py)
    return {
        "id": 999,
        "message": "생성되었습니다",
        **data
    }


# ==================== 직접 실행 ====================

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "src.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG
    )
