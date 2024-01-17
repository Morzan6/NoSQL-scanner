<script>
import { defineComponent } from "vue";

export default defineComponent({
    name: "SmallScan",
    props: {
        id: {
            type: Number,
            default: 0
        },
        name: {
            type: String,
            default: "I am your default scan"
        },
        ip: {
            type: String,
            default: "123.123.123.123"
        },
        service: {
            default: 'redis'
        },
        timedelta: {
            type: String,
            default: "1 сек. назад"
        }
    },
    computed: {
        serviceImage() {
            return `../../public/db-icons/${this.service}.png`;
        }
    }
});

</script>

<template>
    <div class="bar">
        <p class="id">{{ id }}</p>
        <p class="name">{{ name }}</p>
        <p class="ip">{{ ip }}</p>
        <img class="service" :src="serviceImage">
        <p class="timedelta">{{ timedelta }}</p>
    </div>
</template>

<style scoped lang="sass">
.bar
    width: inherit
    background: #F1F2F5
    padding: 1.2rem 1rem 1.2rem
    font-size: 26px
    text-overflow: ellipsis
    
    align-items: center
    justify-content: space-between
    
    flex-flow: row wrap
    border-radius: 10px
    display: flex
    
    box-shadow: rgba(0, 0, 0, .05) 0 27px 104.6px

    & > *:not(:last-child)
        margin-right: 2rem
.id
    width: 2rem
    color: #8D8A8A
.ip
    width:12rem

    &::after
        content: ''
        display: block
        height: 4px
        border-radius: 10px
        background: #D62828
        width: 100%
    
.service
    width: auto
    height: 4.5rem
    flex-shrink: 0

.name
    width: 20rem
.timedelta
    width: 10rem
    color: #8D8A8A
p
    margin: 0px 0px 0px
</style>