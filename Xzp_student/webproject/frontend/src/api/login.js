// login.js
import request from '@/utils/request';
//获取令牌

// 获取令牌

export function getCSRFToken() {
  return request({
    url: '/get_csrf_token/',
    method: 'get',
  });
}

//登录
export function Userlogin(data) {
  return request({
    url: '/login/',
    method: 'post',
    data: data,
  });
}
