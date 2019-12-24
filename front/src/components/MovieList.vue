<template>
  <div class="movie-list">
    <br />
    <h1 id="list">영화 목록</h1>
    <h3 id="genre">장르 선택</h3>
    <select class="form-control" v-model="genreid" id="select-genre">
      <option value="0">전체</option>
      <option v-for="genre in genres" v-bind:key="genre.id" :value="genre.id">{{genre.name}}</option>
    </select>
    <div class="container">
      <div class="row">
        <MovieListItem
          v-for="movie in movieList"
          :movie="movie"
          :key="movie.id"
          id="one_item"
          class="col-md-3"
        />
      </div>
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
    ...mapState(["userInfo"]),
    movieList: function() {
      if (this.genreid != 0) {
        const genre = this.genres.filter(genre => genre.id === this.genreid);
        return this.movies.filter(movie => movie.genre === genre[0].id);
      } else {
        return this.movies;
      }
    }
  }
};
</script>

<style>
#list,
#genre {
  font-family: "Jua", sans-serif;
}
#select-genre {
  background-color: #343a40;
  color: white;
}
</style>