import Vue from 'vue'
import Vuex from 'vuex'
import jwtDecode from 'jwt-decode'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: null,
  },
  getters: {
    isLoggedIn(state){
      return state.token ? true : false
    },
    options(state){
      return {
        headers: {
          Authorization: 'JWT ' + state.token
        }
      }
    },
    userId(state){
      return state.token ? jwtDecode(state.token).user_id : null
    }
  },
  mutations: {
    setToken(state, token){
      state.token = token
    }
  },
  actions: {
    login(context, token){
      context.commit('setToken', token)
    },
    logout(context){
      context.commit('setToken', null)
    }
  },
  modules: {
  }
})
