<template>
  <AppHome :logout="logout" :todoList="todoList" @update-todo-list="updateTodoList"/>
</template>

<script>
// @ is an alias to /src
import AppHome from "@/components/Home/AppHome.vue";
import axios from 'axios'
export default {
  name: "Home",
  components: {
    AppHome
  },
  data() {
    return {
      todoList: []
    }
  },
  methods:{
    getTodoList() {
      axios.get('/todo', {
        headers: {
          "Authorization": localStorage.getItem("token")
        }
      }).then(response => {
        if (response.data.status == 200) {
          this.todoList = response.data.data;
          this.todoList.forEach(item => {item.isAdded=false;item.isEdit = false;item.status = (item.status.toString().toLowerCase() == "pending" ? 0 :1)});
        }
      });
    },
    updateTodoList(){
      console.log("suaid")
      this.getTodoList();
    },
    logout(){
      axios.get('/logout',{
        headers:{
          'Authorization': localStorage.getItem('token')
        }
      }).then((response)=>{
        if(response.data.status == 200) {
          localStorage.setItem('token', null);
          this.$router.back();
        }
      })
    }
  },
  mounted() {
    this.getTodoList();
  }
};
</script>