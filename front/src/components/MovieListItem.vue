
<template>
  <div class="col-3 my-3">
    <img @click="onSelectMovie" class="movie--poster my-3" :src="movie.poster_url" :alt="movie.id" />

    <div>
      <b-modal
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
        <h5>감독 {{movie.director}}</h5>
        <h5>배우 {{movie.actor}}</h5>
        <h5>{{movie.running_time}}분</h5>
        <h5>{{movie.grade}}</h5>
        <h5>{{movie.open_date}}</h5>
        <!-- like 구현 -->

        <br />
        <span>{{movie.description}}</span>
        <!-- comment 구현 -->
        <br />
        <br />
        <h4>Reviews</h4>
        <span>점수 <input v-model="score" type="number" name="score" id="score" max=10 min=0></span>
        <textarea v-model="content" name="textarea" id="content" cols="100" rows="3"></textarea>
        <b-button class="btn btn-dark" size="sm">작성</b-button>
        <!-- <span>{{this.state.userInfo}}</span> -->
        <!-- 쓴 커멘트 보여주기 -->
        

        
      </b-modal>
    </div>
    <h3 id="movie-title">{{ movie.title }}</h3>
    <br />
  </div>
</template>

<script>
export default {
  name: "MovieListItem",

  data() {
    return {
      content:'',
      score:0,
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
    onSubmit() {
      this.$emit('createReview', this.content)
      this.content=''
    }
  }
};
</script>

<style>
#score{
  background-color: #343A40;
  color:white
}
#content{
  background-color: #343A40;
  color:white

}
.movie--poster {
  width: 210px;
}
#movie-title {
  font-size: 21px;
}
#movie-detail-image {
  width: 400px;
  float: left;
  margin-right: 20px;
}
</style>