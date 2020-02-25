import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import { http } from './modules/http'
// import user from './modules/user'
// import auth from './modules/auth'

Vue.use(Vuex)
const server_url = "http://localhost:6543/auth"
export default new Vuex.Store({
  modules: {
    // user,
    // auth,
  },
  state: {
    accessToken:  localStorage.getItem('user_token') ||  '',
    currentUser : {},
    status: ''
  },
  mutations: {
    'user_request': (state) => {
      state.status = 'loading';
    },
    'user_success': (state, resp) => {
      state.status = 'success'
      Vue.set(state, 'profile', resp)
    },
    'user_error': (state) => {
      state.status = 'error'
    },
    'auth_logout': (state) => {
      state.profile = {}
    }
  },
  actions: {
    signup: ({commit, dispatch}, user) => {
      commit('user_request');
      // console.log(user)
      debugger;
      http.post('/auth', user)
          .then(resp => {
            debugger;
            const accessToken = resp.data.accessToken
            localStorage.setItem('user_token', accessToken) // store the token in localstorage
            // axios.defaults.headers.common['Authorization'] = accessToken
            axios({url: 'auth', data: user, method: 'POST' })
            commit('user_success', resp)
          })
          .catch(resp => {
            commit('user_error')
            // if resp is unauthorized, logout, to
            localStorage.removeItem('user-token') // if the request fails, remove any possible user token if possible
            // reject(err)
            commit('auth_logout')
            // dispatch('auth_logout')
        }) }
  },
})
