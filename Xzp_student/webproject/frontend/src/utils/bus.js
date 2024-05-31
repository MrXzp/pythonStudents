import Vue from 'vue';

// 总线，一些组件间简单的数据交流通过它来进行，比如侧边栏折叠。过于复杂的数据推荐使用Vuex
const bus = new Vue();

export default bus;
