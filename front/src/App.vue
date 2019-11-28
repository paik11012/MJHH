<template>
  <div id="app" class="shadow p-3 mb-2 bg-dark text-white" >
    <link href="https://fonts.googleapis.com/css?family=Noto+Serif+KR|Stylish&display=swap" rel="stylesheet">
    <div id="nav">
      <!-- <div v-if="isLogIn"> -->
        <router-link to="/">Home</router-link> |
        <a @click="logout">Logout</a> |
      <!-- </div> -->
      <!-- <div v-else> -->
        <router-link to="/login">Login</router-link> |
        <router-link to="/signup">SignUp</router-link> |
        <router-link to="/admin">Admin</router-link>
      <!-- </div> -->
    </div>
    <div class="container col-6">
      <router-view/>
    </div>
  </div>
</template>

<script>
// import router from '@/router'
import { mapState, mapActions } from "vuex"

export default {
  name: 'App',
  methods: {
    ...mapActions(["logout"])
  },
  computed: {
    ...mapState(["isLogin"])
  },
}
</script>
<style>


#app {
  font-family: 'Stylish', sans-serif;
  /* font-family: 'Noto Serif KR', serif; */
  min-height: 1000px;
  /* font-family: 'Avenir', Helvetica, Arial, sans-serif; */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
#nav {
  padding: 30px;
}
#nav a {
  font-weight: bold;
  color: #f0f0f0;
}
#nav a.router-link-exact-active {
  color: #8dd9ff;
}
</style>