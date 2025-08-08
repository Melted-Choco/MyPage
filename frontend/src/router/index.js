import { createRouter, createWebHistory } from 'vue-router'
import PostList from '@/components/PostList.vue'
import PostDetail from '@/components/PostDetail.vue'

const routes = [
  {
    path: '/category/:category',
    name: 'PostList',
    component: PostList,
    props: true,
  },
  {
    path: '/post/:id',
    name: 'PostDetail',
    component: PostDetail,
    props: true,
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
