<template>
  <div v-if="movie">
		<div  class="details">
			<h4 v-html="movie.title"></h4>
			<h1>Movie Detail</h1>
		</div>
	</div>
</template>

<script>
export default {
	name: "MovieDetail",
	props: {
		movie: {
			type: Object,
		}
	},
	// computed: {
	// 	movieDetail: function() {
	// 		const movieId = this.movie.id.movieId
	// 		return `https:localhost:8080/moviedetail/${$movieId}/`
	// 		// movie 이미지랑 다른것 다 보여주기
	// 	}
	// }
};
</script>



<style>
</style>