<template>
  <h1>New Quiz Page</h1>
  <p>Saisissez votre nom :</p>
  <input type="text" v-model="username">
  <p>{{ username }}</p>
  <br>
  <button @click="launchNewQuiz">GO!</button>
</template>

<script>
//import participationStorageService from "@/ParticipationStorageService";

import ParticipationStorageService from '../services/ParticipationStorageService';

export default {

  name: "NewQuizPage",
  data() {
    return {
      username : ''
    };
  },
  methods:{
    launchNewQuiz(){
      console.log("Launch new quiz with", this.username);
      ParticipationStorageService.savePlayerName(this.username);
      // const playerName = participationStorageService.getPlayerName();
      // this.$router.push('/questions');
      this.$router.push('/manager');
    },
  },
  // async created() {
  //   console.log("Composant New Quiz page 'Created'")
  // }
};
</script>

<style>
</style>