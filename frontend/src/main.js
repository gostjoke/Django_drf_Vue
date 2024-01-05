import { createApp } from 'vue'
import App from './App.vue'
import MyHeader from './components/MyHeader/MyHeader.vue'

const app = createApp(App)

app.component('MyHeader', MyHeader).mount('#app')
