<template>
  <div>
    <h3>User List</h3>
    <div v-for="user in userlist" :key="user.id">
      <button class="btn btn-lg" @click="userdetail(user.id)" id="username" >{{ user.username }} </button>
      <br>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import router from "@/router";

export default {
  name: "AdminUser",
  data() {
    return {
      userlist: []
    };
  },
  methods: {
    getuser: function() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      axios
        .get(`${SERVER_IP}/api/v1/userlist/`)
        .then(response => {
          this.userlist = response.data;
        })
        .catch(() => {
          alert("Fail");
        });
    },
    userdetail: function(userpk) {
      router.push(`/user/${userpk}`)
    }
  },
  mounted() {
    this.getuser();
  }
};
</script>

<style>
#username{
  color:white
}
</style>