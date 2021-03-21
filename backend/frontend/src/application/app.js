// Main.js
import Vue from 'vue';
import App from '../App.vue';
// import router from './router'

import '../../node_modules/bootstrap/dist/css/bootstrap.min.css';
import '../../node_modules/bootstrap/dist/js/bootstrap.bundle.min';

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
    el: '#app',
    // router,
    components: { App },
    template: '<App/>'
});
