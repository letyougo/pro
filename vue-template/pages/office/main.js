// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import ElementUI from 'element-ui'
import '../../theme/index.css'
Vue.use(ElementUI)
Vue.config.productionTip = false
import './index.css'
/* eslint-disable no-new */
var su_validate =  require('../common-part/plugins/su_validate')
Vue.use(su_validate)

new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
