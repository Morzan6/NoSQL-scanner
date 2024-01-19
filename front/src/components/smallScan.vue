<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "SmallScan",
  props: {
    id: {
      type: Number, 
    },
    name: {
      type: String,
      default: "I am your default scan",
    },
    ip: {
      type: String,
      default: "",
    },
    service: {
      default: "None",
    },
    timedelta: {
      type: String,
    },
  },
  computed: {
    serviceImage() {
      return `/db-icons/${this.service}.svg`;
    },
    linkToReport() {
      return `/report/${this.id}`;
    },
  },
});
</script>

<template>
  <a class="bar" :href="linkToReport">
    <p class="id">{{ id }}</p>
    <p class="name">{{ name }}</p>
    <p class="ip">{{ ip }}</p>
    <img class="service" :src="serviceImage" />
    <p class="timedelta">{{ timedelta }}</p>
  </a>
</template>

<style scoped lang="sass">
.bar
    width: inherit
    text-decoration: none
    color: #2D2D2D
    background: #FFF
    padding: 1.2rem 1.2rem 1.2rem
    font-size: 26px
    text-overflow: ellipsis

    align-items: center
    justify-content: space-between

    flex-flow: row wrap
    border-radius: 0.6875rem
    display: flex

    box-shadow: 0px 27px 104.6px 0px rgba(0, 0, 0, 0.05)
    margin-bottom: 1rem


    & > *:not(:last-child)
        margin-right: 2rem
    &:hover
        background: #F1F2F5
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
        width: 80%

.service
    width: auto
    height: 3.5rem
    flex-shrink: 0

.name
    width: 16rem
.timedelta
    width: 12rem
    color: #8D8A8A
    font-size: 22px
p
    margin: 0px 0px 0px
</style>
