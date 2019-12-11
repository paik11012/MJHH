<template>
  <div class="movie-list">
    <br>
    <h1>영화 목록</h1>
    <h3>장르 선택</h3>
    <select class="form-control" v-model="genreid" id="select-genre">
      <option value=0>전체</option>
      <option v-for="genre in genres" v-bind:key="genre.id" :value="genre.id">{{genre.name}}</option>
    </select>
    <div class="row mt-5">
      <MovieListItem v-for="movie in movieList" :movie="movie" :key="movie.id" />
    </div>
  </div>
  
</template>

<script>
import { mapState } from "vuex";
import MovieListItem from "@/components/MovieListItem.vue";


export default {
  name: "MovieList",
  components: {
    MovieListItem
  },
  data() {

    return {
      genreid: 0
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