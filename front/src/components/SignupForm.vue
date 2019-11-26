<template>
  <div class="signup-div">
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
          v-model="credentials.username"
        />
      </div>
      <div class="form-group">
        <label for="password1">Password</label>
        <input
          type="password"
          id="password1"
          class="form-control"
          placeholder="비밀번호를 입력해주세요"
          v-model="credentials.password"
        />
      </div>
			<div class="form-group">
        <label for="password2">Password</label>
        <input
          type="password"
          id="password2"
          class="form-control"
          placeholder="비밀번호를 다시 입력해주세요"
          v-model="credentials.password"
        />
      </div>
			<div class="form-group">
        <label for="email">Password</label>
        <input
          type="email"
          id="email"
          class="form-control"
          placeholder="이메일을 입력해주세요"
          v-model="credentials.email"
        />
      </div>
      <button class="btn btn-success" @click="signup">Sign Up</button>
    </div>
  </div>
</template>

<script>
import {mapState, mapActions} from 'vuex'
import axios from 'axios'
import router from '@/router'
export default {
  name: "SignupForm",
  data() {
    return {
      credentials: {
        username: "",
				password1: "",
				password2: "",
				email: ""
      },
      loading: false,
      errors: [],
    };
  },
  methods: {
    signup(dispatch, loginObj) {
      axios
      .post("http://127.0.0.1:8000/api/rest-auth/reegitstration", loginObj)
      .then(response =>  {
        alert("회원가입을 했습니다.")
        router.push({ name: "login"})
        console.log(response)
      })
      .catch(() => {
        alert("이메일과 비밀번호를 확인하세요.")
      })
    }
  }
};
</script>

<style>
</style>