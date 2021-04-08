import Vue from 'vue'
import App from './App.vue'
import routes from './router/routes'
import store from './store/index'
import './quasar'
import VueRouter from 'vue-router'
// masonry
import VueMasonry from 'vue-masonry-css';
Vue.use(VueMasonry);
import VueFullPage from 'vue-fullpage.js'
import { gsap } from "gsap"
import { PixiPlugin } from "gsap/PixiPlugin.js";
import { MotionPathPlugin } from "gsap/MotionPathPlugin.js";

gsap.registerPlugin(PixiPlugin, MotionPathPlugin);

Vue.use(VueRouter);

export const router = new VueRouter({
  mode: 'history',
  routes,
})
Vue.config.productionTip = false

Vue.use(VueFullPage);

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
