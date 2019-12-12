<template>
  <div class="commentitem">
    <span v-for="user in userlist" :key="user.id">
      <span v-if="user.id === comment.user_id">
        {{ user.username }}
        <br />
        <div v-if="commentupdate">
          score:
          <!-- <input type="number" v-model="modifyscore" max="10" min="0" /> -->
          <select v-model="modifyscore" id="score">
            <option>5</option>
            <option>4</option>
            <option>3</option>
            <option>2</option>
            <option>1</option>
            <option>0</option>
          </select>
          content:
          <input type="text" v-model="modifycontent" />
        </div>
        <div v-else>
          <div v-if="comment.score==5">
            <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet"> 
            <i class="material-icons">star</i> 
            <i class="material-icons">star</i> 
            <i class="material-icons">star</i> 
            <i class="material-icons">star</i> 
            <i class="material-icons">star</i> {{ comment.content }}
          </div>
          <div v-else-if="comment.score==4">
            <i class="material-icons">star</i> 
            <i class="material-icons">star</i> 
            <i class="material-icons">star</i> 
            <i class="material-icons">star</i> 
            <i class="material-icons">star_border</i> {{ comment.content }}
          </div>
          <div v-else-if="comment.score==3">
            <i class="material-icons">star</i> 
            <i class="material-icons">star</i> 
            <i class="material-icons">star</i> 
            <i class="material-icons">star_border</i> 
            <i class="material-icons">star_border</i> {{ comment.content }}
          </div>
          <div v-else-if="comment.score==2">
            <i class="material-icons">star</i> 
            <i class="material-icons">star</i> 
            <i class="material-icons">star_border</i> 
            <i class="material-icons">star_border</i> 
            <i class="material-icons">star_border</i> {{ comment.content }}
          </div>
          <div v-else-if="comment.score==1">
            <i class="material-icons">star</i> 
            <i class="material-icons">star_border</i>  
            <i class="material-icons">star_border</i> 
            <i class="material-icons">star_border</i> 
            <i class="material-icons">star_border</i> {{ comment.content }}
          </div>
          <div v-else-if="comment.score==0">
            <i class="material-icons">star_border</i> 
            <i class="material-icons">star_border</i> 
            <i class="material-icons">star_border</i> 
            <i class="material-icons">star_border</i> 
            <i class="material-icons">star_border</i> {{ comment.content }}
          </div>
        </div>
      </span>
    </span>
    <div v-if="comment.user_id === this.$store.state.userInfo.userpk">
      <button class="btn btn-dark" @click="commentmodify(comment.id)">수정</button>
      <button class="btn btn-dark" @click="commentdelete(comment.id)">삭제</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
// import router from "@/router";

export default {
  name: "CommentListItem",
  props: {
    comment: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      userlist: [],
      modifycontent: this.comment.content,
      modifyscore: this.comment.score,
      commentupdate: false
    };
  },
  methods: {
    getuser: function() {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      axios
        .get(`${SERVER_IP}/api/v1/userlist/`)
        .then(response => {
          this.userlist = response.data;
        })
        .catch(() => {
          alert("Fail");
        });
    },
    commentmodify: function(commentpk) {
      if (this.commentupdate === false) {
        this.commentupdate = true;
      } else {
        const SERVER_IP = process.env.VUE_APP_SERVER_IP;
        const commentObj = {
          "content": this.modifycontent,
          "score": this.modifyscore
          // "user_id": this.$store.state.userInfo.userpk
        };
        axios
          .put(
            `${SERVER_IP}/api/v1/comment_update_and_delete/${commentpk}/`,
            commentObj
          )
          .then(response => {
            console.log(response);
            this.commentupdate = null;
            this.$router.go();
          })
          .catch(error => {
            console.log(error);
          });
        this.commentupdate = false;
      }
    },
    commentdelete: function(commentpk) {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP;
      axios
        .delete(`${SERVER_IP}/api/v1/comment_update_and_delete/${commentpk}`)
        .then(response => {
          console.log(response);
          this.$router.go();
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  mounted() {
    this.getuser();
  }
};
</script>

<style>
</style>