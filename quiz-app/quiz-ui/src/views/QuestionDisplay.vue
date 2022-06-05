<template>
    <img v-if="question.image" :src="question.image" />
    <h2>{{question.questionTitle}}</h2>
    <h3>{{question.questionText}}</h3>
    <p>Veuillez selectionner une réponse :</p>
    <ul>
        <li v-for="item in question.possibleAnswers" :key="item.text">
            <a @click="$emit('answer-selected', 2)">{{item}}</a>
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
};
</script>


<style>
</style>