<template>
  <div class="login-div">
    <div v-if="loading" class="spinner-border" role="status">
      <span class="sr-only">Loading...</span>
    </div>
    <div v-else class="login-form">
      <div v-if="errors.length" class="alert alert-danger">
        <h4>다음의 오류를 해결해주세요.</h4>
        <hr>
        <div v-for="(error, idx) in errors" :key="idx">{{ error }}</div>
      </div>
      <div class="form-group">
        <label for="username">USER NAME</label>
        <input
          type="text"
          id="username"
          class="form-control"
          placeholder="아이디를 입력해주세요"
          v-model="username"
        />
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input
          type="password"
          id="password"
          class="form-control"
          placeholder="비밀번호를 입력해주세요"
          v-model="password"
        />
      </div>
      <button class="btn btn-success" @click="login({username, password})">Login</button>
    </div>
  </div>
</template>

<script>
import {mapState, mapActions} from 'vuex'
export default {
  data() {
    return {
      username: null,
      password: null
    }
  },
  computed: {
    ...mapState(["isLogin", "isLoginError"])
  },
  methods: {
  ...mapActions(["login"])
  },
}
</script>

<style>
</style>