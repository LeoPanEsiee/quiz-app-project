<template>
  <h1>Home page</h1>
  <router-link to="/start-new-quiz-page">Démarrer le quiz !</router-link>

  <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div>

</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: []
    };
  },
  async created() {
    console.log("Composant Home page 'Created'")
  }
};
</script>


<style>
</style>