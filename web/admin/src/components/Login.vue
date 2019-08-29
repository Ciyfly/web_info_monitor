<!--
 * @Author: Recar
 * @Date: 2019-08-15 22:06:17
 * @LastEditTime: 2019-08-29 18:39:23
-->
<template>
  <div>
    <div class="title-container">
      <h3 class="title">资产监控登录</h3>
    </div>
    <el-form name="form">
      <el-form-item prop="username">
        <el-input
          ref="username"
          v-model="username"
          placeholder="用户名"
          name="username"
          type="text"
          tabindex="1"
          autocomplete="on"
        />
      </el-form-item>

      <el-form-item>
        <el-input
          v-model="password"
          placeholder="密码"
          name="password"
          type="password"
          tabindex="2"
          autocomplete="on"
          @keyup.enter.native="handleLogin"
        />
      </el-form-item>

      <el-button
        type="primary"
        style="width:100%;margin-bottom:30px;"
        @click.native.prevent="handleLogin"
      >登录</el-button>
    </el-form>
  </div>
</template>
<script>

import { login } from "../api/user";

export default {
  data() {
    return {
      username: "admin",
      password: "admin"
    };
  },
  methods: {
    handleLogin() {
      var test_data = login({
        username: this.username,
        password: this.password
      });
      console.log(test_data)
    }
  }
};
</script>


<style lang="scss" scoped>
form {
  margin: 0 auto;
  width: 300px;
  height: 100px;
}
</style>
