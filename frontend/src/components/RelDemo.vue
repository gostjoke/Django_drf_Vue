<template>
    <h3> DelDemo </h3>
    <div ref="container" class="container">{{ content }}</div>
    <input type="text" ref="username">
    <button @click="getElementHandle"> 獲取元素 </button>
</template>

<script>

export default{
    data() {
        return {
            content:"yes"
        }
    },
    methods:{
        getElementHandle(){
            this.$refs.container.innerHTML = "hahaha"
            console.log(this.$refs.username.value)
        }
    }
}

</script>




