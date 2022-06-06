<template>
  <h1>Scores Page</h1>
  <!--<QuestionManager :question="currentScore" @endQuiz="launchScores" />
  <button @click="launchScores">Get me the score</button>
  -->
  <button @click="returnHome">Home</button>
  <p>Bravo, votre score est de : {{this.currentScore}}</p>
  <table>
      <thead>
          <td>Date</td>
          <td>Player Name</td>
          <td>Score</td>
      </thead>
      <tbody v-for="score in scores" :key="score.Date">
        <tr>
          <td><p>{{score.date}}</p></td>
          <td><p>{{score.playerName}}</p></td>
          <td><p>{{score.score}}</p></td>
        </tr>
      </tbody>
  </table>
  <!-- <table>
      <thead>
          <td>Date</td>
          <td>Player Name</td>
          <td>Score</td>
      </thead>
      <tbody v-for="score in scores" :key="score.Date">
        <tr>
          <td><p>{{score.date}}</p></td>
          <td><p>{{score.playerName}}</p></td>
          <td><p>{{score.score}}</p></td>
        </tr>
      </tbody>
  </table> -->
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
      participationData : 0,
      scores : []
    };
  },
  
  async created() {
    this.participation();
  },

  methods:{
    async returnHome() {
        this.$router.push('/');
    },      ///console.log(ParticipationStorageService.getParticipationScore())
    async participation() {
      var participation = await quizApiService.getQuizInfo();
    //   console.log("participationData : ");
    //   console.log(participation.data);
      this.currentScore = ParticipationStorageService.getParticipationScore();

      for(var score of participation.data.scores) {
        //   console.log("Score : ")
        //   console.log(score)
          this.scores.push(score)
        //   console.log("val : " + val)
      }
    //   console.log(this.scores);
      //var quiz = await quizApiService.getQuizInfo();
      //console.log(quiz.data);
    },
  }
};
</script>

<style>
</style>