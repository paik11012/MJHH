import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Singup from '../views/Signup.vue'
import Admin from '../views/Admin.vue'
import User from '../views/UserPage.vue'
import Search from '../views/Search.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/signup',
    name: 'signup',
    component: Singup
  },
  {
    path: '/admin',
    name: 'admin',
    component: Admin
  },
  {
    path: '/user/:id',
    name: 'user',
    component: User
  },
  {
    path: '/:name',
    name: 'search',
    component: Search
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
