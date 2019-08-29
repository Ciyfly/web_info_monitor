<!--
 * @Author: Recar
 * @Date: 2019-08-15 22:06:17
 * @LastEditTime: 2019-08-29 16:38:11
-->
<template>
  <div>
    <div class="title-container">
      <h3 class="title">用户注册</h3>
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
          name="password"
          type="password"
          tabindex="2"
          autocomplete="on"
          placeholder="密码"
        />
      </el-form-item>

      <el-form-item>
        <el-input
          v-model="email"
          name="email"
          type="text"
          tabindex="2"
          autocomplete="on"
          placeholder="邮箱"
        />
      </el-form-item>

    <!-- 邀请码 -->
      <el-form-item>
        <el-input
          v-model="invitation_code"
          name="invitation_code"
          type="text"
          tabindex="2"
          autocomplete="on"
          placeholder="邀请码"
          @keyup.enter.native="handleRegister"
        />
      </el-form-item>
      

      <el-button
        type="primary"
        style="width:100%;margin-bottom:30px;"
        @click.native.prevent="handleRegister"
      >注册</el-button>
    </el-form>
  </div>
</template>
<script>

import { register } from "../api/user";
import { Message } from 'element-ui'
export default {
  data() {
    return {
      username: "admin",
      password: "admin",
      email: "admin@admin",
      invitation_code: "邀请码"
    };
  },
  methods: {
    handleRegister() {
        if (this.invitation_code=="" || this.username==""
        || this.password == "" || this.email == "" ){
            Message({
                message: '都不能为空',
                type: 'error',
                duration: 5 * 1000
            })
            return
        }
      register({
        username: this.username,
        password: this.password,
        email: this.email,
        invitation_code: this.invitation_code
      });
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
