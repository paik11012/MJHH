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
        <br />
        <h5>감독 {{movie.director}}</h5>
        <h5>배우 {{movie.actor}}</h5>
        <h5>{{movie.grade}}</h5>
        <h5>{{movie.open_date}} 개봉</h5>
        <h5>{{movie.running_time}}분</h5>
        <!-- like 구현 -->

        <br />
        <span>{{movie.description}}</span>
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
    <button @click="onModify(movie.id)" class="btn btn-danger" type="submit">수정</button>
    <br />
  </div>
</template>

<script>
import axios from "axios";
import router from "@/router";
export default {
  name: "MovieListItem",
  data() {
    return {
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
      // console.log(movie.target.alt);
      this.selectMovie = movie.target.alt;
      this.show = true;
    },
    onDelete(moviepk) {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      axios
        .delete(`${SERVER_IP}/api/v1/moviedetail/${moviepk}/`)
        .then(response => {
          console.log(response);
          router.push("/");
        })
        .catch(error => {
          console.error(error);
        });
    },
    // 수정하는 로직!!
    onModify(moviepk) {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      axios
        .put(`${SERVER_IP}/api/v1/moviedetail/${moviepk}/`)
        .then(response => {
          console.log(response);
          router.push("/");
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>

<style>
#movie-modal {
  font-family: "Stylish", sans-serif;
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
  width: 400px;
  float: left;
  margin-right: 20px;
}
</style>