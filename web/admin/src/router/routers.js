/*
 * @Author: Recar
 * @Date: 2019-08-15 22:42:02
 * @LastEditTime: 2019-08-29 16:33:06
 */
import VueRouter from "vue-router";

// 导入模板
import Login from "../components/Login.vue";
import Register from "../components/Register.vue";

import Home from "../components/Home.vue";
var router = new VueRouter({
  routes: [
    { path: "/login", component: Login },
    { path: "/register", component: Register },
    { path: "/home", component: Home },
    { path: "/", component: Home },
  ]
});

//  把路由对象暴露出去
export default router;
