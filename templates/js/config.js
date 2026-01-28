/**
 * 애플리케이션 설정
 * 모든 설정값을 한 곳에서 관리
 *
 * 사용법:
 *   1. 이 파일을 프로젝트에 복사
 *   2. 프로젝트에 맞게 값 수정
 *   3. 다른 JS 파일보다 먼저 로드
 */

const CONFIG = {
  // ==================== API 설정 ====================
  API: {
    // 기본 URL (프로덕션)
    BASE_URL: 'https://api.example.com',

    // 타임아웃 (밀리초)
    TIMEOUT: 10000,

    // 재시도 설정
    RETRY_COUNT: 3,
    RETRY_DELAY: 1000,

    // 엔드포인트 (선택사항)
    ENDPOINTS: {
      USERS: '/users',
      ITEMS: '/items',
      AUTH: '/auth'
    }
  },

  // ==================== UI 설정 ====================
  UI: {
    // 디바운스 딜레이 (검색 입력 등)
    DEBOUNCE_DELAY: 300,

    // 토스트 메시지 표시 시간
    TOAST_DURATION: 3000,

    // 애니메이션 시간
    ANIMATION_DURATION: 250,

    // 페이지당 아이템 수
    ITEMS_PER_PAGE: 10,

    // 모달 z-index
    MODAL_Z_INDEX: 1050
  },

  // ==================== 저장소 키 ====================
  STORAGE: {
    // 로컬 스토리지 키
    USER_PREFS: 'app_user_preferences',
    AUTH_TOKEN: 'app_auth_token',
    CACHE_PREFIX: 'app_cache_',

    // 캐시 만료 시간 (밀리초)
    CACHE_EXPIRY: 5 * 60 * 1000  // 5분
  },

  // ==================== 기능 플래그 ====================
  FEATURES: {
    // 다크 모드 지원
    DARK_MODE: true,

    // 디버그 모드
    DEBUG: false,

    // 애널리틱스
    ANALYTICS: false,

    // 오프라인 모드
    OFFLINE_MODE: false
  },

  // ==================== 검증 규칙 ====================
  VALIDATION: {
    // 이메일 정규식
    EMAIL_REGEX: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,

    // 비밀번호 최소 길이
    MIN_PASSWORD_LENGTH: 8,

    // 사용자명 길이
    MIN_USERNAME_LENGTH: 3,
    MAX_USERNAME_LENGTH: 20
  },

  // ==================== 메시지 ====================
  MESSAGES: {
    // 에러 메시지
    ERROR: {
      NETWORK: '네트워크 오류가 발생했습니다. 다시 시도해주세요.',
      TIMEOUT: '요청 시간이 초과되었습니다.',
      UNAUTHORIZED: '로그인이 필요합니다.',
      NOT_FOUND: '요청한 정보를 찾을 수 없습니다.',
      SERVER: '서버 오류가 발생했습니다.',
      VALIDATION: '입력값을 확인해주세요.'
    },

    // 성공 메시지
    SUCCESS: {
      SAVE: '저장되었습니다.',
      DELETE: '삭제되었습니다.',
      UPDATE: '수정되었습니다.'
    },

    // 확인 메시지
    CONFIRM: {
      DELETE: '정말 삭제하시겠습니까?',
      UNSAVED: '저장하지 않은 변경사항이 있습니다. 정말 나가시겠습니까?'
    }
  }
};

// ==================== 환경별 오버라이드 ====================

// 개발 환경 (localhost)
if (location.hostname === 'localhost' || location.hostname === '127.0.0.1') {
  CONFIG.API.BASE_URL = 'http://localhost:8080';
  CONFIG.FEATURES.DEBUG = true;
  console.log('🔧 개발 모드 활성화');
}

// 스테이징 환경
if (location.hostname.includes('staging')) {
  CONFIG.API.BASE_URL = 'https://staging-api.example.com';
}

// 설정 객체 불변으로 만들기 (실수로 수정 방지)
Object.freeze(CONFIG);
Object.freeze(CONFIG.API);
Object.freeze(CONFIG.UI);
Object.freeze(CONFIG.STORAGE);
Object.freeze(CONFIG.FEATURES);
Object.freeze(CONFIG.VALIDATION);
Object.freeze(CONFIG.MESSAGES);

// 디버그 모드일 때 설정 출력
if (CONFIG.FEATURES.DEBUG) {
  console.log('📋 현재 설정:', CONFIG);
}
