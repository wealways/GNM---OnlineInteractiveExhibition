import Vue from 'vue'
import App from './App.vue'
import routes from './router/routes'
import store from './store'
import './quasar'
import VueRouter from 'vue-router'

Vue.use(VueRouter);

export const router = new VueRouter({
  mode: 'history',
  routes,
})
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
