
<template>
  <div class="col-3 my-3">
    <img @click="onSelectMovie" class="movie--poster my-3" :src="movie.poster_url" :alt="movie.id" />
    <h3 id="movie-title">{{ movie.title }}</h3>
    <button @click="onDelete" type="submit">삭제</button>
    <br />
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "MovieListItem",
  data() {
    return {};
  },
  computed: {
    ...mapState(["userInfo"])
  },
  props: {
    movie: {
      type: Object,
      required: true
    }
  },
  methods: {
    onDelete() {

    }
  }
};
</script>

<style>
.movie--poster {
  width: 210px;
}
#movie-title {
  font-size: 21px;
  text-align: center;
}
#movie-detail-image {
  width: 400px;
  float: left;
  margin-right: 20px;
}
</style>