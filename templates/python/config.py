"""
애플리케이션 설정 관리
pydantic-settings 사용

설치: pip install pydantic-settings
"""
from functools import lru_cache
from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    애플리케이션 설정

    환경 변수 또는 .env 파일에서 값을 읽음
    """

    # ==================== 기본 설정 ====================
    APP_NAME: str = "MyApp"
    VERSION: str = "1.0.0"
    DEBUG: bool = False

    # ==================== 서버 설정 ====================
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # ==================== CORS ====================
    # 콤마로 구분된 문자열 또는 리스트
    CORS_ORIGINS: List[str] = ["*"]

    # ==================== API 키 ====================
    # 민감한 정보는 환경 변수로 관리
    GEMINI_API_KEY: str = ""
    SECRET_KEY: str = "change-me-in-production"

    # ==================== 데이터베이스 ====================
    DATABASE_URL: str = "sqlite:///./data.db"

    # ChromaDB (RAG 프로젝트용)
    CHROMA_DB_PATH: str = "./data/vector_db"

    # ==================== 로깅 ====================
    LOG_LEVEL: str = "INFO"

    # ==================== 기타 ====================
    # 프로젝트별 설정 추가
    MAX_ITEMS_PER_PAGE: int = 50
    CACHE_TTL: int = 300  # 초

    class Config:
        """Pydantic 설정"""
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

        # 환경 변수 접두사 (선택사항)
        # env_prefix = "APP_"


@lru_cache()
def get_settings() -> Settings:
    """
    설정 인스턴스 반환 (캐시됨)

    사용법:
        from config import settings
        print(settings.APP_NAME)

        # 또는 의존성 주입
        from config import get_settings
        settings = get_settings()
    """
    return Settings()


# 글로벌 설정 인스턴스
settings = get_settings()


# ==================== 사용 예시 ====================

if __name__ == "__main__":
    # 설정 확인
    print(f"앱 이름: {settings.APP_NAME}")
    print(f"버전: {settings.VERSION}")
    print(f"디버그 모드: {settings.DEBUG}")
    print(f"서버: {settings.HOST}:{settings.PORT}")
    print(f"CORS: {settings.CORS_ORIGINS}")
    print(f"DB: {settings.DATABASE_URL}")
