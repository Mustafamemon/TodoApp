<template>
<AppLogin :onSubmit="onSubmit" :request="request" :response="response"/>
</template>

<script>
import AppLogin from "@/components/AppLogin.vue";
import axios from "axios";
export default {
  name: "Login",
  components: {
    AppLogin
  },
  data() {
    return {
      request: {
        email: "",
        password: "",
        isLoading:false
      },
      response: {
        status: 0,
        message: "",
        data: {}
      }
    }
  },
  methods: {
    onSubmit() {
      this.request.isLoading = true;
      let body = {
        "username": this.request.email,
        "password": this.request.password
      }
      axios.post('/login', body).then((response) => {
        this.request.isLoading = false;
        this.response = response.data;
        if (this.response.status == 200) {
          this.$router.push("home");
          localStorage.setItem('token',"Token " + this.response.data.token);
        }
      });
    }
  }
}
</script>

<style scoped>

</style>