import axios from 'axios'
import { Message } from 'element-ui'
import router from '../router/routers'


// create an axios instance
const service = axios.create({
  // baseURL: process.env.VUE_APP_BASE_API, // url = base url + request url
  baseURL: 'http://127.0.0.1:8080',
  // baseURL: '/api',
  // withCredentials: true, // send cookies when cross-domain requests
  timeout: 5000, // request timeout
  headers: {  
    'Access-Control-Allow-Origin': '*',
    'Content-Type':'application/json;charset=UTF-8',  
  },  
  withCredentials: true,
})

// request interceptor
// service.interceptors.request.use(
//   config => {
//     // do something before request is sent

//     if (store.getters.token) {
//       // let each request carry token
//       // ['X-Token'] is a custom headers key
//       // please modify it according to the actual situation
//       config.headers['X-Token'] = getToken()
//     }
//     return config
//   },
//   error => {
//     // do something with request error
//     console.log(error) // for debug
//     return Promise.reject(error)
//   }
// )
// response interceptor
service.interceptors.response.use(

  response => {
    const res = response.data
    res.code = res["status_code"]

    if (res.code == 20003 || res.code == 20004) {
      Message({
        message: res.message || 'Error',
        type: 'error',
        duration: 3 * 1000
      })
    }
      if (res.code == 2000) {
        Message({
          message: res.message || 'success',
          type: 'success',
          duration: 2 * 1000,
          onClose: ()=>{
        // 登录成功 跳转到首页
        router.push({path: '/home/'})
          }
        })

      }
        // return Promise.reject(new Error(res.message || 'Error'))
    
  },
  error => {
    const res = error.response.data
    res.code = res["status_code"]

    if (res.code != 200) {
      Message({
        message: res.message || 'Error',
        type: 'error',
        duration: 5 * 1000
      })
    }
      if (res.code == 200) {
        Message({
          message: res.message || 'success',
          type: 'success',
          duration: 5 * 1000
        })
      }
  }
)

export default service