<template>
  <div class="comment">
    <ul>
      <div v-for="comment in comments" :key="comment.id">
        <li>
          <CommentListItem :comment="comment"/>
        </li>
      </div>
    </ul>
  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem.vue'

export default {
  name: "CommentList",
  components:{
    CommentListItem
  },
  props: {
    comments: {
      type: Array,
      required: true
    }
  },
};
</script>

<style>
</style>