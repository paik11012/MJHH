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
      <p>Select Favorite Genres</p>
      <div id='example-3'>
        <input type="checkbox" id="1" value="멜로/로맨스" v-model="like_genres">
        <label for="jack">멜로/로맨스</label>
        <input type="checkbox" id="john" value="공포" v-model="like_genres">
        <label for="john">공포</label>
        <input type="checkbox" id="mike" value="등등" v-model="like_genres">
        <label for="mike">등등</label>
        <br>
        <span>체크장르: {{ like_genres }}</span>
    </div>
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
      like_genres:[],
    }
  },
  methods: {
    ...mapActions(["signup"])
  }
}

</script>