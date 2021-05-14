<template>
    <div class="phones">
        <h1>{{ shopTitle }}</h1>
        <div class="card" v-for="(phone, key) in phones" :key="key">
          <h3>{{ phone.title }}</h3>
          <div>{{ phone.memory }}</div>
          <div>{{ phone.price }}</div>
          <div>
            <button class="btn" @click="minusCount(phone)">-</button>
            <input v-model="phone.count" type="text" class="input">
            <button class="btn" @click="plusCount(phone)">+</button>
          </div>
          <div class="sum">{{ itemPrice(phone) }} р</div>
        </div>
        <div class="total-sum">Сумма: {{ totalPrice }}</div>
    </div>
</template>

<script>
export default {
  name: 'Shop.vue',
  props: {
    shopTitle: String,
  },
  data() {
    return {
      phones: [
        {
          title: 'Google pixel 5',
          memory: '4Gb/64Gb',
          price: 50000,
          count: 1,
        },
        {
          title: 'Apple iPhone X',
          memory: '4Gb/64Gb',
          price: 80000,
          count: 2,
        },
        {
          title: 'Samsung Galaxy 10',
          memory: '6Gb/128Gb',
          price: 100000,
          count: 3,
        },
        {
          title: 'Redmi Note 10',
          memory: '6Gb/128Gb',
          price: 25000,
          count: 5,
        },
      ],
    };
  },
  computed: {
    totalPrice() {
      let sum = 0;
      this.phones.forEach((item) => {
        sum += item.price * item.count;
      });
      return sum;
    },
  },
  methods: {
    itemPrice(phone) {
      return +phone.count * phone.price;
    },

    plusCount(phone) {
      phone.count = +phone.count + 1;
    },

    minusCount(phone) {
      if (phone.count > 0) {
        phone.count = +phone.count - 1;
      }
    },
  },
};
</script>

<style scoped lang="scss">
  .card {
    box-shadow: 0 2px 4px 0 #333;
    border-radius: 8px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 20px;
    margin-bottom: 10px;
  }

  h3 {
    width: 25%;
    text-align-last: left;
  }

  .sum{
    width: 10%;
  }

  .total-sum {
    text-align: right;
    padding: 10px;
    font-style: bold;
    font-size: 2em;
  }

  .input{
    box-sizing: border-box;
    height: 30px;
    border: 1px solid #ccc;
    border-left: 0;
    border-right: 0;
    width: 30px;
    text-align: center;
    font-size: 0.9em;
  }

  .btn {
    box-shadow: none;
    border: 1px solid #ccc;
    background: #ffffff;
    height: 30px;
    width: 30px;
    cursor: pointer;

    &:first-child{
      border-radius: 8px 0 0 8px;

      &:hover{
        background: #666;
        color: #fff;
      }
    }
    &:last-child{
      border-radius: 0 8px 8px 0;
      &:hover{
        background: green;
        color: #fff;
      }
    }
  }
</style>
