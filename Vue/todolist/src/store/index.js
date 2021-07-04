import Vue from "vue";
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: []
  },
  mutations: {
    CREATE_TODO (state, todoItem) {
      state.todos.push(todoItem)
    },
    DELETE_TODO (state, todoItem) {
      const index = state.todos.indexOf(todoItem)
      state.todos.splice(index, 1)
    },
    UPDATED_TODO (state, todoItem) {
      state.todos = state.todos.map((todo) => {
        if (todo == todoItem) {
          return { ...todo, completed: !todo.completed}
        }
        return todo
      })
    }
  },
  actions: {
    createTodo ({commit}, todoItem) {
      commit('CREATE_TODO', todoItem)
    },
    deleteTodo ({commit}, todoItem) {
      if (confirm('삭제할꺼?')) {
        commit('DELETE_TODO', todoItem)
      }
    },
    UpdateTpdp ({commit}, todoItem) {
      commit('UPDATED_TODO', todoItem)
    }
  },
  getters: {
    completedTodosCount (state) {
      return state.todos.filter(todo => toeo.completed)
    },
    uncompletedTodosCount (state) {
      return state.todos.filter(todo => !todo.completed)
    }
  },
  modules: {

  },
})