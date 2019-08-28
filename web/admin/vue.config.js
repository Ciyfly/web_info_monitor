/*
 * @Author: Recar
 * @Date: 2019-08-14 21:50:02
 * @LastEditTime: 2019-08-28 18:35:47
 */
module.exports = {
  devServer: {
    host: "0.0.0.0",
		port: 8070, // 端口号
		https: false,
  //   proxy: {
  //     '/api': {
  //         target: 'http://127.0.0.1:8080',
  //         changeOrigin: true,
  //         ws: true,
  //         pathRewrite: {
  //           '^/api': ''
  //         }
  //     }
  // }
}
}