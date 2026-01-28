"""
FastAPI 애플리케이션 템플릿
"""
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    """앱 시작/종료 이벤트 핸들러"""
    # ===== 시작 시 실행 =====
    print(f"🚀 {settings.APP_NAME} v{settings.VERSION} 시작...")

    # 데이터베이스 연결, 캐시 초기화 등
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
    docs_url="/docs" if settings.DEBUG else None,  # 프로덕션에서 문서 비활성화
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


# ==================== 상태 확인 엔드포인트 ====================

@app.get("/health")
async def health_check():
    """서버 상태 확인"""
    return {
        "status": "healthy",
        "app": settings.APP_NAME,
        "version": settings.VERSION,
        "debug": settings.DEBUG
    }


@app.get("/")
async def root():
    """루트 엔드포인트"""
    return {
        "message": f"{settings.APP_NAME}에 오신 것을 환영합니다!",
        "docs": "/docs" if settings.DEBUG else "비활성화됨"
    }


# ==================== API 라우트 (예시) ====================

@app.get("/api/v1/items")
async def get_items():
    """아이템 목록 조회"""
    # TODO: 실제 로직 구현
    return {
        "items": [
            {"id": 1, "name": "아이템 1"},
            {"id": 2, "name": "아이템 2"},
        ],
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
    # TODO: Pydantic 스키마로 검증
    return {
        "id": 999,
        "message": "생성되었습니다",
        **data
    }


# ==================== 에러 핸들러 ====================

@app.exception_handler(404)
async def not_found_handler(request, exc):
    return {
        "error": "Not Found",
        "message": "요청한 리소스를 찾을 수 없습니다",
        "path": str(request.url)
    }


@app.exception_handler(500)
async def server_error_handler(request, exc):
    return {
        "error": "Internal Server Error",
        "message": "서버 오류가 발생했습니다"
    }


# ==================== 직접 실행 ====================

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG  # 개발 모드에서 자동 리로드
    )
