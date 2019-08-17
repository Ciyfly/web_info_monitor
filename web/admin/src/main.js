/*
 * @Author: Recar
 * @Date: 2019-08-15 23:12:09
 * @LastEditTime: 2019-08-17 17:27:18
 */
import Vue from "vue";
import App from "./App.vue";
import VueRouter from "vue-router";
Vue.use(VueRouter);
import router from "./router/routers.js";
import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";
Vue.use(ElementUI);

import axios from "axios";
import VueAxios from "vue-axios";
// 通过use方法加载axios插件
Vue.use(VueAxios, axios);
Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
  router
}).$mount("#app");
