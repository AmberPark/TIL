<template>
  <div class="container">
    <h2 class="text-center mt-5">My Vue Todo app</h2>

    <!--input-->
    <div class="d-flex">
      <input v-model="task" type="text" placeholder="Enter task" class="form-control">
      <button @click="submitTask" class="btn btn-warning rounded-0">Submit</button>
    </div>

    <!-- Task table -->
    <table class="table table-bordered">
      <thead>
        <tr>
          <th scope="col">Task</th>
          <th scope="col">Status</th>
          <th scope="col" class="text-center">Edit</th>
          <th scope="col" class="text-center">Delete</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(task, index) in tasks" :key="index">
          <td><span :class="{'finished': task.status === 'Done'}">{{task.name}}</span></td>
          <td style="width: 120px">
            <span @click="changeStatus(index)" class="pointer" 
            :class="{'text-danger': task.status === 'Todo', 
            'text-warning': task.status === 'InProgress',
            'text-success': task.suatus === 'Done'}">
              {{firstCharUpper(task.status)}}
            </span>
          </td>
          <td>
            <div class="text-center" @click="editTask(index)">
              <span class="fa fa-pen"></span>
            </div>
          </td>
          <td>
            <div class="text-center" @click="deleteTask(index)">
              <span class="fa fa-trash"></span>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>


export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      task: '',
      editedTask: null,
      availableStatuses: ['Todo', 'Inprogress', 'Done'],
      tasks: [
        {
          name: 'Eat dinner',
          status: 'InProgress',
        },
        {
          name: 'Sleep',
          status: 'Todo'
        }
      ]
    }
  },
  methods: {
    submitTask(){
      if(this.task.length === 0) return;

      if(this.editedTask === null){
        this.tasks.push({
          name: this.task,
          status: 'Todo'
        })
      }else{
          this.tasks[this.editedTask].name = this.task;
          this.editedTask = null;        
      }

      this.task = '';

    },
    deleteTask(index){
      this.tasks.splice(index, 1);
    },
    editTask(index){
      this.task = this.tasks[index].name;
      this.editedTask = index;

    },

    changeStatus(index){
      let newIndex = this.availableStatuses.indexOf(this.tasks[index].status);
      if(++newIndex > 2) newIndex = 0;
      this.tasks[index].status = this.availableStatuses[newIndex];
    },

    firstCharUpper(str) {
      return str.charAt(0).toUpperCase() + str.slice(1)
    }


  }
}
</script>

<style>
.pointer{
  cursor: pointer;
}

.finished{
  text-decoration: line-through;
}
</style>
