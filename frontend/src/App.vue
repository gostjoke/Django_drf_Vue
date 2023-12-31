<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  <IfDemo />
  <ListDemo />
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';
import IfDemo from './components/IfDemo.vue';
import ListDemo from './components/ListDemo.vue';

export default {
  name: 'App',
  components: {
    HelloWorld,
    IfDemo,
    ListDemo,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
