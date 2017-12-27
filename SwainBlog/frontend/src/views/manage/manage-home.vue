<template>
  <div class="manage-home-wrapper">
    <el-container>
      <el-header>
        <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
          <el-menu-item index="1">首页</el-menu-item>
          <el-submenu index="2">
            <template slot="title">内容管理</template>
            <el-menu-item index="2-1" v-on:click="showArticle">文章管理</el-menu-item>
            <el-menu-item index="2-2">今日事</el-menu-item>
            <el-menu-item index="2-3">其他</el-menu-item>
          </el-submenu>
          <el-menu-item index="3">个人中心</el-menu-item>
        </el-menu>
      </el-header>


      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        activeIndex: '1'
      };
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      },
      showArticle(){
          var me = this;
          me.$router.push("/managehome/article");
      }
    }
  }
</script>


<style>
  .manage-home-wrapper{
    height: 100%;
    width:100%;
    display: flex;
    flex-direction: column;
  }
  .el-header{
    /*padding: 0px;*/
    /*background-color: antiquewhite;*/
  }
  .el-main{
    padding: 10px;
    background-color: #fff;
  }
</style>
