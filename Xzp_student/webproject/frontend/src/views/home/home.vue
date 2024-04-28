<template>
  <div class="view-container">
    
  </div>
</template>

<script>
export default {
  name: '',
  data() {
    return {
      message: '你好，Vue 2！',
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
  },
  watch: {
    // 监听属性
  },
}
</script>
 
<style lang="scss" scoped>
.view-container {
 height: 100vh;
 width: 100vh;


}
</style>