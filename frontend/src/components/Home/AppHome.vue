<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">

    <div class="container-fluid  w-50 justify-content-end">
      <a class="navbar-brand" href="#/home">
        <img
            src="https://icon-library.com/images/todo-icon/todo-icon-5.jpg"
            class="me-2"
            height="30"
            width="60"
            alt="todoapp Logo"
            loading="lazy"
        />
        <small>Todo app</small>
      </a>
    </div>
      <div class="d-flex justify-content-end w-50" style="margin-right: 0.6em">
        <a class="text-reset me-3" href="#" @click.prevent="logout">
          <i class="fas fa-sign-out-alt"></i>
        </a>
      </div>
  </nav>
  <div class="container-fluid">
    <TodoList :todoList="todoList" @update-todo="updateTodo"/>
  </div>
</template>

<script>
import TodoList from "@/components/Home/TodoList";
export default {
  name: "Home",
  components:{
    TodoList
  },
  props:{
    logout:Function,
    todoList:Array,
  },
  emits:["update-todo-list"],
  methods:{
    updateTodo(){
      this.$emit("update-todo-list")
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
