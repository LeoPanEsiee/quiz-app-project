<template>
    <img v-if="question.image" :src="question.image" />
    <a @click="$emit('answer-selected', 2)">La réponse D</a>
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