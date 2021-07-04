<template>
  <div id="app">
    <h1>TodoList</h1>
    <h2>Todos: {{ todos.length }}</h2>
    <h2>completed: {{ completedTodosCount.length }}</h2>
    <h2>Uncompleted: {{ UncompletedTodosCount.length }}</h2>
  </div>
</template>

<script>
import { mapState, mapGetters } from 'vuex'
import TodoForm from './components/TodoForm.vue'
import TodoList from './components/TodoList.vue'
export default {
  name: 'App',
  components: {
    TodoForm, TodoList,
  },
  computed: {
    ...mapGetters([
      'completedTodosCount',
      'uncompletedTodosCount',
    ]),
    ...mapState(['todos'])
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
