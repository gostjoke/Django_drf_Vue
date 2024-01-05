<template>
    <div class="main">
        <h3>Main</h3>
        <AritcleItem/>
        <AritcleItem/>
        <AritcleItem/>
    </div>
</template>

<script>
import AritcleItem from './AritcleItem.vue';
export default{
    components:{
        AritcleItem
    }
}
</script>

<style scoped>

.main{
    float:left;
    width:70%;
    height:400px;
    border: 5px solid #999;
    box-sizing: border-box;
}

</style>
