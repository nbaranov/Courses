<template>
    <div id="data">
      <h2>Your ToDo List</h2>
      <div class="form">
          <input type="text" v-on:keyup.enter="add" v-model="todoText" placeholder="Ваша задача">
          <button class="add" @click="add" :disabled="!todoText" >Добавить</button>
          <button class="delete-all" @click="deleteAll">Удалить всё</button>
      </div>
      <div class="list">
          <div class="item" v-for="(todo, key) in list" :key=key>
            <button class="delete-item" @click="deleteTodo(key)">&#10003;</button>
            <span class="todo-text">{{ todo.text }}</span>
          </div>
      </div>
    </div>
</template>

<script>
export default {
  name: 'Todo',
  data() {
    return {
      todoText: '',
      list: [],
    };
  },
  methods: {
    add() {
      this.list.push({ text: this.todoText });
      this.todoText = '';
    },

    deleteAll() {
      this.list = [];
    },

    deleteTodo(key) {
      this.list.pop(key);
    },
  },
};
</script>

<style scoped>
  #data{
    display: flex;
    justify-content: center;
    flex-direction: column;
  }

  .form{
    display: flex;
    align-self: center;
    justify-content: space-around;
    width: 97%;
    align-self: center;
  }

  input{
    width: 55%;
  }

  .add{
    width: 20%;
  }

  .delete-all{
    width: 20%;
  }

  .list{
    display: flex;
    justify-content: center;
    flex-direction: column;
    margin-top: 1em;
  }

  .item{
    display: flex;
    justify-content: space-around;
    align-content: center;
    border: 1px;
    border-style: solid;
    line-height: 35px;
    margin-bottom: 15px;
  }

  .delete-item{
    width: 35px;
    background-color:transparent;
    border-radius:25px;
    border:2px solid #4b8f29;
    cursor:pointer;
    color:#099412;
    font-size:20px;
    text-shadow:0px 1px 0px #5b8a3c;
    text-align: center;
  }

  .delete-all{
    text-align: center;
  }

  .todo-text{
    width: 90%;
  }
</style>
