<template>
  <el-container>
    <el-aside width="200px">Aside</el-aside>
    <el-main>
      <UE :defaultMsg=defaultMsg :config=config ref="ue"></UE>
    </el-main>
  </el-container>
</template>

<script>
  import UE from '../components/ueditor.vue';
  export default {
    components: {UE},
    data() {
      return {
        defaultMsg: '这里是UE测试',
        config: {
          initialFrameWidth: null,
          initialFrameHeight: 350
        }
      }
    },
    methods: {
      getUEContent() {
        let content = this.$refs.ue.getUEContent();
        this.$notify({
          title: '获取成功，可在控制台查看！',
          message: content,
          type: 'success'
        });
        console.log(content)
      }
    }
  };
</script>

<style>
.el-container{
  height:100%;
  width:100%;
}
.el-aside {
  height: inherit;
  background-color: #D3DCE6;
  color: #333;
  text-align: center;
  line-height: 200px;
}

.el-main {
  height: inherit;
  background-color: #E9EEF3;
  color: #333;
  text-align: center;
  line-height: 160px;
}
</style>
