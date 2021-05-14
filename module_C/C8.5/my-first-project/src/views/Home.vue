<template>
  <div class="home">
    <img alt="Це картинка" src="../assets/logo.png">
    <HelloWorld msg="Моя первая хурма на Vue"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue';

export default {
  name: 'Home',
  components: {
    HelloWorld,
  },
};
</script>
