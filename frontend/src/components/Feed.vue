<template>
    <div class="feed">
        <div class="row justify-content-center">
            <feed-item v-for="post of posts" :post="post" :key="post.id" class="col-md-4 col-lg-4"></feed-item>
        </div>
    </div>
</template>

<script>
import FeedItem from './FeedItem.vue'
import axios from 'axios';

const getHeaders =() => {
    const getCookie = () => {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) { 
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    axios.defaults.xsrfHeaderName = "X-CSRFToken";
    const csrftoken = getCookie('csrftoken');
    const headers = {"X-CSRFTOKEN": csrftoken}

      return headers;
}

export default {
    name: 'Feed',
    components : {
        FeedItem
    },
    data () {
        return {
            posts : []
        }
    },
    created() {
        axios.get('http://localhost:8000/api/post/posts/?format=json').then(({data}) => {
            this.posts = data;
        });
        // axios.post(
        //     'http://localhost:8000/api/post/posts/?format=json',
        //     {
        //         "post_title": "teste 3",
        //         "post_content": "teste 3",
        //         "post_image": "null",
        //         "post_location": "teste",
        //         "post_category": 1
        //     },
        //     getHeaders()
        // )
    }
}
</script>

<style scoped>
</style>
