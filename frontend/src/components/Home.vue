<template>
    <div class="home">
        <div class="container">
            <Menu></Menu>
            <Title :title="title" :border="true"></Title>
            <Feed></Feed>
        </div>
    </div>
</template>

<script>
import Menu from './Menu.vue';
import Title from './Title.vue';
import Feed from './Feed.vue';

export default {
    name: 'Home',
    components : {
        Menu,
        Title,
        Feed,
    },
    data () {
        return {
            title: 'Blogaralho'
        }
    }
}
</script>
