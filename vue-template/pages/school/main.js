
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'

import '../../theme/index.css'
Vue.use(ElementUI)
var su_validate =  require('../common-part/plugins/su_validate')
Vue.use(su_validate)
Vue.config.productionTip = false
import './index.css'
/* eslint-disable no-new */

new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
