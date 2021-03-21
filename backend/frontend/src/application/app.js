// Main.js
import Vue from 'vue';
import App from '../App.vue';
// import router from './router'

import '../../node_modules/milligram/dist/milligram.min.css';
import '../../node_modules/milligrid/dist/Milligrid.css';

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
    el: '#app',
    // router,
    components: { App },
    template: '<App/>'
});
