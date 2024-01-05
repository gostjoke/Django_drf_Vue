<!-- eslint-disable vue/multi-word-component-names -->  
<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <MyHeader />
  <MyMain />
  <MyAside />
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  <IfDemo />
  <ListDemo />
  <EventDemo/>  
  <EventDemo2/>
  <ComputesDemo/>
  <ClassChange />
  <StyleChange />
  <RelDemo />
</template>

<script>
// import MyHeader from './components/MyHeader/MyHeader.vue';
import MyMain from './components/MyHeader/MyMain.vue';
import MyAside from './components/MyHeader/MyAside.vue';
import HelloWorld from './components/HelloWorld.vue';
import IfDemo from './components/IfDemo.vue';
import ListDemo from './components/ListDemo.vue';
import EventDemo from './components/EventDemo.vue';
import EventDemo2 from './components/EventDemo2.vue';
import ComputesDemo from './components/ComputesDemo.vue';
import ClassChange from './components/ClassChange.vue';
import StyleChange from './components/StyleChange.vue';
import RelDemo from './components/RelDemo.vue';

export default {
  name: 'App',
  components: {
    // MyHeader,
    MyMain,
    MyAside,
    HelloWorld,
    IfDemo,
    ListDemo,
    EventDemo,
    EventDemo2,
    ComputesDemo,
    ClassChange,
    StyleChange,
    RelDemo,
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
