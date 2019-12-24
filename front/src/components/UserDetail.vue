<template>
  <div class="user" id="all">
    <br />
    <h3 id="one">My Info</h3>
    <br />
    <img
      width="300px"
      src="http://file.mk.co.kr/meet/neds/2019/11/image_readtop_2019_983208_15747235963989824.jpg"
      alt
    />
    <br />
    <br />
    <h4>ID: {{ username }}</h4>
    <br />
    <h4>Email: {{ useremail }}</h4>
    <hr />
    <h3>Liked Movies</h3>
    <!-- <b-carousel
      id="carousel-fade"
      style="text-shadow: 0px 0px 2px #000"
      fade
      indicators
      img-width="1024"
     img-height="480"
    >
      <div v-for="movie in liked_movies" :key="movie.id">
        <b-carousel-slide :caption="movie.title" :img-src="movie.poster_url" id="like_movie"> 
        </b-carousel-slide>
      </div>
    </b-carousel>-->
    <div>
      <b-carousel
        id="carousel-fade"
        style="text-shadow: 0px 0px 2px #000"
        fade
        indicators
      >
      <div v-for="movie in liked_movies" :key="movie.id">
        <b-carousel-slide :img-src="movie.poster_url" id="like_movie"> 
          <!-- :caption="movie.title"  -->
        </b-carousel-slide>
      </div>
      </b-carousel>
    </div>

    <hr />
    <h3>Comments</h3>
    <div v-for="comment in comments" :key="comment.id">
      {{ comment.content }}
      <br />
    </div>
    <br />

    <!-- <h3>Liked Genres</h3>
    <p>{{ user.liked_genres }}</p>-->
    <!-- <hr />
    <h3>Followers</h3>
    <div v-for="follower in followers" :key="follower.id">{{ follower }}</div>-->
    <!-- <div v-if="user === this.$store.state.userInfo.userpk"> -->
    <!-- <div>
        <h3>Select Favorite Genres</h3>
        <div id="liked_genres_chk">
          <input type="checkbox" id="1" value="드라마" v-model="liked_genres" />
          <label for="드라마">멜로/로맨스</label>
          <input type="checkbox" id="2" value="판타지" v-model="liked_genres" />
          <label for="판타지">판타지</label>
          <input type="checkbox" id="4" value="공포" v-model="liked_genres" />
          <label for="공포">공포</label>
          <input type="checkbox" id="6" value="모험" v-model="liked_genres" />
          <label for="모험">모험</label>
          <input type="checkbox" id="7" value="스릴러" v-model="liked_genres" />
          <label for="스릴러">스릴러</label>
          <input type="checkbox" id="8" value="느와르" v-model="liked_genres" />
          <label for="느와르">느와르</label>
          <input type="checkbox" id="10" value="다큐멘터리" v-model="liked_genres" />
          <label for="다큐멘터리">다큐멘터리</label>
          <input type="checkbox" id="11" value="코미디" v-model="liked_genres" />
          <label for="코미디">코미디</label>
          <br />
          <input type="checkbox" id="12" value="가족" v-model="liked_genres" />
          <label for="가족">가족</label>
          <input type="checkbox" id="13" value="미스터리" v-model="liked_genres" />
          <label for="미스터리">미스터리</label>
          <input type="checkbox" id="14" value="전쟁" v-model="liked_genres" />
          <label for="전쟁">전쟁</label>
          <input type="checkbox" id="15" value="애니메이션" v-model="liked_genres" />
          <label for="애니메이션">애니메이션</label>
          <input type="checkbox" id="16" value="범죄" v-model="liked_genres" />
          <label for="범죄">범죄</label>
          <input type="checkbox" id="17" value="뮤지컬" v-model="liked_genres" />
          <label for="뮤지컬">뮤지컬</label>
          <input type="checkbox" id="18" value="SF" v-model="liked_genres" />
          <label for="SF">SF</label>
          <input type="checkbox" id="19" value="액션" v-model="liked_genres" />
          <label for="액션">액션</label>
          <input type="checkbox" id="20" value="무협" v-model="liked_genres" />
          <label for="무협">무협</label>
          <br />
          <span>장르: {{ liked_genres }}</span>
          <button @click="checkgenre" class="btn" id="sub">Submit</button>
        </div>
    </div>-->
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "UserDetail",
  el: "#liked_genres_chk",
  data() {
    return {
      user: this.$route.params.id,
      username: "",
      useremail: "",
      comments: [],
      followers: [],
      liked_movies: [],
      choose_genres: false,
      liked_genres: []
    };
  },
  methods: {
    getuserinfo: function() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      axios
        .get(`${SERVER_IP}/api/v1/userdetail/${this.user}`)
        .then(response => {
          console.log(response);
          this.username = response.data.username;
          this.useremail = response.data.email;
          this.comments = response.data.comments;
          this.followers = response.data.followers;
          this.liked_movies = response.data.liked_movies;
          this.liked_genres = response.data.liked_genres;
        });
    }
    // checkgenre: function() {
    //   if (this.choose_genres === false) {
    //     this.choose_genres = true;
    //   } else {
    //     this.user.liked_genres = this.liked_genres;
    //     this.choose_genres = false;
    //   }
    // }
  },
  mounted() {
    this.getuserinfo();
  }
};
</script>

<style>
#all {
  font-family: "Jua", sans-serif;
}
.img{
  width: auto; height: 100%; }

#like_movie {
  max-height: 35%;
  max-width: 35%;
  margin-left: 33%  
}
#fg {
  color: white;
}
#sub {
  color: white;
}
</style>