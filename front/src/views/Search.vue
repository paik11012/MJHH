<template>
  <div class="search">
    <h1>검색 결과</h1>
    <div class="row mt-5" v-if="searchResult.length >= 1">
      <MovieListItem v-for="movie in searchResult" :movie="movie" :key="movie.id" />
    </div>
    <div id="result" class="row mt-5" v-else>
      <h2>검색 결과를 찾을 수 없습니다!</h2>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import MovieListItem from "@/components/MovieListItem.vue";

export default {
name: 'Search',
components: {
  MovieListItem
},
data() {
  return {
    movies: [],
    genres: [],
    keyword: this.$route.params.name,
  }
},
methods: {
  getMovies: function(){
    const SERVER_IP = process.env.VUE_APP_SERVER_IP
    axios.get(`${SERVER_IP}/api/v1/movielist/`)
      .then(response=>{
        this.movies = response.data
      })
      .catch(()=>{
        alert('페이지를 로딩하지 못했습니다!')
      })
  },
  getGenres: function(){
    const SERVER_IP = process.env.VUE_APP_SERVER_IP
    axios.get(`${SERVER_IP}/api/v1/genrelist/`)
      .then(response=>{
        this.genres = response.data
      })
      .catch(()=>{
        alert('페이지를 로딩하지 못했습니다!')
      })
  }
},
computed: {
  searchResult: function() {
    let res = []
    for (const movie of this.movies){
      if (movie.actor.includes(this.keyword)){
        res.push(movie)
      } else if (movie.description.includes(this.keyword)){
        res.push(movie)
      } else if (movie.director.includes(this.keyword)){
        res.push(movie)
      } else if (movie.title.includes(this.keyword)){
        res.push(movie)
      }
    }
    for (const genre of this.genres){
      if (genre.name.includes(this.keyword)){
        const genre = this.genres.filter(
          genre => genre.name.includes(this.keyword)
        );
        res = res.concat(this.movies.filter(movie => movie.genre === genre[0].id))
      }
    }
    return res
  }
},
mounted() {
  this.getMovies()
  this.getGenres()
}
}
</script>

<style>
#result{
  text-align: center;
}
</style>