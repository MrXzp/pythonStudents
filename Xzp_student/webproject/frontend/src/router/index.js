import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)
// 公共路由
export const constantRoutes = [
  {
    path: '/login',
    component: () => import('@/views/login'),
    hidden: true
  },
  {
    path: '',
    component: () => import('@/views/home/Home'),
    hidden: true
  },
]

// 创建 Router 实例
const router = new Router({
  routes: constantRoutes
})

export default router


