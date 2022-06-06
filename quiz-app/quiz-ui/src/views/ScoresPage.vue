<template>
  <h1>Scores Page</h1>
  <QuestionManager :question="currentScore" @endQuiz="launchScores" />
  <button @click="returnHome">Home</button>
</template>

<script>
export default {
  name: "Scores",
  data() {
    return {
      username : ''
    };
  },
  methods:{
    returnHome() {
        this.$router.push('/');
    },
    launchScores(currentScore) {
      console.log("Launch scores page")
      console.log(currentScore)
    }
  }
};
</script>

<style>
</style>