<template>
    <h3>
        ListDemo 列表渲染
    </h3>
    <div>
    <p v-for="(item, index) in names" :key="index">{{ index }}:{{ item }}</p>
    </div>
</template>

<script>    


export default{
    data(){
        return {
            names:["dog","cat","pig"]
        }
    }
}
</script>
