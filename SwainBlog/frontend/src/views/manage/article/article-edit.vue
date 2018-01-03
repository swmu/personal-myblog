<template>
  <div class="articel-wrapper">
    <div class="article-container"></div>
    <el-form ref="form" :model="article" label-width="80px">

      <el-form-item label="文章标题">
        <el-input v-model="article.title"></el-input>
      </el-form-item>

      <el-form-item label="作  者">
        <el-input v-model="article.author"></el-input>
      </el-form-item>

      <el-form-item label="文章类型">
        <!--<el-select v-model="article.type" placeholder="请选择文章类型" style="width: 100%;">-->
          <!--<el-option label="java" value="java"></el-option>-->
          <!--<el-option label="web" value="web"></el-option>-->
        <!--</el-select>-->
        <el-input v-model="article.type"></el-input>
      </el-form-item>

      <el-form-item label="所属标签">
        <el-input v-model="article.labels"></el-input>
      </el-form-item>

      <el-form-item label="写作日期">
        <el-col :span="11">
          <el-date-picker type="date" placeholder="选择日期" v-model="article.date" style="width: 100%;" value-format="yyyy-MM-dd"></el-date-picker>
        </el-col>
        <el-col class="line" :span="2">-</el-col>
        <el-col :span="11">
          <el-time-picker type="fixed-time" placeholder="选择时间" v-model="article.time" style="width: 100%;" value-format="HH:mm:ss"></el-time-picker>
        </el-col>
      </el-form-item>

      <el-form-item label="文章图片">
        <el-upload style="float:left;" name="img" :limit=1
          action="http://127.0.0.1:8000/upload/imageUpload"
          list-type="picture-card"
          :on-preview="handlePictureCardPreview"
          :on-success="handleAvatarSuccess"
          :on-remove="handleRemove"
          :data="{type:'article'}">
          <i class="el-icon-plus"></i>
        </el-upload>
        <el-dialog :visible.sync="dialogVisible" size="tiny">
          <img width="100%" :src="uploadImg" alt="">
        </el-dialog>

      </el-form-item>

      <el-form-item label="文章概要">
        <el-input type="textarea" v-model="article.chief"></el-input>
      </el-form-item>

      <el-form-item label="主要内容">
        <UE :defaultMsg=defaultMsg :config=config ref="ue"></UE>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" v-on:click="saveArticle">保存</el-button>
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
        dialogVisible: false,
        config: {
          initialFrameWidth: null,
          initialFrameHeight: 350,
          serverUrl:'http://127.0.0.1:8000/rest/getConfig'
        },

        article: {
          title: '',
          author: '',
          type: '',
          labels: '',
          date: '',
          time: '',
          chief: '',
          image_path: '',
          content:''
        },
        uploadImg:''
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
        console.log(content);
      },
      // 图片上传成功后返回
      handleAvatarSuccess(res, file) {
        this.article.image_path = res.imgPath;
        this.uploadImg = URL.createObjectURL(file.raw);
      },
      handlePictureCardPreview(file) {
        this.dialogVisible = true;
      },
      handleRemove(file, fileList) {
        console.log(file, fileList);
      },
      saveArticle(){
          var me = this;
          let content = this.$refs.ue.getUEContent();
          me.article.content = content;
          console.log(me.article);
          me.$axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/rest/article/',
            data: {
              "article":me.article
            }
          }).then(function (response) {
            console.log(response);
            me.$message('保存文章成功');
          });
      }
    }
  };
</script>


<style scoped>
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

  /*上传文件演示*/
  .el-upload{
    border: 1px solid #dcac6c;
    border-radius: 5px;
    float: left;
  }
  .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  }
  .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }
  /*上传文件演示*/
</style>
