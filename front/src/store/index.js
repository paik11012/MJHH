import Vue from "vue";
import Vuex from "vuex";
import router from "@/router";
import axios from "axios";
Vue.use(Vuex);


export default new Vuex.Store({
  //data 옵션의 기본 상태(state) 정의
  state: {
    userInfo: null, //아직 정보를 받아오지 않은 상태이므로 null
    isLogin: false, //로그인이 되었다면 true로 변경
    isLoginError: false
  },
  mutations: {
    loginSuccess(state, payload) { //로그인 성공시,
      state.isLogin = true;
      state.isLoginError = false;
      state.userInfo = payload;
    },
    loginError(state) { //로그인 실패시,
      state.isLogin = false;
      state.isLoginError = false;
      state.userInfo = null;
    },
    logout(state) { //로그 아웃시,
      state.isLogin = false;
      state.isLoginError = false;
      state.userInfo = null;
    }
  },
  actions: {
    login(context, loginObj) {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      axios.post(SERVER_IP + "/rest-auth/login/", loginObj)
        .then(res => {
          let token = res.data.token;
          const userpk = res.data.user.pk
          localStorage.setItem("access_token", token);
          // this.commit('loginSuccess', token)
          router.push({name: "home"});
          // userinfo 객체 새롭게 만들어서 그곳에 token, loginobject의 username을 저장한다. object 만들기
          const userInfo = {
            userpk: userpk,
            token: token,
            username: loginObj.username
          }
          context.commit("loginSuccess", userInfo)
          // console.log(this.state)
        })
        .catch(() => {
          // this.commit('loginError')
          alert("아이디와 비밀번호를 확인하세요.");
        });
    },
    logout(context) {
      context.commit('logout');
      // router.push({ name: "home"});
      localStorage.setItem("access_token", null)

    },
    signup(dispatch, loginObj) {
      const SERVER_IP = process.env.VUE_APP_SERVER_IP
      axios.post(SERVER_IP + "/rest-auth/registration/", loginObj)
        .then(() => {
          alert("회원가입이 성공적으로 이뤄졌습니다.");
          router.push({ name: "login" });
        })
        .catch(() => {
          alert("이메일과 비밀번호를 확인하세요.");
        });
    },
  }
});