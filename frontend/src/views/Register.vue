<template>
<AppRegister :onSubmit="onSubmit" :request="request" :response="response"/>
</template>

<script>

import AppRegister from "@/components/AppRegister.vue";
import axios from "axios";
export default {
  name: "Register",
  components:{
    AppRegister
  },
  data(){
    return{
      request: {
        email: "",
        password: "",
        confirmPassword: "",
        isLoading:false
      },
      response:{
        status:0,
        message:"",
        data:{}
      }
    }
  },
  methods:{
    onSubmit() {
      this.request.isLoading = true;
      if (this.request.password != this.request.confirmPassword) {
        let res = {
          status: 401,
          message: "Password do not match.",
          data: {}
        }
        this.response = res;
      } else {
        let body = {
          "email": this.request.email,
          "password": this.request.password
        }
        axios.post('/register', body).then((response) => {
          this.response = response.data;
        });
      }
      this.request.isLoading = false;
    }
  }
}
</script>
<style scoped>

</style>