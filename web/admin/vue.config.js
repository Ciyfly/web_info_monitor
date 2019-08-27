/*
 * @Author: Recar
 * @Date: 2019-08-14 21:50:02
 * @LastEditTime: 2019-08-22 19:53:41
 */
module.exports = {
  devServer: {
    disableHostCheck: true,
  //   proxy: {//配置跨域
  //     '/api': {
  //         target: 'http://127.0.0.1:8080',//这里后台的地址模拟的;应该填写你们真实的后台接口
  //         ws: true,
  //         changOrigin: true,//允许跨域
  //         pathRewrite: {
  //             '^/api': ''//请求的时候使用这个api就可以
  //         }
  //     }
      
  // }
  proxy: "http://localhost:8080"

  },
    }
    
