<template>
  <div class="m-3">

    <div v-if="this.response.status == 200 || this.response.status == 201" class="alert btn-success mb-3" role="alert">
      {{this.response.message}}
    </div>
    <div v-else-if="this.response.status != 0" class="alert btn-danger mb-3" role="alert">
      {{this.response.message}}
    </div>
  <div class="card">

    <span class="w-100 card-header d-flex justify-content-between">
        <h5 class="mt-2 d-inline">Todo list</h5>
        <button class="btn btn-primary" @click="addRow">Add</button>
    </span>
    <div class="card-body p-0">
      <table class="table align-middle mb-0 bg-white">
        <thead class="bg-light">
        <tr>
          <th>Title</th>
          <th>Description</th>
          <th>Status</th>
          <th style="padding-left: 3.1rem">Actions</th>
        </tr>
        </thead>
        <tbody >
        <TableRow v-for="(todo,index) in todoList" :key="todo.todo_id" :index="index" :todo="todo"
                  :deleteRow="deleteRow" :response="response" @update-response="updateResponse"/>
        </tbody>
      </table>
    </div>
  </div>
  </div>
</template>

<script>
import TableRow from "@/components/Home/TableRow";
import axios from "axios";
export default {
  name: "TodoList",
  components:{TableRow},
  data(){
    return{
    response:{
      status:0,
      message:""
    }
    }
  },
  methods:{
    deleteRow(e,index){
      if(index == 0 && this.$props.todoList[index].isAdded){
        this.$props.todoList.splice(index, 1);
      }else {
        let todo_id = this.$props.todoList[index].todo_id;
        axios.delete(`todo/${todo_id}`, {
          headers: {
            'Authorization': localStorage.getItem("token")
          }
        }).then(response => {
          if (response.data.status == 200) {
            this.response = response.data
            this.$props.todoList.splice(index, 1);
          }
        })
      }
    },
    addRow(){
      this.$props.todoList.unshift({
            todo_id:this.$props.todoList.length+1,
            title:"",
            description:"",
            status:0,
            isEdit:true,
            isAdded:true,
      })
    },
    updateResponse(response) {
      this.response.status = response.status;
      this.response.message = response.message;
      if (response.status == 200 || response.status == 201)
        this.$emit('update-todo')
    }
  },
  props:{
    todoList:Array,
  },
  emits:["update-todo"]
}
</script>

<style scoped>

</style>