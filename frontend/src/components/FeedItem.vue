<template>
    <div class="card" v-if="post_is_public">
        <div class="card-body">
            <div class="">
                <hr noshade v-if="!post_image">
                <figure v-if="post_image">
                   <img v-bind:src="post_image" class="card-img-top" alt="">
                </figure>
                <Title :subtitle="true" :title="post_title" class="text-center"></Title>
                <div class="date">
                    <p> {{post_date}}</p>
                </div>
                <hr noshade v-if="!post_image">
            </div>
        </div>
    </div>

</template>
<script>
import Title from './Title.vue';

export default {
    name: 'feed-item',
    components : {
        Title
    },
    props: ['post'],
    created() {
        Object.assign(this,this.post);
    }
}

</script>

<style scoped>
    /* .feed-item {
        margin: 20px 0;
    }
    .feed-item:nth-child(1n+1) {
        border-right : 2px solid #212121;
    }
    .feed-item:nth-child(3n+3) {
        border-right: 0;
    }
    .feed-item .content {
        margin: 0 auto;
    }
    .feed-item .container.no-image {
        position: relative;
        height: 600px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-self: center;
    }
    .feed-item .container.no-image hr {
        display: block;
        width: auto;
        border-top : 1px solid #212121;
        border-bottom : 1px solid #212121;
    }
    .feed-item figure {
        margin: 0;
        padding: 0;
    }
    .feed-item .image {
        width: 100%;
        height: 600px;
        background-size: cover;
        background-position: center center;
    }
    .feed-item .date p {
        text-transform: uppercase;
        font-size: 12px;
        font-weight: bold;
        letter-spacing: -0.1em;
        margin: 0;
    } */
</style>
