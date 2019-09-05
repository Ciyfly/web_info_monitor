<template>
    <div>
        <el-card class="box-card" v-for="domain in domains">
    <div slot="header" class="clearfix">
        <span>卡片名称</span>
        <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
    </div>
    <div v-for="o in 4" :key="o" class="text item">
        {{'列表内容 ' + o }}
    </div>
</el-card>
    </div>
</template>
<script>
export default {
    domains:[
        {"name": "百度", url: "www.baidu.com", "last_time": "2019-09-05", "subdomain_count":200},
        {"name": "中通", url: "www.zto.com", "last_time": "2019-09-05", "subdomain_count":100},
        {"name": "小米", url: "www.mi.com", "last_time": "2019-09-05", "subdomain_count":400},
        {"name": "京东", url: "www.jd.com", "last_time": "2019-09-05", "subdomain_count":800},
    ]
}
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
    clear: both
}

.box-card {
    width: 480px;
}
</style>
