import Vue from 'vue'
import Cookies from 'js-cookie'
import App from './App.vue'
import store from './store'
import router from './router'

import Element from 'element-ui'

Vue.use(Element, {
  size: Cookies.get('size') || 'medium' // set element-ui default size
})

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router,
  store,
}).$mount('#app')
