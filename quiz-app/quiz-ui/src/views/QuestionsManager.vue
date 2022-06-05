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
        var test = await quizApiService.getQuizInfo();
        console.log(quizQuestion.data.text)
        console.log(test)
    },
    methods: {
        async loadQuestionByPosition() {

            console.log("Composant loadQuestionByPosition 'Created'")
        },
        async answerClickedHandler(position) {
            // recup position
            console.log("Composant answerClickedHandler 'Created'")
        },
        async endQuiz() {
            console.log("Composant endQuiz 'Created'")
        }
    }
};
</script>


<style>
</style>