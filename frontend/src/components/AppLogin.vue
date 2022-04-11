<template>
  <div class="vertical-center">
    <div v-if="response.status == 401 || response.status == 500" class="alert btn-danger" role="alert">
      {{response.message}}
    </div>
    <div v-if="response.status == 200" class="alert btn-success" role="alert">
      {{response.message}}
    </div>

    <div class="bg-white border">
    <h5 class="pt-md-4 text-center">LOGIN</h5>
    <section class="w-100 plr-5 d-flex justify-content-center pb-4">
  <form class="w-100" @submit.prevent="onSubmit">

    <div class="form-outline mb-4">
      <input type="email" name="email" id= "email" class="form-control" :class="{'active':request.email}" :value="request.email" @change="onChange"/>
      <label class="form-label" for="email">Email address</label>
    </div>

    <div class="form-outline mb-4">
      <input id="password" type="password" name="password" class="form-control" :class="{'active':request.password}" :value="request.password" @change="onChange"/>
      <label class="form-label" for="password">Password</label>
    </div>

    <div class="row mb-4">
      <div class="col d-flex justify-content-center">
        <div class="form-check">
          <input class="form-check-input" type="checkbox" value="" id="form2Example34" checked />
          <label class="form-check-label" for="form2Example34"> Remember me </label>
        </div>
      </div>

      <div class="col">
        <a href="#!">Forgot password?</a>
      </div>
    </div>
    <button type="submit" class="btn btn-primary btn-block mb-4">
      <span v-if="!request.isLoading">SIGN IN</span>
      <div v-if="request.isLoading" class="spinner-border text-light" role="status">
        <span class="sr-only">Loading...</span>
      </div>
    </button>

    <div class="text-center">
      <p>Not a member? <a href="#/register">Register</a></p>
    </div>
  </form>
  </section>
  </div>
  </div>
</template>

<script>
export default {
  name: "Login",
  props:{
    request:Object,
    response:Object,
    onSubmit:Function
  },
  methods:{
    onChange(e){
      this.$props.request[e.target.name] = e.target.value;
    }
  }
}
</script>

<style scoped>
.vertical-center{
  border-radius: 20px;
  width:30%;
  margin: auto;
  position: absolute;
  top: 20%;
  left: 35%;
}
.plr-5{
  padding: 0 3em;
}
</style>