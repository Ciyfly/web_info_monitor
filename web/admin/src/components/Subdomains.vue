<template>
  <div>
    <el-card class="box-card domain-card" v-for="domain in domains" :key="domain.name">
      <div slot="header" class="clearfix">
        <span>{{domain.name}}</span>
        <el-button style="float: right; padding: 3px 0" type="text">详情</el-button>
        <br />
        <br />
        <span>{{domain.url}}</span>
        <br />
        <span>{{domain.last_time}}</span>
        <br />
        <span>{{domain.subdomain_count}}</span>
      </div>
    </el-card>
  </div>
</template>
<script>
export default {
  data() {
    return {
      domains: [
        {
          name: "百度",
          url: "www.baidu.com",
          last_time: "2019-09-05",
          subdomain_count: 200
        },
        {
          name: "中通",
          url: "www.zto.com",
          last_time: "2019-09-05",
          subdomain_count: 100
        },
        {
          name: "小米",
          url: "www.mi.com",
          last_time: "2019-09-05",
          subdomain_count: 400
        },
        {
          name: "京东",
          url: "www.jd.com",
          last_time: "2019-09-05",
          subdomain_count: 800
        }
      ]
    };
  }
};
</script>
<style>
.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both;
}

.box-card {
  width: 480px;
}
.domain-card {
  float: left;
  width: 23%;
  padding-left: 5px;
  margin-left: 5px;
}
</style>
