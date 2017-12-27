<template>
  <div class="articel-wrapper">
    <div class="article-container"></div>
    <el-form ref="form" :model="form" label-width="80px">

      <el-form-item label="文章标题">
        <el-input v-model="form.name"></el-input>
      </el-form-item>

      <el-form-item label="文章类型">
        <el-select v-model="form.region" placeholder="请选择活动区域" style="width: 100%;">
          <el-option label="java" value="shanghai"></el-option>
          <el-option label="web" value="beijing"></el-option>
        </el-select>
      </el-form-item>

      <el-form-item label="所属标签">
        <el-input v-model="form.name"></el-input>
      </el-form-item>

      <el-form-item label="写作日期">
          <el-date-picker type="date" placeholder="选择日期" v-model="form.date1" style="width: 100%;"></el-date-picker>
      </el-form-item>

      <el-form-item label="文章概要">
        <el-input type="textarea" v-model="form.desc"></el-input>
      </el-form-item>

      <el-form-item label="主要内容">
        <UE :defaultMsg=defaultMsg :config=config ref="ue"></UE>
      </el-form-item>

      <el-form-item>
        <el-button type="primary">保存</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>


<script>
  import UE from '@/components/ueditor.vue'

  export default {
    components: {UE},
    data() {
      return {
        defaultMsg: '这里是UE测试',
        config: {
          initialFrameWidth: null,
          initialFrameHeight: 350
        },
        form: {
          name: '',
          region: '',
          date1: '',
          date2: '',
          delivery: false,
          type: [],
          resource: '',
          desc: ''
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
  .articel-wrapper{
    height:100%;
    display: flex;
    flex-direction: column;
    background-color: #ffffff;
  }
  .article-container{
    padding: 20px;
    flex: 1;
  }
</style>
