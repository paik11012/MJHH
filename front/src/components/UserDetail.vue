<template>
  <div class="user">
    <h1>hi</h1>
  </div>
</template>

<script>
import jwtDecode from 'jwt-decode'
import axios from 'axios'

export default {
  name: "UserDetail",
  data() {
    return {
    user: jwtDecode(localStorage.getItem("access_token"))
    }
  },
  methods: {
    getuserinfo: function(){
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      axios.get(`${SERVER_IP}/api/v1/userdetail/${this.user.user_id}`)
        .then(response=>{
          console.log(response)
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