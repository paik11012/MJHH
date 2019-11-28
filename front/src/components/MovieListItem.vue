
<template>
  <div class="col-3 my-3">
    <button class="btn btn-dark" type="submit"><img @click="onSelectMovie" class="movie--poster my-3" :src="movie.poster_url" :alt="movie.id" /></button>
    <div>
      <b-modal
        hide-footer
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
        <h5>{{movie.grade}}</h5>
        <h5>{{movie.open_date}} 개봉</h5>
        <h5>{{movie.running_time}}분</h5>
        <!-- like 구현 -->

        <br />
        <span>{{movie.description}}</span>
        <!-- comment 구현 -->
        <br />
        <br />
        <h4>Reviews</h4>
        <span>평점 <input type="number" v-model="score" max=10 min=0 id="score"></span>
        <textarea  name="inputContent" v-model="content" cols="100" rows="3" id="content"></textarea>
        <b-button @click="onSubmit" class="btn btn-dark" size="sm">작성</b-button>
        <!-- <span>{{userInfo.username}}</span> -->
        <!-- 쓴 커멘트 보여주기 -->
        
      </b-modal>
    </div>
    <h3 id="movie-title">{{ movie.title }}</h3>
    <br />
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "MovieListItem",


  data() {
    return {
      content:'',
      contentList: [],
      score: 0,
      scoreList: [],
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
  computed: {
    ...mapState([
      "userInfo"
    ])
 
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
      // this.score = score.value
      this.scoreList.push(this.score)
      this.contentList.push(this.content)
      // 여기 있는 정보를 sqlite에 저장해야 함
      // 위 컴포넌트에서 가져오기(user, content, score)
      // console.log(this.name)
      this.content=''
      this.score=0
    },
  }
};
</script>

<style>
#movie-modal{
  font-family: 'Stylish', sans-serif;
}
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
  text-align: center
}
#movie-detail-image {
  width: 400px;
  float: left;
  margin-right: 20px;
}
</style>