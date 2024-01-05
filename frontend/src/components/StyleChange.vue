<template>
    <h3 style="color:green">
       StyleChange 
    </h3>
    <p :style="objectstyle">Style</p>
</template>

<script>
export default {
    data(){
        return{
            objectstyle:{color:'red',fontSize:'30px'}
        }
    }
}
</script>

