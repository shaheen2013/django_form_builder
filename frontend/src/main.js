import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './scss/main.scss'
import ApiService from './services/api.service.js'
window.ApiService = ApiService;
ApiService.init();
Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
