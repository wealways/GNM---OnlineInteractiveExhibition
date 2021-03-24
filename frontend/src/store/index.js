import Vue from 'vue';
import Vuex from 'vuex';

import guestbook from './guestbook';
Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    guestbook,
  },
});