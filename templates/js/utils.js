/**
 * 공통 유틸리티 함수
 * config.js 다음에 로드
 */

// ==================== DOM 유틸리티 ====================

/**
 * DOM 요소 선택 (단일)
 * @param {string} selector - CSS 선택자
 * @param {Element} parent - 부모 요소 (기본: document)
 * @returns {Element|null}
 */
function $(selector, parent = document) {
  return parent.querySelector(selector);
}

/**
 * DOM 요소 선택 (복수)
 * @param {string} selector - CSS 선택자
 * @param {Element} parent - 부모 요소 (기본: document)
 * @returns {Element[]}
 */
function $$(selector, parent = document) {
  return [...parent.querySelectorAll(selector)];
}

/**
 * HTML 이스케이프 (XSS 방지)
 * @param {string} text - 이스케이프할 텍스트
 * @returns {string}
 */
function escapeHtml(text) {
  const div = document.createElement('div');
  div.textContent = text;
  return div.innerHTML;
}

/**
 * 요소 표시/숨김 토글
 * @param {Element} element - 대상 요소
 * @param {boolean} show - 표시 여부 (생략 시 토글)
 */
function toggleVisibility(element, show) {
  if (show === undefined) {
    element.classList.toggle('hidden');
  } else {
    element.classList.toggle('hidden', !show);
  }
}

// ==================== 함수 유틸리티 ====================

/**
 * 디바운스
 * @param {Function} func - 실행할 함수
 * @param {number} wait - 대기 시간 (ms)
 * @returns {Function}
 */
function debounce(func, wait = CONFIG?.UI?.DEBOUNCE_DELAY || 300) {
  let timeout;
  return function executedFunction(...args) {
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(this, args), wait);
  };
}

/**
 * 쓰로틀
 * @param {Function} func - 실행할 함수
 * @param {number} limit - 최소 간격 (ms)
 * @returns {Function}
 */
function throttle(func, limit = 100) {
  let inThrottle;
  return function executedFunction(...args) {
    if (!inThrottle) {
      func.apply(this, args);
      inThrottle = true;
      setTimeout(() => inThrottle = false, limit);
    }
  };
}

// ==================== 포맷팅 유틸리티 ====================

/**
 * 날짜 포맷팅
 * @param {Date|string|number} date - 날짜
 * @param {string} format - 포맷 ('short' | 'long' | 'time' | 'datetime')
 * @returns {string}
 */
function formatDate(date, format = 'short') {
  const d = new Date(date);

  if (isNaN(d.getTime())) {
    return '-';
  }

  const options = {
    short: { year: 'numeric', month: '2-digit', day: '2-digit' },
    long: { year: 'numeric', month: 'long', day: 'numeric', weekday: 'long' },
    time: { hour: '2-digit', minute: '2-digit' },
    datetime: { year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit' }
  };

  return d.toLocaleDateString('ko-KR', options[format] || options.short);
}

/**
 * 숫자 포맷팅 (천 단위 콤마)
 * @param {number} num - 숫자
 * @returns {string}
 */
function formatNumber(num) {
  if (num === null || num === undefined) return '-';
  return new Intl.NumberFormat('ko-KR').format(num);
}

/**
 * 통화 포맷팅
 * @param {number} amount - 금액
 * @param {string} currency - 통화 코드 (기본: KRW)
 * @returns {string}
 */
function formatCurrency(amount, currency = 'KRW') {
  if (amount === null || amount === undefined) return '-';
  return new Intl.NumberFormat('ko-KR', {
    style: 'currency',
    currency: currency
  }).format(amount);
}

/**
 * 파일 크기 포맷팅
 * @param {number} bytes - 바이트
 * @returns {string}
 */
function formatFileSize(bytes) {
  if (bytes === 0) return '0 B';
  const k = 1024;
  const sizes = ['B', 'KB', 'MB', 'GB', 'TB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}

// ==================== 저장소 유틸리티 ====================

const Storage = {
  /**
   * 값 가져오기
   * @param {string} key - 키
   * @param {*} defaultValue - 기본값
   * @returns {*}
   */
  get(key, defaultValue = null) {
    try {
      const item = localStorage.getItem(key);
      return item ? JSON.parse(item) : defaultValue;
    } catch {
      console.warn(`Storage.get 실패: ${key}`);
      return defaultValue;
    }
  },

  /**
   * 값 저장
   * @param {string} key - 키
   * @param {*} value - 값
   * @returns {boolean} 성공 여부
   */
  set(key, value) {
    try {
      localStorage.setItem(key, JSON.stringify(value));
      return true;
    } catch (e) {
      console.error(`Storage.set 실패: ${key}`, e);
      return false;
    }
  },

  /**
   * 값 삭제
   * @param {string} key - 키
   */
  remove(key) {
    localStorage.removeItem(key);
  },

  /**
   * 전체 삭제
   */
  clear() {
    localStorage.clear();
  }
};

// ==================== API 유틸리티 ====================

/**
 * 재시도 로직이 포함된 fetch 래퍼
 * @param {string} url - URL
 * @param {Object} options - fetch 옵션
 * @param {number} retries - 재시도 횟수
 * @returns {Promise<Object>}
 */
async function fetchWithRetry(url, options = {}, retries = CONFIG?.API?.RETRY_COUNT || 3) {
  const timeout = CONFIG?.API?.TIMEOUT || 10000;
  const retryDelay = CONFIG?.API?.RETRY_DELAY || 1000;

  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), timeout);

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
      const error = new Error(`HTTP ${response.status}: ${response.statusText}`);
      error.status = response.status;
      throw error;
    }

    return await response.json();

  } catch (error) {
    clearTimeout(timeoutId);

    // 네트워크 오류 또는 서버 오류일 때만 재시도
    const shouldRetry = retries > 0 &&
                        !error.name?.includes('Abort') &&
                        (!error.status || error.status >= 500);

    if (shouldRetry) {
      console.warn(`재시도 중... (${CONFIG.API.RETRY_COUNT - retries + 1}/${CONFIG.API.RETRY_COUNT})`);
      await new Promise(r => setTimeout(r, retryDelay));
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
    const baseUrl = CONFIG?.API?.BASE_URL || '';
    return fetchWithRetry(`${baseUrl}${endpoint}`);
  },

  async post(endpoint, data) {
    const baseUrl = CONFIG?.API?.BASE_URL || '';
    return fetchWithRetry(`${baseUrl}${endpoint}`, {
      method: 'POST',
      body: JSON.stringify(data)
    });
  },

  async put(endpoint, data) {
    const baseUrl = CONFIG?.API?.BASE_URL || '';
    return fetchWithRetry(`${baseUrl}${endpoint}`, {
      method: 'PUT',
      body: JSON.stringify(data)
    });
  },

  async delete(endpoint) {
    const baseUrl = CONFIG?.API?.BASE_URL || '';
    return fetchWithRetry(`${baseUrl}${endpoint}`, {
      method: 'DELETE'
    });
  }
};

// ==================== UI 유틸리티 ====================

/**
 * 토스트 메시지 표시
 * CSS: components.css의 .toast, .toast-container 필요
 *
 * @param {string} message - 메시지
 * @param {string} type - 타입 ('success' | 'error' | 'warning' | 'info')
 * @param {number} duration - 표시 시간 (ms)
 */
function showToast(message, type = 'info', duration = CONFIG?.UI?.TOAST_DURATION || 3000) {
  // 토스트 컨테이너 확인/생성
  let container = $('.toast-container');
  if (!container) {
    container = document.createElement('div');
    container.className = 'toast-container';
    document.body.appendChild(container);
  }

  // 토스트 생성 (CSS 클래스만 사용)
  const toast = document.createElement('div');
  toast.className = `toast toast-${type}`;
  toast.textContent = message;

  container.appendChild(toast);

  // 자동 제거
  setTimeout(() => {
    toast.classList.add('toast-exit');
    setTimeout(() => toast.remove(), 300);
  }, duration);
}

/**
 * 로딩 표시
 * CSS: components.css의 .loader-overlay, .loader-spinner 필요
 *
 * @param {boolean} show - 표시 여부
 */
function showLoading(show = true) {
  let loader = $('#global-loader');

  if (show) {
    if (!loader) {
      loader = document.createElement('div');
      loader.id = 'global-loader';
      loader.className = 'loader-overlay';
      loader.innerHTML = '<div class="loader-spinner"></div>';
      document.body.appendChild(loader);
    }
    loader.classList.remove('hidden');
  } else if (loader) {
    loader.classList.add('hidden');
  }
}

// ==================== 검증 유틸리티 ====================

const Validator = {
  /**
   * 이메일 검증
   * @param {string} email
   * @returns {boolean}
   */
  isEmail(email) {
    const regex = CONFIG?.VALIDATION?.EMAIL_REGEX || /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
  },

  /**
   * 비어있지 않은지 확인
   * @param {string} value
   * @returns {boolean}
   */
  isNotEmpty(value) {
    return value !== null && value !== undefined && value.toString().trim() !== '';
  },

  /**
   * 길이 검증
   * @param {string} value
   * @param {number} min
   * @param {number} max
   * @returns {boolean}
   */
  isLength(value, min = 0, max = Infinity) {
    const len = (value || '').length;
    return len >= min && len <= max;
  },

  /**
   * 숫자 검증
   * @param {*} value
   * @returns {boolean}
   */
  isNumber(value) {
    return !isNaN(parseFloat(value)) && isFinite(value);
  }
};

/*
 * 참고: 애니메이션과 .hidden 클래스는
 * components.css 또는 utilities.css에서 정의됩니다.
 * JS에서 스타일을 주입하지 않습니다.
 */
