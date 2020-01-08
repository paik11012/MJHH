<template>
  <div id="app" class="shadow p-3 mb-2 bg-dark text-white" >
    <b-navbar toggleable="lg" type="dark" variant="dark" id="navbar">
      <b-navbar-brand to="/">Movies</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-form-input size="sm" class="mr-sm-2" placeholder="Search" v-model="searchObj"></b-form-input>
            <b-button size="sm" class="my-2 my-sm-0" type="submit" @click="getSearch">Search</b-button>
          </b-nav-form>
          <div v-if="isLogin">
            <b-nav-item-dropdown right :text="this.$store.state.userInfo.username">
              <b-dropdown-item to="/admin" v-if="this.$store.state.userInfo.userpk=== 1">Admin</b-dropdown-item>
              <b-dropdown-item
                :to="{ name: 'user', params: { id: this.$store.state.userInfo.userpk }}"
              >My Page</b-dropdown-item>
              <b-dropdown-item @click="logout" to="/">Logout</b-dropdown-item>
            </b-nav-item-dropdown>
          </div>
          <div v-else>
            <b-nav-item-dropdown right text="Guest">
              <b-dropdown-item to="/login">Login</b-dropdown-item>
              <b-dropdown-item to="/signup">SignUp</b-dropdown-item>
            </b-nav-item-dropdown>
          </div>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
    <img height="60%" src="./assets/sea.png" alt="" id="bgimage">
    <link href="https://fonts.googleapis.com/css?family=Jua|Nanum+Gothic&display=swap" rel="stylesheet">
    <div class="container col-10">
      <router-view />
    </div>
    <!-- 끝에 -->
    <div>
</div>
<div class="jumbotron" id="jumbo">
  <h2 class="display-5" >2018-2019 Popular Movies</h2>
  <p class="lead">김현화 & 백민주</p>
  <p>For more information visit website</p>
  <p class="lead">
    <a class="btn btn-dark" href="https://github.com/paik11012/MJHH" role="button" target="_blank">Github</a>
  </p>
</div>

  </div>
</template>

<script>
// import router from '@/router'
import { mapState, mapActions } from "vuex";
import jwtDecode from "jwt-decode";
import router from "@/router";

export default {
  name: "App",
  data() {
    return {
      searchObj: ''
    }
  },
  methods: {
    ...mapActions(["logout"]),
    getSearch: function() {
      if (this.searchObj !== ''){
        router.push({name: 'search', params: {name: this.searchObj}})
      }
    }
  },
  computed: {
    ...mapState(["isLogin"]),
  },
  mounted() {
    if (localStorage.getItem("access_token") !== "null") {
      const token = localStorage.getItem("access_token");
      const user = jwtDecode(token);
      const userInfo = {
        userpk: user.user_id,
        token: token,
        username: user.username
      };
      this.$store.commit("loginSuccess", userInfo);
      this.userInfo = userInfo;
    }
  }
};
</script>
<style>
#image{
  width: max-content
}
#navbar{
  font-family: 'Jua', sans-serif;
}
#app {
  font-family: 'Nanum Gothic', monospace;
  
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
#jumbo{
  color:black;
  background-color: darkgrey;
  height: 280px;
  font-family: 'Jua', sans-serif;
  margin-bottom: 2px
}
/* 이미지 크기 고정하기 */
img {
  max-width: 100%;
  height: auto;
}
</style>