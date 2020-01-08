<template>
  <div class="col-3 my-3">
    <button class="btn btn-dark" type="submit">
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
        <button @click="onModify(movie.id)" class="btn btn-danger" type="submit" id="modi">수정</button>
        <hr />
        <h5>제목</h5>
        <input type="text" v-model="title" id="title" />
        <h5>포스터url</h5>
        <input type="text" v-model="poster_url" id="poster_url" />
        <div>
          <h5>감독</h5>
          <input type="text" v-model="director" id="director" />
          <h5>배우</h5>
          <input type="text" v-model="actor" id="actor" />
          <h5>개봉일</h5>
          <input type="text" v-model="open_date" id="open_date" />
          <h5>상영시간</h5>
          <input type="text" v-model="running_time" id="running_time" />
          <h5>장르</h5>
          <input type="text" v-model="genre" id="genre" />
          <hr />
          <textarea name id cols="40" v-model="movie.description" rows="12"></textarea>
        </div>
        <br />

        <!-- like 구현 -->
        <!-- comment 구현 -->
        <br />

        <br />
        <h4>Reviews</h4>
        <span>
          평점
          <input type="number" v-model="score" max="10" min="0" id="score" />
        </span>
        <textarea name="inputContent" v-model="content" cols="100" rows="3" id="content"></textarea>
        <!-- 쓴 커멘트 보여주기 -->
      </b-modal>
    </div>
    <h3 id="movie-title">{{ movie.title }}</h3>
    <button @click="onDelete(movie.id)" class="btn btn-warning" type="submit">삭제</button>

    <br />
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "MovieListItem",
  data() {
    return {
      title: this.movie.title,
      director: this.movie.director,
      poster_url: this.movie.poster_url,
      actor: this.movie.actor,
      running_time: this.movie.running_time,
      grade: this.movie.grade,
      description: this.movie.description,
      open_date: this.movie.open_date,
      genre: this.movie.genre,

      content: "",
      contentList: [],
      score: 0,
      scoreList: [],
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
  props: {
    movie: {
      type: Object,
      required: true
    }
  },
  components: {},
  methods: {
    onSelectMovie: function(movie) {
      this.selectMovie = movie.target.alt;
      this.show = true;
    },
    onDelete(moviepk) {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      axios
        .delete(`${SERVER_IP}/api/v1/moviedetail/${moviepk}/`)
        .then(response => {
          console.log(response);
          this.$router.go();
        })
        .catch(error => {
          console.error(error);
        });
    },
    // 수정하는 로직!!
    onModify(moviepk) {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      const data = {
        title: this.title,
        poster_url: this.poster_url,
        director: this.director,
        actor: this.actor,
        description: this.description,
        grade: this.grade,
        running_time: this.running_time,
        naver_score: this.movie.naver_score,
        open_date: this.open_date,
        audience: this.movie.audience,
        genre: this.genre
      };
      console.log(moviepk);
      console.log(data);
      axios
        .put(`${SERVER_IP}/api/v1/moviedetail/${moviepk}/`, data)
        .then(response => {
          console.log(response);
          this.$router.go();
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>

<style>
#modi {
  color: black;
}
#movie-modal {
  font-family: "Nanum Gothic", monospace;
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
  width: 45%;
  float: left;
  margin-right: 20px;
}
</style>