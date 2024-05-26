// request.js
import axios from 'axios';

// 创建 Axios 实例
const instance = axios.create({
  baseURL: 'http://127.0.0.1:8000/',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// 从 Cookie 中获取 CSRF 令牌
function getCSRFTokenFromCookie() {
  const csrfCookie = document.cookie
    .split(';')
    .map(cookie => cookie.trim())
    .find(cookie => cookie.startsWith('csrftoken='));

  // 如果找到了 'csrftoken' Cookie，则从中提取 CSRF 令牌
  if (csrfCookie) {
    return csrfCookie.split('=')[1];
  } else {
    // 如果未找到 'csrftoken' Cookie，则返回 null
    return null;
  }
}


// 导出默认的请求函数
export default function request(options) {
  // 检查是否存在 CSRF 令牌，并将其加入请求头中
  const csrfToken = getCSRFTokenFromCookie(); // 从 Cookie 中获取 CSRF 令牌
  if (csrfToken) {
    instance.defaults.headers.common['X-CSRFToken'] = csrfToken;
  }
  return instance(options);
}
