"""
애플리케이션 설정 관리
pydantic-settings v2 사용 (최신 패턴)

설치: pip install pydantic-settings
"""
from functools import lru_cache
from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    애플리케이션 설정

    환경 변수 또는 .env 파일에서 값을 자동으로 읽음
    """

    # ==================== 기본 설정 ====================
    APP_NAME: str = "MyApp"
    VERSION: str = "1.0.0"
    DEBUG: bool = False

    # ==================== 서버 설정 ====================
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # ==================== CORS ====================
    CORS_ORIGINS: List[str] = ["*"]

    # ==================== API 키 (민감정보) ====================
    # 주의: 반드시 환경 변수로 설정, 코드에 하드코딩 금지
    GEMINI_API_KEY: str = ""
    SECRET_KEY: str = ""  # 배포 전 필수 변경

    # ==================== 데이터베이스 ====================
    DATABASE_URL: str = "sqlite:///./data.db"

    # ChromaDB (RAG 프로젝트용)
    CHROMA_DB_PATH: str = "./data/vector_db"

    # ==================== 로깅 ====================
    LOG_LEVEL: str = "INFO"

    # ==================== 기타 ====================
    MAX_ITEMS_PER_PAGE: int = 50
    CACHE_TTL: int = 300  # 초

    # Pydantic v2 설정 (model_config 사용)
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",  # 알 수 없는 환경 변수 무시
    )


@lru_cache
def get_settings() -> Settings:
    """
    설정 인스턴스 반환 (캐시됨)

    사용법:
        from src.config import settings
        print(settings.APP_NAME)

        # 또는 의존성 주입
        from src.config import get_settings
        settings = get_settings()
    """
    return Settings()


# 글로벌 설정 인스턴스
settings = get_settings()


# ==================== 설정 검증 ====================

def validate_settings() -> None:
    """
    필수 설정 검증
    앱 시작 시 호출 권장
    """
    errors = []

    if not settings.SECRET_KEY:
        errors.append("SECRET_KEY가 설정되지 않았습니다")

    if settings.SECRET_KEY == "change-me-in-production":
        errors.append("SECRET_KEY를 기본값에서 변경해주세요")

    if errors:
        raise ValueError(f"설정 오류: {', '.join(errors)}")


# ==================== 사용 예시 ====================

if __name__ == "__main__":
    print(f"앱 이름: {settings.APP_NAME}")
    print(f"버전: {settings.VERSION}")
    print(f"디버그 모드: {settings.DEBUG}")
    print(f"서버: {settings.HOST}:{settings.PORT}")
    print(f"CORS: {settings.CORS_ORIGINS}")
    print(f"DB: {settings.DATABASE_URL}")
