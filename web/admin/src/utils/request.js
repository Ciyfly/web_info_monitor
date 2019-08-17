/*
 * @Author: Recar
 * @Date: 2019-08-17 17:31:08
 * @LastEditTime: 2019-08-17 18:49:57
 */
import axios from "axios"; //引用axios
import { Message } from "element-ui";

if (process.env.NODE_ENV == "dev") {
  axios.defaults.baseURL = "http://127.0.0.1:8080";
} else if (process.env.NODE_ENV == "debug") {
  axios.defaults.baseURL = "http://127.0.0.1:8080";
} else if (process.env.NODE_ENV == "production") {
  axios.defaults.baseURL = "http://127.0.0.1:8080";
} else {
  axios.defaults.baseURL = "http://127.0.0.1:8080";
}
axios.defaults.timeout = 10000;

//创建axios实例
var service = axios.create({
  headers: {
    "content-type": "application/json",
    token: "14a1347f412b319b0fef270489f"
  }
});

export function get(url, param) {
  //get请求，其他类型请求复制粘贴，修改method

  return new Promise((cback, reject) => {
    service({
      method: "get",
      url,
      params: param
    })
      .then(res => {
        //axios返回的是一个promise对象
        var res_code = res.status.toString();
        if (res_code.charAt(0) == 2) {
          cback(res); //cback在promise执行器内部
        } else {
          // eslint-disable-next-line no-console
          console.log(res, "异常1");
        }
      })
      .catch(err => {
        if (!err.response) {
          // eslint-disable-next-line no-console
          console.log("请求错误");
          //Message是element库的组件，可以去掉
          Message({
            showClose: true,
            message: "请求错误",
            type: "error"
          });
        } else {
          reject(err.response);
          // eslint-disable-next-line no-console
          console.log(err.response, "异常2");
        }
      });
  });
}
export function post(url, data) {
  console.log(url);
  //post
  return new Promise((cback, reject) => {
    service({
      method: "post",
      url,
      data
    })
      .then(res => {
        //axios返回的是一个promise对象
        var res_code = res.status.toString();
        if (res_code.charAt(0) == 2) {
          cback(res); //cback在promise执行器内部
        } else {
          // eslint-disable-next-line no-console
          console.log(res, "异常1");
        }
      })
      .catch(err => {
        if (!err.response) {
          // eslint-disable-next-line no-console
          console.log("请求错误");
          //Message是element库的组件，可以去掉
          Message({
            showClose: true,
            message: "请求错误",
            type: "error"
          });
        } else {
          reject(err.response);
          // eslint-disable-next-line no-console
          console.log(err.response, "异常2");
        }
      });
  });
}
