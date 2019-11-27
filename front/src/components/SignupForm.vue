<template>
  <div class="formContainer">
    <form class="login-box">
      <p>ID</p>
      <input type="text" v-model="username" name="username" label="ID를 입력하세요" />
      <p>Email</p>
      <input type="text" v-model="email" name="useremail" label="이메일을 입력하세요" />
      <p>Password</p>
      <input type="password" v-model="password1" name="userpassword" label="비밀번호를 입력하세요" />
      <p>Comfirm Password</p>
      <input type="password" v-model="password2" name="userpassword" label="비밀번호 확인" />
      <br />
    </form>
    <br>
    <div class="login-btn">
      <input
        type="submit"
        class="btn btn-primary"
        name="submit"
        @click="signup({username, email, password1, password2})"
        value="회원가입"
      />
    </div>
  </div>   
</template>

<script>
import { mapActions } from "vuex"

export default {
  data() {
    return {
      username: null, 
      email: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    ...mapActions(["signup"])
  }
}

</script>