<template>
  <div class="col-3 my-3">
    <link
      rel="stylesheet"
      href="https://use.fontawesome.com/releases/v5.2.0/css/all.css"
      integrity="sha384-hWVjflwFxL6sNzntih27bfxkr27PmbbK/iSvJ+a4+0owXq79v+lsFkW54bOGbiDQ"
      crossorigin="anonymous"
    />
    <button class="btn btn-sm btn-dark" type="submit">
      <img
        @click="onSelectMovie"
        class="movie--poster my-3"
        :src="movie.poster_url"
        :alt="movie.id"
      />
    </button>
    <div>
      <b-modal
        hide-footer
        v-model="show"
        id="movie-modal"
        size="lg"
        :title="`${movie.title}`"
        :header-bg-variant="headerBgVariant"
        :header-text-variant="headerTextVariant"
        :body-bg-variant="bodyBgVariant"
        :body-text-variant="bodyTextVariant"
        :footer-bg-variant="footerBgVariant"
        :footer-text-variant="footerTextVariant"
      >
        <img :src="movie.poster_url" alt="movie poster" id="movie-detail-image" />
        <h5>감독 {{movie.director}}</h5>
        <h5>배우 {{movie.actor}}</h5>
        <h5>{{movie.grade}}</h5>
        <h5>{{movie.open_date}} 개봉</h5>
        <h5>{{movie.running_time}}분</h5>
        <!-- like 구현 -->

        <br />
        <span>{{movie.description}}</span>
        <!-- comment 구현 -->
        <hr />
        <!-- 별점 표현하기 -->
        <div v-if="this.$store.state.userInfo !== null">
          <h4 id="reviews">Reviews</h4>
          <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet" />
          <span>평점</span>
          <!-- <input type="number" v-model="score" max="5" min="0" id="score" /> -->
          <select v-model="score" id="score">
            <option>5</option>
            <option>4</option>
            <option>3</option>
            <option>2</option>
            <option>1</option>
          </select>

          <br />
          <br />

          <div class="input-group">
            <textarea class="form-control" aria-label="With textarea"
            name="inputContent"
            v-model="content"
            id="content"></textarea>
          </div>
          
          <!-- comment  작성하기 -->
          <b-button @click="onSubmit(movie.id)" class="btn btn-dark" id="wb">작성</b-button>
          <CommentList :comments="movie.comments" />
          <router-view :key="$route.fullPath" />
        </div>
      </b-modal>
    </div>
    <h3 id="movie-title">
      {{ movie.title }}
      <div v-if="this.$store.state.userInfo !== null">
        <div v-if="movie.liked_users.includes(this.$store.state.userInfo.userpk)">
          <i class="fas fa-heart" @click="removelikes(movie.id)"></i>
        </div>
        <div v-else>
          <i class="far fa-heart" @click="addlikes(movie.id)"></i>
        </div>
      </div>
    </h3>
    <br />
  </div>
</template>

<script>
import axios from "axios";
// import router from "@/router";
import { mapState } from "vuex";
import CommentList from "@/components/CommentList.vue";

export default {
  name: "MovieListItem",
  components: {
    CommentList
  },
  data() {
    return {
      liked_users: this.movie.liked_users,
      content: "",
      score: 0,
      // modal관련
      show: false,
      variants: ["light", "dark"],
      headerBgVariant: "dark",
      headerTextVariant: "light",
      bodyBgVariant: "dark",
      bodyTextVariant: "light",
      footerBgVariant: "dark",
      footerTextVariant: "dark"
    };
  },
  computed: {
    ...mapState(["userInfo"])
  },
  props: {
    movie: {
      type: Object,
      required: true
    }
  },
  methods: {
    onSelectMovie: function(movie) {
      this.selectMovie = movie.target.alt;
      this.show = true;
    },
    onSubmit(moviepk) {
      // comment의 작성 버튼을 눌렀을 때
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      const commentObj = {
        content: this.content,
        score: parseInt(this.score),
        user_id: this.$store.state.userInfo.userpk
      };
      axios
        .post(`${SERVER_IP}/api/v1/commentcreate/${moviepk}/`, commentObj)
        .then(() => {
          this.$router.go();
          // 새로 넣은 두 줄
        })
        .catch(error => {
          console.log(error);
        });
      this.content = "";
      this.score = 0;
    },
    addlikes: function(moviepk) {
      this.liked_users.push(this.$store.state.userInfo.userpk);
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      const data = {
        title: this.movie.title,
        poster_url: this.movie.poster_url,
        director: this.movie.director,
        actor: this.movie.actor,
        description: this.movie.description,
        grade: this.movie.grade,
        running_time: this.movie.running_time,
        naver_score: this.movie.naver_score,
        open_date: this.movie.open_date,
        audience: this.movie.audience,
        genre: this.movie.genre,
        liked_users: this.liked_users
      };
      axios
        .put(`${SERVER_IP}/api/v1/moviedetail/${moviepk}/`, data)
        .then(() => {})
        .catch(error => {
          console.error(error);
        });
    },
    removelikes: function(moviepk) {
      this.liked_users.pop(this.$store.state.userInfo.userpk);
      console.log(this.liked_users);
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      const data = {
        title: this.movie.title,
        poster_url: this.movie.poster_url,
        director: this.movie.director,
        actor: this.movie.actor,
        description: this.movie.description,
        grade: this.movie.grade,
        running_time: this.movie.running_time,
        naver_score: this.movie.naver_score,
        open_date: this.movie.open_date,
        audience: this.movie.audience,
        genre: this.movie.genre,
        liked_users: this.liked_users
      };
      axios
        .put(`${SERVER_IP}/api/v1/moviedetail/${moviepk}/`, data)
        .then(response => {
          console.log(response);
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>

<style>
#movie-detail-image {
  margin: 15px;
}
#reviews {
  font-family: "Jua", sans-serif;
}
#score {
  background-color: #343a40;
  color: white;
}
#content {
  background-color: #343a40;
  color: white;
}
.movie--poster {
  width: 210px;
}
#movie-title {
  font-size: 21px;
  text-align: center;
}
#movie-detail-image {
  width: 300px;
  float: left;
  margin-right: 20px;
}
/* 이미지에 마우스 올리면 확대 */
.btn img {
  -webkit-transform: scale(1);
  -moz-transform: scale(1);
  -ms-transform: scale(1);
  -o-transform: scale(1);
  transform: scale(1);
  -webkit-transition: 0.3s;
  -moz-transition: 0.3s;
  -ms-transition: 0.3s;
  -o-transition: 0.3s;
  transition: 0.3s;
}
.btn:hover img {
  -webkit-transform: scale(1.2);
  -moz-transform: scale(1.2);
  -ms-transform: scale(1.2);
  -o-transform: scale(1.2);
  transform: scale(1.2);
}
</style>