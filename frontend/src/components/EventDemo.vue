<template>
    <h3 style="color:green"> Event Demo</h3>
    <button @click="addcount">Add</button>
    <button @click="mulcount">multiple</button>
    <p>{{ count }}</p>
    <button @click="printHello(count)">hello</button>
    <div ref="helloContainer"></div>
</template>

<script>
export default {
    data(){
        return {
            count: 0,
            count2: 2,
        }
    },
    methods:{
        addcount(event){
            event.target.innerHTML = "Add" + this.count;
            this.count ++
        },
        mulcount(event){
            event.target.innerHTML = "multiple" + this.count;
            this.count *= this.count
        },
        printHello(msg){
            const newParagraph = document.createElement('p');
            newParagraph.textContent = msg;

            // 获取容器元素并将新元素添加到容器中
            const container = this.$refs.helloContainer;
            container.appendChild(newParagraph);
        }
    }
}

</script>