<template>
    <h3 style="color:blue">Class Change</h3>
    <p :class="{ 'active':isActive, 'text-danger':hasError}"> class bond 1</p>
    <p :class="classObject"> Class bond 2 </p>
    <p :class="[classObject.active ? 'active':'']">Class bond 3</p>
    <button @click="changeclass">changeclass</button>
</template>

<script>

export default{
    data(){
        return{
            isActive:true,
            hasError:true,
            classObject:{
                'active':true,
                'text-danger':true,
            },
        }
    },
    methods:{
        changeclass(){
            this.classObject.active = !(this.classObject.active);
            this.classObject['text-danger'] = !(this.classObject['text-danger']);
            console.log(this.classObject.active)
        }
    }
}

</script>

<style>

.active {
    font-size: 30px;
}
.text-danger {
    color:red;
}
</style>