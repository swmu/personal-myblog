import Vue from 'vue'
import Router from 'vue-router'

// manage page
import login from '@/views/login.vue'
import manageHome from '@/views/manage/manage-home.vue'
// article
import article from '@/views/manage/article/article.vue'
import articleEdit from '@/views/manage/article/article-edit.vue'
import articleShow from '@/views/manage/article/article-show.vue'
// show page
import home from '@/views/show/home.vue'

Vue.use(Router)

export default new Router({
  routes: [
    // show page
    {
      path: '/',
      name: 'home',
      component: home,
      children:[

      ]
    },

    //  manage login
    {
      path:'/admin',
      name:'admin',
      component: login
    },

    // manage page
    {
      path:'/managehome',
      component:manageHome,
      children:[
        {
          path:'article',
          component:article,
          children:[
            {
              path:'edit',
              component:articleEdit
            },
            {
              path:'show',
              component:articleShow
            }
          ]
        }
      ]
    }

  ]
})
