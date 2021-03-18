<template>
    <div id="app">
        <div class="container">
            <router-view/>
        </div>
    </div>
</template>

<script>
export default {
    name: 'App'
}
</script>

<style>
    body {
        font-family: 'halyard-display', sans-serif;
        font-size: 15px;
        margin: 0;
        -moz-osx-font-smoothing: grayscale;
        -webkit-font-smoothing: antialiased;
        overscroll-behavior-y: none;
        background-color: #fdfdfd;
    }

    body::after {
        animation: grain 6s steps(10) infinite;
        background-image: url('./assets/grain.png');
        background-repeat: repeat;
        content: '';
        height: 300%;
        left: -100%;
        opacity: .02;
        pointer-events: none;
        position: fixed;
        top: -100%;
        transition: opacity 0.1s ease;
        width: 300%;
        will-change: transform;
        z-index: 3;
    }

    @keyframes grain {
        0% { transform: translate(20%, -15%) }
        10% { transform: translate(-20%, -15%) }
        20% { transform: translate(20%, -5%) }
        30% { transform: translate(-20%, -5%) }
        40% { transform: translate(20%, 5%) }
        50% { transform: translate(-20%, 5%) }
        60% { transform: translate(20%, 15%) }
        70% { transform: translate(-20%, 15%) }
        80% { transform: translate(20%, 5%) }
        90% { transform: translate(-20%, 5%) }
        100% { transform: translate(20%, -5%) }
    }

    .app {
        padding: 0 2.0rem;
    }
</style>
