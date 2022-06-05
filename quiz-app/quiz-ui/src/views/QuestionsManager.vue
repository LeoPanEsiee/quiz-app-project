<template>
    <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestion }} </h1>
    <QuestionDisplay :question="currentQuestion" @answer-selected="answerClickedHandler" />
</template>

<script> 
import QuestionDisplay from "@/views/QuestionDisplay.vue";
import quizApiService from "@/services/QuizApiService";

export default {
    data() {
        return {
            currentQuestion: {
                questionImage : "",
                questionTitle : "No title",
                questionText : "No text",
                possibleAnswers : []
            },
            currentQuestionPosition : 1,
            totalNumberOfQuestion : 0
        };
    },
    components: {
        QuestionDisplay
    },
    async created() {
        console.log("Composant created 'Created'")
        var quizQuestion = await quizApiService.getQuestion(1);
        this.loadQuestionByPosition(quizQuestion.data.position);
    },
    methods: {
        async loadQuestionByPosition(position) {
            var quizQuestion = await quizApiService.getQuestion(position);
            var answers = [];
            var possibleAnswers = Object.entries(quizQuestion.data.possibleAnswers);
            console.log(possibleAnswers)
            for(var [key, val] of possibleAnswers)
                answers.push(val.text);
            this.currentQuestion.questionImage = quizQuestion.data.image;
            this.currentQuestion.questionTitle = quizQuestion.data.title;
            this.currentQuestion.questionText = quizQuestion.data.text;
            this.currentQuestion.possibleAnswers = answers;
        },
        async answerClickedHandler(position) {
            // Verifie la rep
            // Incremente score si correcte
            console.log("Composant answerClickedHandler 'Created'")
            var quiz = await quizApiService.getQuizInfo();
            if(position == quiz.data.size) {
                this.endQuiz();
            }

            this.loadQuestionByPosition(position + 1);
        },
        async endQuiz() {
            console.log("Composant endQuiz 'Created'")
        }
    }
};
</script>


<style>
</style>