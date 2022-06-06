<template>
  <h1>Scores Page</h1>
  <!--<QuestionManager :question="currentScore" @endQuiz="launchScores" />
  <button @click="launchScores">Get me the score</button>

  -->
  
  <button @click="returnHome">Home</button>
  <p>Bravo, votre score est de : {{this.currentScore}}</p>
</template>



<script>

import ParticipationStorageService from '../services/ParticipationStorageService';
import quizApiService from "@/services/QuizApiService";

export default {
  name: "Scores",
  data() {
    return {
      username : '',
      
      currentScore : 0,
      participationData : 0
    };
  },
  
  async created() {
    this.launchScore();
    this.participation();
  },

  methods:{
    async returnHome() {
        this.$router.push('/');
    },      ///console.log(ParticipationStorageService.getParticipationScore())
    async participation() {
      var participation = await quizApiService.getQuizInfo();
      console.log("participationData : ");
      console.log(participation.data);


      //var quiz = await quizApiService.getQuizInfo();
      //console.log(quiz.data);
      

    },
  }
};
</script>

<style>
</style>