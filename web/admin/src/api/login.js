/*
 * @Author: Recar
 * @Date: 2019-08-17 17:30:52
 * @LastEditTime: 2019-08-17 18:50:33
 */
import { post, get } from "../utils/request";

export function login(data) {
  return post("/user/login", data);
}

export function getInfo(token) {
  return get({
    url: "/user/info",
    params: { token }
  });
}

export function logout(token) {
  return get({
    url: "/user/logout",
    params: { token }
  });
}
