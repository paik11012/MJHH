<template>
  <div class="movie-list">
    <!-- <h1>영화 목록</h1>
    <h2>장르 선택</h2>
    <select class="form-control" v-model="genrename">
      <option>전체</option>
      <option v-for="genre in genres" v-bind:key="genre.id">{{genre.name}}</option>
    </select>
    <div class="row mt-5">
      <movielistitem v-for="movie in movieList" :movie="movie" :key="movie.id" />
    </div> -->
  </div>
</template>

<script>
export default {
  name: "MovieList",
  props: {
    movies: {
      type: Array,
      required: true,
    }
  },
}
</script>

<style>

</style>