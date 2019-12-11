<template>
  <div class="movie-list">
    <h1>영화 목록</h1>
    <h3>장르 선택</h3>
    <select class="form-control" v-model="genreid" id="select-genre">
      <option value=0>전체</option>
      <option v-for="genre in genres" v-bind:key="genre.id" :value="genre.id">{{genre.name}}</option>
    </select>
    <br>
    <div>
      <b-button v-b-modal.modal-1 class="btn btn-success">추가</b-button>
      <b-modal hide-footer id="modal-1" title="Add Movie"
        :header-bg-variant="headerBgVariant"
        :header-text-variant="headerTextVariant"
        :body-bg-variant="bodyBgVariant"
        :body-text-variant="bodyTextVariant"
        :footer-bg-variant="footerBgVariant"
        :footer-text-variant="footerTextVariant"
      >
        제목 <input type="text" v-model="title" id="title"> <br>
        포스터 URL <input type="text" v-model="poster_url" id="poster_url"><br>
        감독 <input type="text" v-model="director" id="director"><br>
        배우 <input type="text" v-model="actor" id="actor"><br>
        등급 <input type="text" v-model="grade" id="grade"><br>
        네이버 평점 <input type="number" step="0.01" v-model="naver_score" id="naver_score"><br>
        관객 <input type="number" v-model="audience" id="audience"><br>
        개봉일 <input type="date" v-model="open_date" id="open_date"><br>
        상영시간 <input type="number" v-model="running_time" id="running_time"><br>
        장르 <input type="number" v-model="genre" id="genre"><br>
        <p>줄거리</p>
        <textarea name="" id="" cols="40" v-model="description" rows="12"></textarea>&nbsp;&nbsp;
        <button @click="addMovie" class="btn btn-success">추가</button>
      </b-modal>
    </div>
    <div class="row mt-5">
      <MovieListItem v-for="movie in movieList" :movie="movie" :key="movie.id" />
    </div>
    <hr>
    <AdminUser />
  </div>
</template>

<script>
// import axios from "axios";
import { mapState } from "vuex";
import axios from "axios";
import router from "@/router";
import MovieListItem from "@/components/MovieListItemAdmin.vue";
import AdminUser from "@/components/AdminUser.vue"


export default {
  name: "MovieList",
  components: {
    MovieListItem,
    AdminUser
  },
  data() {
    return {
      genreid: 0,
      title: '',
      director: '',
      poster_url: '',
      actor: '',
      running_time:'',
      grade: '',
      audience: 0,
      naver_score: 0,
      description: '',
      open_date:'',
      genre: 0,

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
    movies: {
      type: Array,
      required: true
    },
    genres: {
      type: Array,
      required: true
    }
  },
  methods: {
    addMovie: function(){
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      const movie = {
        "title": this.title,
        "poster_url": this.poster_url,
        "director": this.director,
        "actor": this.actor,
        "description": this.description,
        "grade": this.grade,
        "running_time": this.running_time,
        "naver_score" : this.naver_score,
        "open_date": this.open_date,
        "audience": this.audience,
        "genre": this.genre
      }
      axios.post(`${SERVER_IP}/api/v1/create/`, movie)
        .then(response=>{
          console.log(response)
          router.push('/')
        })
        .catch(error=>{
          console.log(error)
        })
    }
  },
  computed: {
    ...mapState([
      "userInfo"
    ]),
    movieList: function() {
      if (this.genreid != 0) {
        const genre = this.genres.filter(
          genre => genre.id === this.genreid
        );
        return this.movies.filter(movie => movie.genre === genre[0].id);
      } else {
        return this.movies;
      }
    }
  },
};
</script>

<style>
#select-genre {
  background-color:#343A40 ;
  color: white
}

#modal-1 {
  font-family: "Stylish", sans-serif;
}

</style>