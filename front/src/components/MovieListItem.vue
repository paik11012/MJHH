
<template>
  <div class="col-3 my-3">
    <img @click="onSelectMovie" class="movie--poster my-3" :src="movie.poster_url" :alt="movie.id">
    
    <h3 id="movie-title">{{ movie.title }}</h3>
    <br>

    <!-- <button class="btn btn-primary" data-toggle="modal" :data-target="`#movie-${movie.id}`">
      영화 정보 상세보기
    </button> -->
      <!-- <movielistitemmodal :movie="movie" /> -->
  </div>
</template>

<script>
export default {
  name: 'MovieListItem',
  props: {
    movie: {
      type: Object,
      required: true
    }
  },
  components: {
  },
  methods: {
    onSelectMovie: function(movie) {
      console.log(movie.target.alt)
      this.selectMovie = movie.target.alt
    }
  }
}
</script>

<style>
.movie--poster {
  width: 200px;
}
#movie-title {
  font-size: 21px
}
</style>