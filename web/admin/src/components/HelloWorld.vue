<!--
 * @Author: Recar
 * @Date: 2019-08-15 22:23:53
 * @LastEditTime: 2019-08-15 23:42:26
-->
<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <router-link to="/login">login</router-link>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
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
