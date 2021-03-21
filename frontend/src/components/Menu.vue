<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
            <!-- <a class="navbar-brand" href="#">Blogaralho</a> -->
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="#">Home</a>
                </li>
                <li class="nav-item" v-for="{label,url} of items" :key="label">
                    <a class="nav-link" :href="url">
                        {{label}}
                    </a>
                </li>
            </ul>
            <form class="d-flex">
                <input class="form-control me-2 shadow-none" type="search" placeholder="Search" aria-label="Search">
                <button class="btn btn-outline-dark" type="submit">Search</button>
            </form>
            </div>
        </div>
    </nav>
</template>

<script>
export default {
    name: 'Menu',
    data () {
        return {
            items : [
                {
                    url: '#/item1',
                    label : 'item 1',
                    active : false,
                },
                {
                    url: '#/item2',
                    label : 'item 2',
                    active : false,
                },
                {
                    url: '#/item3',
                    label : 'item 3',
                    active : false,
                },
            ]
        }
    }
}
</script>

<style scoped>
    .menu {
        padding-top: 10px;
        padding-bottom: 15px;
    }
    .menu .row {
        height: 40px;
    }
    .menu .column {
        display: flex;
        flex-direction: row;
        justify-content: flex-end;
    }
    .menu .search {
        cursor: pointer;
        display: inline-block;
        font-size: 1.1rem;
        font-weight: 700;
        height: 3.8rem;
        letter-spacing: .1rem;
        line-height: 3.8rem;
        text-align: center;
        text-decoration: none;
        text-transform: uppercase;
        white-space: nowrap;
        margin-bottom: 1.0rem;
    }
    .menu .button a {
        color: #000;
    }
    .nav-link:hover{
        background-color:#212529;
        color: #fff;
        transition-duration: 0.4s;
        
    }
    .nav-link{
        transition-duration: 0.4s
    }
    
</style>
