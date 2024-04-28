import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://127.0.0.1:8000/', // 设置请求的基本 URL
  timeout: 10000, // 设置超时时间为 10 秒
  headers: {
    'Content-Type': 'application/json', // 设置请求头为 JSON
  },
});

// 封装 GET 请求
export function get(url, params) {
  return instance.get(url, { params });
}

// 封装 POST 请求
export function post(url, data) {
  return instance.post(url, data);
}
