<template>
  <div class="wrapper">
      <div class="header">
        文章
      </div>

      <div class="content">
          <ul>
             <li v-for="article in articles">
                <div class="article-img">
                  <img :src="article.image_path" alt="图片">
                </div>
               <div class="aricle-info">
                  <div class="brif"> {{article.chief}}</div>
                  <div class="labels">
                      <div class="labels-info">
                        <label>创建时间:</label>{{article.date}}
                        <label>类型:</label>{{article.type}}
                        <label>标签:</label>{{article.labels}}
                      </div>
                      <div class="labels-btn">
                        <el-button type="primary" size="mini">查看</el-button>
                        <el-button type="info" size="mini">修改</el-button>
                        <el-button type="danger" size="mini">删除</el-button>
                      </div>
                  </div>
               </div>
             </li>
          </ul>
      </div>

      <div class="footer">
        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="currentPage"
          :page-size="100"
          layout="total, sizes, prev, pager, next, jumper"
          :total="total">
        </el-pagination>
      </div>
  </div>
</template>

<script>
  export default{
      data() {
        return {
          total:400,
          currentPage: 1,
          articles:{
            image_path:'',
            chief:'sdfd',
            date:'',
            type:'sd',
            labels:''
          }
        };
      },
      created(){
        var me = this;
        me.getArticles();
      },
      methods: {
        handleSizeChange(val) {
          console.log(`每页 ${val} 条`);
        },
        handleCurrentChange(val) {
          console.log(`当前页: ${val}`);
        },
        // 获取文章信息
        getArticles(){
          var me = this;
          me.$axios({
            method: 'get',
            url: 'http://127.0.0.1:8000/rest/article/',
            data: {
              "article":me.article
            }
          }).then(function (response) {
            me.articles = response.data;
          });
        }
      },
  }
</script>

<style scoped>
  .content ul{
    list-style: none;
  }
  .content li{
    height:80px;
    display: flex;
    padding: 5px;
    flex-direction: row;
    border-bottom: 1px solid #00b8ff;
  }
  .wrapper{
    flex:1;
    display:flex;
    flex-direction: column;
    overflow: hidden;
  }
  .header{
    height:40px;
    background-color: #8c939d;
    line-height: 40px;
  }
  .content{
    flex:1;
    overflow: auto;
  }
  .footer{
    height:40px;
  }

  .article-img{
    float:left;
    height:100%;
    width:80px;

  }
  .article-img>img{
    height:100%;
    width:100%;
  }
  .aricle-info{
    height:40px;
    flex: 1;
    text-align: left;
  }
  .brif{
    height:100%;
    width:100%;
    text-overflow: clip;
  }
  .labels{
      height: 40px;
      display: flex;
      flex-direction: row;
  }
  .labels-info{
    flex: 1;
    line-height: 40px;
  }
  .labels-info>label{
    margin-left: 10px;
  }
  .labels-info>label:first-child{
    margin-left: 0px;
  }
  .labels-btn{
    padding: 0px 10px;
  }
</style>
