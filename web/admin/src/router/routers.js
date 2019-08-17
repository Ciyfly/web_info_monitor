/*
 * @Author: Recar
 * @Date: 2019-08-15 22:42:02
 * @LastEditTime: 2019-08-17 13:43:51
 */
import VueRouter from "vue-router";

// 导入模板
import Login from "../components/Login.vue";
import Home from "../components/Home.vue";
var router = new VueRouter({
  routes: [
    { path: "/login", component: Login },
    { path: "/home", component: Home },
    { path: "/", component: Home },
    { path: "/home", component: Home }
  ]
});

//  把路由对象暴露出去
export default router;
