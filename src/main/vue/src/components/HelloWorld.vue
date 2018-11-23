<template>
  <div class="users">
    <h1>Users</h1>
     <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Username</th>
              <th scope="col">Email</th>
              <th scope="col">Picture</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(user, index) in users" :key="index">
              <td>{{ user.username }}</td>
              <td>{{ user.email }}</td>
              <td>{{ user.picture }}</td>
            </tr>
          </tbody>
        </table>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      users: []
    };
  },
  methods: {
    getUsers() {
      const path = "http://localhost:5000/users";
      axios
        .get(path)
        .then(res => {
          this.users = res.data.users;
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
        });
    }
  },
  created() {
    this.getUsers();
    console.log(this.users[0,3])
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
