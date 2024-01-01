<template>
    <h3 style="color:red"> Attributes Calculate 屬性計算 </h3>
    <ul>
        <li>{{ ite.content.length > 0 ? "yes":"no" }}</li>
    </ul>
</template>

<script>
    export default{
        data(){
            return{ 
                ite:{
                    name:"dog",
                    content:["fr","back","python"],
                }
            }
        }
    }
</script>