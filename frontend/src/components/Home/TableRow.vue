<template>
  <tr>
    <td style="width: 200px">
      <input v-if="isEdit" type="text" class="height" v-model="title"/>
      <p v-if="!isEdit" class="fw-bold mb-1">{{title}}</p>
    </td>
    <td>
      <textarea v-if="isEdit" class="w-100 height margin" v-model="description"></textarea>
      <p v-if="!isEdit" class="fw-normal mb-1">{{description}}</p>
    </td>
    <td style="width: 200px" >
      <select v-if="isEdit" class="form-control height"  v-model="status" @change="onChange">
        <option value=0>Pending</option>
        <option value=1>Completed</option>
      </select>
      <span v-if="!isEdit" style="padding-left: 1em">
        <i v-if="status" class="fas fa-check-circle" style="color: green"></i>
        <i v-if="!status" class="fas fa-hourglass" style="color: red"></i>
      </span>
    </td>
    <td style="width: 200px">
      <button type="button" class="padding btn btn-link btn-sm" @click="onEdit" :disabled="isEdit">
        <i class="fas fa-edit"></i>
      </button>
      <span style="padding-bottom: 0.1rem"> | </span>
      <button type="button" class="padding btn btn-link btn-sm" @click="(e)=>deleteRow(e,index)">
        <i class="far fa-trash-alt " style="color: red"></i>            </button>
      <span style="padding-bottom: 0.1rem"> | </span>

      <button type="button" class="padding btn btn-link btn-sm" @click="onSave" :disabled="!isEdit" >
        <i class="fas fa-save"></i>
      </button>
    </td>
  </tr>
</template>

<script>
import axios from "axios";
export default {
  mounted() {
    this.title = this.todo.title;
    this.description = this.todo.description;
    this.status = this.todo.status;
    this.isEdit = this.todo.isEdit;
  },
  name: "TableRow",
  props:{index:Number,todo:Object , response:Object,deleteRow:Function},
  emits:['update-response'],
  data() {
    return {
      isEdit: false,
      title:'',
      description:'',
      status:0
    }
  },
  methods:{
    onChange(e){
      this.status = parseInt(e.target.value) ;
    },
    onEdit(){
      this.isEdit = true;
    },
    onSave(){
      let body = {
        'title': this.title,
        'description': this.description,
        'status': this.status == 1 ? "completed" : "pending"
      }
      if(this.todo.isAdded) {
        axios.post('todo', body, {
          headers: {
            'Authorization': localStorage.getItem('token')
          }
        }).then(response => {
          if (response.data.status == 201) {
            this.isEdit = false;
          }
          this.$emit('updateResponse',response.data)
        })
      }else{
        axios.put(`todo/${this.$props.todo.todo_id}`, body, {
          headers: {
            'Authorization': localStorage.getItem('token')
          }
        }).then(response => {
          if (response.data.status == 200) {
            this.isEdit = false;
          }
          this.$emit('update-response',response.data)
        })
      }
    }
  }
}
</script>

<style scoped>
.padding{
  padding: 0.1rem 0.5rem;
}
.height{
  height:35px;
}
.margin{
  margin-top: 6px;
}
</style>