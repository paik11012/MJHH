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
      <b-modal id="modal-1" title="Add Movie"
        :header-bg-variant="headerBgVariant"
        :header-text-variant="headerTextVariant"
        :body-bg-variant="bodyBgVariant"
        :body-text-variant="bodyTextVariant"
        :footer-bg-variant="footerBgVariant"
        :footer-text-variant="footerTextVariant"
      >
        <!-- <button @click="onModify(movie.id)" class="btn btn-danger" type="submit" id="modi">수정</button> -->
        제목: <input type="text" v-model="title" id="title"> <br>
        포스터url: <input type="text" v-model="poster_url" id="poster_url"><br>
        감독: <input type="text" v-model="director" id="director"><br>
        배우: <input type="text" v-model="actor" id="actor"><br>
        개봉일: <input type="text" v-model="open_date" id="open_date"><br>
        상영시간: <input type="text" v-model="running_time" id="running_time"><br>
        장르: <input type="text" v-model="genre" id="genre"><br>
        상세정보: <textarea name="" id="" cols="40" v-model="description" rows="12"></textarea>
      </b-modal>
    </div>
    <div class="row mt-5">
      <MovieListItem v-for="movie in movieList" :movie="movie" :key="movie.id" />
    </div>
  </div>
</template>

<script>
// import axios from "axios";
import { mapState } from "vuex";
import MovieListItem from "@/components/MovieListItemAdmin.vue";


export default {
  name: "MovieList",
  components: {
    MovieListItem
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
      description: '',
      open_date:'',
      genre:'',
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
  // methdos: {
  //   addMovie: function(){
  //     const SERVER_IP = process.env.VUE_APP_SERVER_IP
  //     axios.post(`${SERVER_IP}/api/v1/create/`)
  //       .then(response=>{

  //       })
  //   }
  // },
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

</style>