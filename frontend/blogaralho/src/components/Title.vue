<template>
    <h1 v-if="!subtitle" :class="border ? 'title border' : 'title'" >{{title}}</h1>
    <h3 v-else :class="border ? 'subtitle border' : 'subtitle'" >{{title}}</h3>
</template>

<script>
export default {
    name: 'Title',
    props: ['title','border','subtitle']
}
</script>

<style scoped>
    .title {
        display: block;
        color: #212121;
        text-align: center;
        padding: 8px;
    }
    .subtitle {
        color: #212121;
        text-align: left;
        margin: 8px 0;
    }
    .title.border {
        border-top: 2px solid #212121;
        border-bottom: 2px solid #212121;
    }
</style>
