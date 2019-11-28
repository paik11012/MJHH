<template>
  <div class="home">
    <MovieList :movies="movies" :genres="genres"/>
  </div>
</template>

<script>
import axios from 'axios'
import MovieList from '@/components/MovieList.vue'

export default {
  name: 'home',
  components: {
    MovieList
  },
  data() {
    return {
      movies: [],
      genres: []
    }
  },
  methods: {
    getMovies: function(){
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      axios.get(`${SERVER_IP}/api/v1/movielist/`)
        .then(response=>{
          // console.log(response)
          this.movies = response.data
        })
        .catch(error=>{
          console.log(error)
        })
    },
    getGenres: function(){
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      axios.get(`${SERVER_IP}/api/v1/genrelist/`)
        .then(response=>{
          // console.log(response)
          this.genres = response.data
        })
        .catch(error=>{
          console.log(error)
        })
    }
  },
  mounted() {
    this.getMovies()
    this.getGenres()
  }
}
</script>
