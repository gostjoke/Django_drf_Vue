<template>
    <h3 style="color:red"> EventDemo2 stopdefault </h3>
    <a @click.prevent="clickhandle" href="https://github.com/youngyangyang04/leetcode-master/">Click</a>

    <div @click="clickdiv">
        <p @click.stop="clickp">bubble test</p>
    </div>
    <div>
        <button @click="addlist"> addlist </button>
        <button @click="poplist"> poplist </button>
    </div>
    <div>
        <ul>
            <li v-for="(item, index) of names" :key="index">{{ item }}</li>
        </ul>
    </div>

</template>

<script>
    export default {
        data(){
            return{
                names:["Iva", "Vivan", "Tracy"]
            }
        },
        methods:{
            clickhandle(){
                // e.preventDefault();  // equal to @click.prevent 
                console.log("to the other page");
            },
            clickdiv(){
                console.log("div")
            },
            clickp(){
                // e.stopPropagation(); // equal to @click.stop
                console.log("p")
            },
            addlist(){
                this.names.push("Dog")
            },
            poplist(){
                var a;
                a= this.names.pop(),
                console.log(a)
            }
        }
    }
</script>
