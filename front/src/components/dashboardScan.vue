<template>
  <div class="scan-container">
    <div class="scan-bar">
        <div class="first-bar">
            <p class="name">{{ name }}</p>
            <p >{{ ip }}</p>
        </div>
        <div class="second-bar">
            <p class="description">{{ description}}</p>
            <p class="vulns">Уязвимостей: {{ vulnNumber }}</p>
        </div>
        <div class="third-bar">
            <div>
                <img class="service" :src="serviceImage" />
                <p> {{ status }} </p>
            </div>
            <p class="timedelta">{{ timedelta }}</p>
        </div>
    </div>
    <div style="display: flex; justify-content: flex-start">
        <a class="button" :href="'/static/'">Скачать отчёт</a>
        <a class="button" :href="linkToReport">Подробнее</a>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "vue";
export default defineComponent({
  name: "dashboardScan",
  props: {
    id: {
      type: Number, 
    },
    name: {
      type: String,
      default: "I am your default scan",
    },
    description: {
        type: String,
        default: "This is scan"
    },
    status: {
        type: String,
        default: "UNKNOWN"
    },
    vulnNumber: {
        type: Number,
        default: 0
    },
    ip: {
      type: String,
      default: "123.123.123.123",
    },
    service: {
      default: "None",
    },
    timedelta: {
      type: String,
      default: " 1 сек. назад"
    },
    pdf: {
        default: ""
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
  mounted() {},
  methods: {},
});
</script>
<style scoped lang="sass">
.third-bar
    display: flex
    align-items: center
    justify-content: space-between
    margin-top: auto
    .timedelta
        font-weight: 500
        font-size: 20px
        color: #8D8A8A
    & div
        display: flex
        align-items: center
        max-width: 12rem
        justify-content: space-between
        .service
            width: auto
            height: 2rem
            flex-shrink: 0
        & p
            margin-left: 1rem 
            font-size: 22px
            font-weight: 400
            color: #2D2D2D


.second-bar
    display: flex
    margin-top: 1rem
    justify-content: space-between
    .description
        font-size: 18px
        color: #2D2D2D
        text-overflow: ellipsis
        max-width: 28rem
        font-weight: 400
    .vulns
        font-size: 20px
        font-weight: 500
        color: #8D8A8A
    
.first-bar
    display: flex
    
    justify-content: space-between
    font-size: 28px
    color: #2D2D2D
    font-weight: 400
    .name
        max-width: 28rem
        text-overflow: ellipsis
        &::after
            content: ''
            display: block
            height: 4px
            border-radius: 10px
            background: #D62828
            width: 100%
p
 margin: 0
.scan-bar
 font-family: "Inter", sans-serif
 box-shadow: 0px 27px 104.6px 0px rgba(0, 0, 0, 0.05)
 display: flex
 border-radius: 0.6875rem
 background: #FFF
 padding: 1rem 2rem 1rem
 width: 48rem
 height: 13rem
 margin-left: 1rem
 flex-direction: column
 @media screen and (max-width: 1600px)
  width: 50rem
 @media screen and (max-width: 1200px)
  width: 34rem
 @media screen and (max-width: 900px)
  width: 100%
 
.button
 margin-left: 1rem
 box-shadow: 0px 27px 104.6px 0px rgba(0, 0, 0, 0.05)
 text-decoration: none
 margin-top: 1rem
 border-radius: 1rem
 background: #FFF
 padding: 0.6875rem
 width: 12rem
 height: 3rem
 display: flex
 align-items: center
 justify-content: center
 font-family: "Inter", sans-serif
 font-size: 14px
 color: #2D2D2D
 font-weight: 600
 border: none

 &:hover
    background: #E8E8E8
</style>
