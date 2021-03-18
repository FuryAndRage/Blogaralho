<template>
    <div class="feed">
        <div class="container">
            <div class="row row-3">
                <feed-item v-for="post of posts" :post="post"></feed-item>
            </div>
        </div>
    </div>
</template>

<script>
import FeedItem from './FeedItem'

export default {
    name: 'Feed',
    components : {
        FeedItem
    },
    data () {
        return {
            posts : [
                {
                    title: 'Nome de um post',
                    id: '1',
                    url: '',
                    timestamp: '',
                    location: ''
                },
                {
                    title: 'Nome de um post 2',
                    id: '2',
                    url: '',
                    timestamp: '',
                    location: ''
                },
                {
                    title: 'Nome de um post 3',
                    id: '3',
                    url: '',
                    timestamp: '',
                    location: ''
                },
                {
                    title: 'Nome de um post 4',
                    id: '4',
                    url: '',
                    timestamp: '',
                    location: ''
                },
                {
                    title: 'Nome de um post 5',
                    id: '5',
                    url: '',
                    timestamp: '',
                    location: ''
                },
                {
                    title: 'Nome de um post 6',
                    id: '6',
                    url: '',
                    timestamp: '',
                    location: ''
                },
            ]
        }
    }
}
</script>

<style scoped>
</style>
