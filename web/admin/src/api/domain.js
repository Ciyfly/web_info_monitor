/*
 * @Author: Recar
 * @Date: 2019-08-17 17:30:52
 * @LastEditTime: 2019-09-05 16:53:44
 */
import request from "../utils/request";

export function getDomain() {
  return request({
    url: '/domain/',
    method: 'get',
  })
}

export function addDomain(data) {
  return request({
    url: '/domain/',
    method: 'post',
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
