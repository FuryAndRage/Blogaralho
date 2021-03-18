<template>
    <div class="menu">
        <div class="container">
            <div class="row">
                <div class="column column-90">
                    <ul>
                        <li class="button button-clear" v-for="{label,url} of items" :key="label">
                            <a :href="url">
                                {{label}}
                            </a>
                        </li>
                    </ul>
                </div>
                <div class="column column-10">
                    <div class="search">
                        Search
                    </div>
                </div>
            </div>
        </div>
    </div>
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
        padding: 0;
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
</style>
