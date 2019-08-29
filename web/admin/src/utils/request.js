import axios from 'axios'
import { Message } from 'element-ui'


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
    if (res.code != 200) {
      Message({
        message: res.message || 'Error',
        type: 'error',
        duration: 5 * 1000
      })

      if (res.code == 200) {
        Message({
          message: res.message || 'success',
          type: 'success',
          duration: 5 * 1000
        })
      }
        // return Promise.reject(new Error(res.message || 'Error'))
    } else {
      return res
    }
  },
  error => {
    const res = error.response.data
    Message({
        message: res.message || 'Error',
        type: 'error',
        duration: 5 * 1000
      })
  }
)

export default service