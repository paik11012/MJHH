<template>
  <div class="modify-form">
    <div class="form-group">
      <input type="text" id="director" class="form-control" value="{{director}}" v-model="director" />
    </div>
    <div class="form-group">
      <input type="text" id="actor" value="{{director}}" class="form-control" v-model="actor" />
    </div>
    <div class="form-group">
      <input type="number" id="grade" class="form-control" v-model="grade" />
    </div>
    <div class="form-group">
      <input type="date" id="open_date" class="form-control" v-model="open_date" />
    </div>
    <div class="form-group">
      <input type="number" id="running_time" class="form-control" v-model="running_time" />
    </div>
    <div class="form-group">
      <input type="text" id="description" class="form-control" v-model="description"  />
    </div>
    <button class="btn btn-warning" @click="modify({director, actor, grade, open_date, running_time, description})">수정하기</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      director: movie.director,
      actor: movie.actor,
      grade: movie.grade,
      open_date: movie.open_date,
      running_time: movie.running_time,
      description: movie.description
    };
  }
};
</script>

<style>
</style>