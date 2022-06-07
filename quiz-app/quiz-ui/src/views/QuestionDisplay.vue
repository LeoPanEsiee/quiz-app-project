<template>
    <h2>{{ question.questionTitle }}</h2>
    <img class="questionImage" v-if="question.questionImage" :src="question.questionImage" />
    <h3>{{ question.questionText }}</h3>
    <p>Veuillez selectionner une réponse :</p>
    <ul>
        <li v-for="answer in question.possibleAnswers" :key="answer">
            <a @click="$emit('answer-selected', question.possibleAnswers.indexOf(answer) + 1)">{{ answer }}</a>
        </li>
    </ul>


</template>

<script>
export default {
    name: "QuestionDisplay",
    emits: ["answer-selected"],
    props: {
        question: {
            type: Object
        }
    },
    data() {
        return {
        };
    }
    // methods: {
    //     answerSelected(event) {
    //         this.$emit('answer-selected', question.possibleAnswers);
    //     }
    // }
};
</script>


<style>
.questionImage {
    height: 100%;
    width: 100%;
    max-width: 300px;
    max-height: 300px;
}
</style>