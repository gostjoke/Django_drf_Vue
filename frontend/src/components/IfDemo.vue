<template>
    <div>
        條件渲染,contdition view     
    </div>
    <div v-if="flag">你能看見我嗎?</div>
    <div v-else> 你不能看見我</div>
    <div v-show="flag">vshow see me?</div>
    <div v-if="type === 'A'">it is A</div>
    <div v-else-if="type === 'B'"> it is B</div>
    <button @click="changeFlag">click me</button>
    <form method="POST">
        <div>
            <label for="usename">Username:</label><input for="username" type="text" id="username">
        </div>
        <div>
            <label for="password">Password :</label><input for="password" type="password" id="password">
        </div>
        <input type="submit" value="Submit" :disabled="checksubmit">
    </form>
    <button @click="changecheck">確認填寫</button>
</template>
<script>    
export default {
    data(){
        return {
            flag:true,  
            type:"B",
            checksubmit:true,
        };
    },
    methods:{
        changeFlag(){
            this.flag = !this.flag;
        },
        changecheck(){
            this.checksubmit = !this.checksubmit;
        }
    },
};

</script>