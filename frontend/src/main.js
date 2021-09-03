import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './scss/main.scss'
import 'bootstrap'
import ApiService from './services/api.service.js'
import Swal from 'sweetalert2'

window.ApiService = ApiService;
ApiService.init();
Vue.config.productionTip = false;
//sweetalert2
window.Swal = require('sweetalert2');
//Toast
window.Toast = Swal.mixin({
  toast: true,
  position: 'top-end',
  showConfirmButton: false,
  timer: 3000,
  timerProgressBar: true,
  didOpen: (toast) => {
    toast.addEventListener('mouseenter', Swal.stopTimer)
    toast.addEventListener('mouseleave', Swal.resumeTimer)
  }
});
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
