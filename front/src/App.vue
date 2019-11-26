<template>
  <div id="app">
    <div id="nav">
      <!-- <div v-if="isLogIn"> -->
        <router-link to="/">Home</router-link> |
        <a @click="logout">Logout</a> |
      <!-- </div> -->
      <!-- <div v-else> -->
        <router-link to="/login">Login</router-link> |
        <router-link to="/signup">SignUp</router-link>
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
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
}
#nav a {
  font-weight: bold;
  color: #2c3e50;
}
#nav a.router-link-exact-active {
  color: #42b983;
}
</style>