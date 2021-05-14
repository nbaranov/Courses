<template>
  <div id="app">
    <shop shop-title="Смартфоны" />
    <shop shop-title="Еще смартфоны" />
  </div>
</template>

<script>
import Shop from './components/Shop.vue';

export default {
  components: {
    Shop,
  },
};

</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #0d2946;
}

</style>
