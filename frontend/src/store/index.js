import Vue from 'vue';
import Vuex from 'vuex';

import guestbook from './guestbook';
import getsession from './getsession';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    guestbook,
    getsession,
  },
});