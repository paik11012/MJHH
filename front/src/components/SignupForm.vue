<template>
  <div class="formContainer">
    <form class="login-box">
      <br>
      <h2>Sign Up</h2>
      <br>
      
      <img src="http://file.mk.co.kr/meet/neds/2019/11/image_readtop_2019_983208_15747235963989824.jpg" alt="cat" width="200px">
      <br>
      <br>
      <span>ID    </span><input type="text" v-model="username" name="username" placeholder="ID를 입력하세요" />
      <br>
      <br>
      <span>Email    </span>
      <input type="text" v-model="email" name="useremail" placeholder="이메일을 입력하세요" />
      <br>
      <br>
      <span>Password    </span>
      <input type="password" v-model="password1" name="userpassword" placeholder="비밀번호를 입력하세요" />
      <br>
      <br>
      <span>Confirm Password    </span>
      <input type="password" v-model="password2" name="userpassword" placeholder="비밀번호를 입력하세요" />
      <!-- <p>Select Favorite Genres(장르를 세 개 체크해 주세요)</p>  -->
      <p></p>
      <!-- <div id="like_genres_chk">
        <input type="checkbox" id="1" value="드라마" v-model="like_genres" />
        <label for="드라마">멜로/로맨스 </label>
        <input type="checkbox" id="2" value="판타지" v-model="like_genres" />
        <label for="판타지">판타지 </label>
        <input type="checkbox" id="4" value="공포" v-model="like_genres" />
        <label for="공포">공포 </label>
        <input type="checkbox" id="6" value="모험" v-model="like_genres" />
        <label for="모험">모험 </label>
        <input type="checkbox" id="7" value="스릴러" v-model="like_genres" />
        <label for="스릴러">스릴러 </label>
        <input type="checkbox" id="8" value="느와르" v-model="like_genres" />
        <label for="느와르">느와르 </label>
        <input type="checkbox" id="10" value="다큐멘터리" v-model="like_genres" />
        <label for="다큐멘터리">다큐멘터리 </label>
        <input type="checkbox" id="11" value="코미디" v-model="like_genres" />
        <label for="코미디">코미디 </label>
        <br>
        <input type="checkbox" id="12" value="가족" v-model="like_genres" />
        <label for="가족">가족 </label>
        <input type="checkbox" id="13" value="미스터리" v-model="like_genres" />
        <label for="미스터리">미스터리 </label>
        <input type="checkbox" id="14" value="전쟁" v-model="like_genres" />
        <label for="전쟁">전쟁 </label>
        <input type="checkbox" id="15" value="애니메이션" v-model="like_genres" />
        <label for="애니메이션">애니메이션 </label>
        <input type="checkbox" id="16" value="범죄" v-model="like_genres" />
        <label for="범죄">범죄 </label>
        <input type="checkbox" id="17" value="뮤지컬" v-model="like_genres" />
        <label for="뮤지컬">뮤지컬 </label>
        <input type="checkbox" id="18" value="SF" v-model="like_genres" />
        <label for="SF">SF </label>
        <input type="checkbox" id="19" value="액션" v-model="like_genres" />
        <label for="액션">액션 </label>
        <input type="checkbox" id="20" value="무협" v-model="like_genres" />
        <label for="무협">무협 </label>
        <br />
        <span>장르: {{ like_genres }}</span>
      </div> -->
      <br />
    </form>
    <br />
    <div class="login-btn">
      <input
        type="submit"
        class="btn btn-primary"
        name="submit"
        @click="signup({username, email, password1, password2, liked_genres}),login({username, password})"
        value="회원가입"
      />
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  data() {
    return {
      username: null,
      email: null,
      password1: null,
      password2: null,
      like_genres: []
    };
  },
  methods: {
    ...mapActions(["signup"]),
    ...mapActions(["login"])
  }
};
</script>
<style>

</style>