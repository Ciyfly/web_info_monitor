/*
 * @Author: Recar
 * @Date: 2019-08-15 22:42:02
 * @LastEditTime: 2019-09-03 17:54:34
 */
import VueRouter from "vue-router";

// 导入模板
import Login from "../components/Login.vue";
import Register from "../components/Register.vue";

import Home from "../components/Home.vue";

// Home下子路由
import Console from "../components/Console.vue";
import Subdomains from "../components/Subdomains.vue";
import Tasks from "../components/Tasks.vue";
var router = new VueRouter({
  routes: [
    { path: "/login", component: Login },
    { path: "/register", component: Register },
    { path: "/home", component: Home,
        children: [
          {
            path: 'console',
            component: Console
          },
          {
            path: 'subdomain',
            component: Subdomains
          },
          {
            path: 'tasks',
            component: Tasks
          },
        ],
      },
    { path: "/", component: Home },
  ]
});

//  把路由对象暴露出去
export default router;
