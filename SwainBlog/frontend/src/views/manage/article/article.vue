<template>
  <div class="articel-wrapper">
    <el-container>
      <el-aside width="200px">
        <el-menu>
          <el-menu-item index="1" v-on:click='showClick'>
            <i class="el-icon-menu"></i>
            <span slot="title" >文章查看</span>
          </el-menu-item>
          <el-menu-item index="2" v-on:click='editClick'>
            <i class="el-icon-setting"></i>
            <span slot="title">文章编辑</span>
          </el-menu-item>
        </el-menu>
      </el-aside>


      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </div>
</template>


<script>
export default{
  methods:{
      showClick(){
          var me = this;
          me.$router.push('/managehome/article/show')
      },

      editClick(){
        var me = this;
        me.$router.push('/managehome/article/edit')
      }
    }
}
</script>

<style>
  .articel-wrapper{
    width:100%;
    height:100%;
    background-color: #ffffff;
    display: flex;
    flex-direction: column;
  }
  .el-container{
    flex:1;
  }
  .el-main{
    width:100%;
    height:100%;
    display: flex;
    flex-direction: column;
  }
</style>
