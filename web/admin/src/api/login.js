/*
 * @Author: Recar
 * @Date: 2019-08-17 17:30:52
 * @LastEditTime: 2019-08-29 12:41:39
 */
import request from "../utils/request";

export function login(data) {
  return request({
    url: '/user/login/',
    method: 'post',
    // data: qs.stringify(data)
    data: data
  })
}

export function getInfo(token) {
  return request({
    url: '/user/info',
    method: 'get',
    params: { token }
  })
}

export function logout() {
  return request({
    url: '/user/logout',
    method: 'post'
  })
}
