<template>
    <div class="home">
        <Menu></Menu>
        <Title :title="title" :border="true"></Title>
        <Feed></Feed>
    </div>
</template>

<script>
import Menu from './Menu';
import Title from './Title';
import Feed from './Feed';

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

<style scoped>

</style>
