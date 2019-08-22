/*
 * @Author: Recar
 * @Date: 2019-08-17 17:30:52
 * @LastEditTime: 2019-08-22 19:20:52
 */
import request from "../utils/request";

export function login(data) {
  return request({
    url: '/api/user/login',
    method: 'post',
    data
  })
}

export function getInfo(token) {
  return request({
    url: '/api/user/info',
    method: 'get',
    params: { token }
  })
}

export function logout() {
  return request({
    url: '/api/user/logout',
    method: 'post'
  })
}
