<template>
  <div class="vertical-center">
  <div v-if="response.status == 401 || response.status == 409" class="alert btn-danger" role="alert">
    {{response.message}}
  </div>
    <div v-if="response.status == 201" class="alert btn-success" role="alert">
      {{response.message}}
    </div>

    <div class="bg-white border">

    <h5 class="pt-md-4 text-center">Registration</h5>
    <section class="w-100 plr-5 d-flex justify-content-center pb-4">

      <form class="w-100" @submit.prevent="onSubmit">

        <div class="form-outline mb-4">
          <input type="email" name="email" id= "email" class="form-control" :class="{'active':request.email}" :value="request.email" @change="onChange"/>
          <label class="form-label" for="email">Email address</label>
        </div>

        <div class="form-outline mb-4">
          <input type="password" name="password" class="form-control" :class="{'active':request.password}" :value="request.password" @change="onChange"/>
          <label class="form-label" >Password</label>
        </div>

        <div class="form-outline mb-4">
          <input type="password" name="confirmPassword" class="form-control" :class="{'active':request.confirmPassword}" :value="request.confirmPassword" @change="onChange"/>
          <label class="form-label" >Confirm Password</label>
        </div>

        <button type="submit" class="btn btn-primary btn-block mb-4" >Sign up</button>

        <div class="text-center">
          <p>Already a member? <a href="/">Sign in</a></p>
        </div>

      </form>
    </section>
  </div>
  </div>
</template>

<script>
export default {
  name: "Register",
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