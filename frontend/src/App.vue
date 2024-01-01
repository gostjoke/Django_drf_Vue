<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  <IfDemo />
  <ListDemo />
  <EventDemo/>
  <EventDemo2/>
  <ComputesDemo/>
  <ClassChange />
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';
import IfDemo from './components/IfDemo.vue';
import ListDemo from './components/ListDemo.vue';
import EventDemo from './components/EventDemo.vue';
import EventDemo2 from './components/EventDemo2.vue';
import ComputesDemo from './components/ComputesDemo.vue';
import ClassChange from './components/ClassChange.vue';

export default {
  name: 'App',
  components: {
    HelloWorld,
    IfDemo,
    ListDemo,
    EventDemo,
    EventDemo2,
    ComputesDemo,
    ClassChange,
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
