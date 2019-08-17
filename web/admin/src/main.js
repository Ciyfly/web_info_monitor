/*
 * @Author: Recar
 * @Date: 2019-08-15 23:12:09
 * @LastEditTime: 2019-08-17 14:33:36
 */
import Vue from "vue";
import App from "./App.vue";
import VueRouter from "vue-router";
Vue.use(VueRouter);
import router from "./router/routers.js";
import ElementUI from "element-ui";
import "element-ui/lib/theme-chalk/index.css";
Vue.use(ElementUI);
Vue.config.productionTip = false;

new Vue({
  render: h => h(App),
  router
}).$mount("#app");
