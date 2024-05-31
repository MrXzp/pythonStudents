<template>
    <div class="Caidan">
        <div class="logoDom">
            <span>吉他小站</span>
        </div>
        <div class="sles">
            <el-input placeholder="请输入内容" v-model="input" clearable>
            </el-input>

        </div>

        <div class="itemList">
            <span v-for="(item, index) in itemList" :key="index" @click="Showimg(item)">
                {{ item.name }}
            </span>
        </div>
    </div>
</template>

<script>
import Bus from "@/utils/bus.js";
export default {
    name: 'Caidan',
    data() {
        return {
            message: '你好，Vue 2！',
            input: '',
            itemList: [
                {
                    name: '平凡之路',
                    author: '朴树',
                    id: '021',
                    imgList: [
                        '@/assets/gieta/pfzl/1.jpg',
                        '@/assets/gieta/pfzl/2.jpg',
                        '@/assets/gieta/pfzl/3.jpg',

                    ]
                },
                {
                    name: '蒲公英的约定',
                    author: '周杰伦',
                    id: '027',
                    imgList: [
                        '@/assets/gieta/pgydyd/1.jpg',
                        '@/assets/gieta/pgydyd/2.jpg',
                        '@/assets/gieta/pgydyd/3.jpg',

                    ]
                }
            ]
        };
    },
    components: {},
    created() {
   
    },
    mounted() {
        
    },
    updated() {
      
    },
    destroyed() {
       
    },
    methods: {
        // 自定义方法
        Showimg(item) {
            console.log('当前点击的歌是', item);
            Bus.$emit('ImgChange', item)

        },
    },
    watch: {
        // 监听属性
    },
    
}
</script>
 
<style lang="scss" scoped>
.Caidan {
    width: 240px;
    height: 100%;
    display: flex;
    flex-direction: column;


    .logoDom {
        height: 80px;
        font-size: 30px;
        display: flex;
        justify-content: center;
        align-items: center;
       
    }
    .sles{
        padding: 0 20px;
    }

    ::v-deep .el-input__inner {
        border-radius: 20px;
        background-color: #ffffff00;
    }

    .itemList {

        font-size: 18px;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding-left: 15px;
        padding-top: 20px;

        span {
            width: 100%;
            cursor: pointer;
            border-radius: 8px;
            padding: 3px 5px;

            &:hover {
                background-color: rgba(226, 203, 203, 0.25);
            }
        }
    }

    /* 样式 */
}
</style>