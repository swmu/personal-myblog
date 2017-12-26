<template>
    <div class="login-wrapper">
      <div class="login-container">
          <el-form :label-position="labelPosition" label-width="80px" :model="userinfo">
            <el-form-item label="用户名">
              <el-input v-model="userinfo.userName"></el-input>
            </el-form-item>
            <el-form-item label="密 码">
              <el-input type="password" v-model="userinfo.password"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="onSubmit">登录</el-button>
              <el-button @click="reset">重置</el-button>
            </el-form-item>
          </el-form>

      </div>
    </div>
</template>


<script>

  export default{
      data(){
          return {
            labelPosition: 'right',
            userinfo: {
              userName: '',
              password: '',
            }
          }
      },
      methods:{
        onSubmit(){
            var me = this;
            me.$router.push('/managehome')
        },
        reset(){
            var me = this;
            me.userinfo.userName = '';
            me.userinfo.password = '';
        }
      }
  }
</script>


<style>
  .login-wrapper{
    height:100%;
    width:100%;
    display: flex;
    flex-direction:column;
    justify-content:center;
  }
  .login-container{
    width:400px;
    height:300px;
    align-self: center;
  }
</style>
