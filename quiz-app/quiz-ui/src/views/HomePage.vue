<template>
  <h1>Home page</h1>
  <router-link to="/start-new-quiz-page">Démarrer le quiz !</router-link>
  
  <h2>Classement</h2>
  <div v-for="scoreEntry in registeredScores" v-bind:key="scoreEntry.date">
    {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";
import participationStorageService from '../services/ParticipationStorageService';

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: []
    };
  },
  async created() {
    console.log("Composant Home page 'Created'")
    
    var participation = await quizApiService.getQuizInfo();

    for(var score of participation.data.scores) {
        this.registeredScores.push(score);
    }
    
  }
};
</script>


<style>
</style>