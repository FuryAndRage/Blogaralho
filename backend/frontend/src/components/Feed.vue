<template>
    <div class="feed">
        <div class="row row-3">
            <feed-item v-for="post of posts" :post="post" :key="post.id"></feed-item>
        </div>
    </div>
</template>

<script>
import FeedItem from './FeedItem.vue'

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
                    image : {
                        src : 'https://images.unsplash.com/photo-1497262693247-aa258f96c4f5?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTl8fHRyYXZlbHxlbnwwfDF8MHw%3D&auto=format&fit=crop&w=500&q=60'
                    },
                    timestamp: '',
                    location: '',
                },
                {
                    title: 'Nome de um post 2',
                    id: '2',
                    url: '',
                    image : {
                        src : 'https://images.unsplash.com/photo-1505142468610-359e7d316be0?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MTd8fHRyYXZlbHxlbnwwfDF8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60'
                    },
                    timestamp: '',
                    location: '',
                },
                {
                    title: 'Nome de um post 3',
                    id: '3',
                    url: '',
                    image : {
                        src : 'https://images.unsplash.com/photo-1527631746610-bca00a040d60?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MjB8fHRyYXZlbHxlbnwwfDF8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60'
                    },
                    timestamp: '',
                    location: '',
                },
                {
                    title: 'Nome de um post 4',
                    id: '4',
                    url: '',
                    image : {
                        src : 'https://images.unsplash.com/photo-1520466809213-7b9a56adcd45?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MjR8fHRyYXZlbHxlbnwwfDF8MHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60'
                    },
                    timestamp: '',
                    location: '',
                },
                {
                    title: 'Nome de um post 5',
                    id: '5',
                    url: '',
                    image : {
                        src : ''
                    },
                    timestamp: '',
                    location: '',
                },
                {
                    title: 'Nome de um post 6',
                    id: '6',
                    url: '',
                    image : {
                        src : 'https://images.unsplash.com/photo-1527605158555-853f200063e9?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=619&q=80'
                    },
                    timestamp: '',
                    location: '',
                },
            ]
        }
    }
}
</script>

<style scoped>
</style>
