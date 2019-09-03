<!--
 * @Author: Recar
 * @Date: 2019-08-15 22:23:53
 * @LastEditTime: 2019-09-03 17:43:14
-->
<template>
  <div class="home">
<el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" router >
  <el-menu-item index="/home/console/">控制台</el-menu-item>
  <!-- <el-submenu index="/home/subdomain/">
    <template slot="title">域名管理</template>
    <el-menu-item index="2-1">选项1</el-menu-item>
    <el-menu-item index="2-2">选项2</el-menu-item>
    <el-menu-item index="2-3">选项3</el-menu-item>

  </el-submenu> -->
  <el-menu-item index="/home/subdomain/">域名管理</el-menu-item>

  <el-menu-item index="/home/tasks/" >任务中心</el-menu-item>
</el-menu>

<router-view />

  </div>
</template>

<script>
export default {
    data() {
      return {
        msg: "Home",
        activeIndex: '/home/console/',
        activeIndex2: '/home/subdomain/'
      };
    },
    methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
