<template>
    <div class="feed-item column column-33">
        <div class="container">
            <div class="content">
                <figure>
                    <img src="https://images.unsplash.com/photo-1615915768736-3520426009d5?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1534&q=80" />
                </figure>
                <Title :subtitle="true" :title="title"></Title>
                <div class="date">
                    <p> January 7, 2021 </p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Title from './Title';

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
    .feed-item {
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
        padding-left: 10px;
        padding-right: 10px;
    }
    .feed-item figure {
        margin: 0;
        padding: 0;
    }
    .feed-item .date p {
        text-transform: uppercase;
        font-size: 12px;
        font-weight: bold;
        letter-spacing: -0.1em;
        margin: 0;
    }
</style>
