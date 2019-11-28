<template>
  <div class="user">
    <h2>My Info</h2>
    <br>
    <img width="300px" src="http://file.mk.co.kr/meet/neds/2019/11/image_readtop_2019_983208_15747235963989824.jpg" alt="">
    <br>
    <br>
    <h3>ID: {{ username }}</h3>
    <h3>Email: {{ useremail }}</h3>
    <h3>Comments: {{ comments }}</h3>
    <h3>Followers: {{ followers }}</h3>
    
    
    
    
  </div>
</template>

<script>
import jwtDecode from 'jwt-decode'
import axios from 'axios'

export default {
  name: "UserDetail",
  data() {
    return {
      user: jwtDecode(localStorage.getItem("access_token")),
      username: '',
      useremail: '',
      comments: [],
      followers: [],
    }
  },
  methods: {
    getuserinfo: function(){
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      axios.get(`${SERVER_IP}/api/v1/userdetail/${this.user.user_id}`)
        .then(response=>{
          this.username = response.data.username
          this.useremail = response.data.email
          this.comments = response.data.comments
          this.followers = response.data.followers
        })
    }
  },
  mounted() {
    this.getuserinfo()
  }
};
</script>

<style>
</style>