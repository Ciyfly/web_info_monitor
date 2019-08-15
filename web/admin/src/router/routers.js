/*
 * @Author: Recar
 * @Date: 2019-08-15 22:42:02
 * @LastEditTime: 2019-08-15 23:10:23
 */
import VueRouter from 'vue-router'

// 导入模板
import Login from '../components/Login.vue'
var router = new VueRouter({
  routes: [
    { path: '/login', component: Login }

  ]
})

//  把路由对象暴露出去
export default router
