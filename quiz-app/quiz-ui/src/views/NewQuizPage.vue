<template>
  <h1>New Quiz Page</h1>
  <p>Saisissez votre nom :</p>
  <input type="text" placeholder="username" v-model="username">
  <p>{{ username }}</p>
  <br>
  <button>GO!</button>


</template>

<script>


export default {
  name: "NewQuizPage",
  data() {
    return {
    };
  },
  async created() {
    console.log("Composant New Quiz page 'Created'")
  }
};
</script>


<style>
</style>