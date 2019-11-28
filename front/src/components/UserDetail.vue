<template>
  <div class="user">
    {{ username }}
    {{ useremail }}
    {{ comments }}
    {{ followers }}
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