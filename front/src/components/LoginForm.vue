<template>
  <div class="login-div">
    <div class="form-group">
      <label for="username">ID </label>
      <input
        type="text"
        id="username"
        class="form-control"
        placeholder="아이디를 입력해주세요"
        v-model="username"
        style="color:black"
      />
      <div class="form-group">
        <label for="password">Password </label>
        <input
          type="password"
          id="password"
          class="form-control"
          placeholder="비밀번호를 입력해주세요"
          v-model="password"
        />
      </div>
      <button class="btn btn-primary" @click="login({username, password})">Login</button>
    </div>                
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  data() {
    return {
      username: null,
      password: null
    };
  },
  computed: {
    ...mapState(["isLogin", "isLoginError"])
  },
  methods: {
    ...mapActions(["login"])
  }
};
</script>

<style>
#username{
  color: black
}
</style>