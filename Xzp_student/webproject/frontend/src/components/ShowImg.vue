<template>
  <div class="Imgdom">
    <div class="img-container">
      <img class="imgbox" v-for="(imgSrc, index) in imgList" :key="index" :src="getImageUrl(imgSrc)" alt="Image" :style="{ width: `calc((100vw - 240px) / ${imgList.length})` }" />
    </div>
  </div>
</template>

<script>
import Bus from "@/utils/bus.js";
import { getImageUrl } from "@/utils/loadImages.js";
export default {
  name: '',
  data() {
    return {
      message: '你好，Vue 2！',
      imgList: [],
    };
  },
  components: {},
  created() {

  },
  mounted() {
    //给Bus绑定一个isLeft监听事件
    Bus.$on('ImgChange', (info) => {  //info 接收的参数
      this.imgList = info.imgList
      console.log('要展示的图片对象', this.imgList)
    });
  },
  updated() {

  },
  destroyed() {

  },
  methods: {
    // 自定义方法
    getImageUrl(imgSrc) {
      return getImageUrl(imgSrc.replace('@/assets/gieta/', ''));
    }

  },
  watch: {
    // 监听属性
  },
  beforDestroy() {
    Bus.$off("ImgChange")  //要释放，不然会一直叠加
  }
}
</script>
 
<style lang="scss" scoped>
.Imgdom {
  width: calc(100vw - 240px);
  height: 100%;
  display: flex;

  .img-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 100%;
  }

  

  /* 样式 */
}</style>