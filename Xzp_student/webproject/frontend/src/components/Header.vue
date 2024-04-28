<template>
  <div class="view-container">
        <div class="listDom">
            <div class="itemDom" v-if="(item,index) in data" :key="index" @click="RouterClick(item)"></div>
        </div>
  </div>
</template>

<script>
export default {
  name: '',
  data() {
    return {
      message: '你好，Vue 2！',
      data:[
        {
            name:'首页',
            path:'/index'
        },
        {
            name:'登录',
            path:'/login'
        }
      ]
    };
  },
  components: {},
  created() {
    console.log('组件已创建。');
  },
  mounted() {
    console.log('组件已挂载。');
  },
  updated() {
    console.log('组件已更新。');
  },
  destroyed() {
    console.log('组件已销毁。');
  },
  methods: {
    // 自定义方法

    RouterClick(item){
        this.$router.push(redirect)
    },
  },
  watch: {
    // 监听属性
  },
}
</script>
 
<style lang="scss" scoped>
.view-container {
  /* 样式 */

  .listDom{
    min-height: 80px;

  }
}
</style>