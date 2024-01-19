<template>
  <div v-if="isOpen" class="modal">
    <div class="modal-content">
      <div class="row">
        <p class="name">{{ name }}</p>
        <div style="display: flex">
          <p
            :style="{
              'font-weight': 600,
              'font-size': '30px',
              color: this.color(severity),
              'margin-right': '10rem',
            }"
          >
            {{ severity }}
          </p>
          <p :style="{ 'font-weight': 600, 'font-size': '30px' }">
            {{ score }}
          </p>
        </div>
        <button @click="closeModal"><img src="/cross.svg" /></button>
      </div>
      <div class="row">
        <p>ОПИСАНИЕ</p>
      </div>
      <div class="data">
        <p>{{ description }}</p>
      </div>
      <div class="row">
        <p>РЕКОМЕНДАЦИИ</p>
      </div>
      <div class="data">
        <!-- {{ markdownToHtml }} -->
        <div class="markdown" v-html="markdownToHtml"></div>
      </div>
    </div>
  </div>
</template>

<script>
import { marked } from 'marked';
import { defineComponent } from "vue";
export default defineComponent({
  name: "modalCVE",
  props: {
    isOpen: Boolean,
    closeModal: Function,
    score: {
      type: String,
      default: "6.0",
    },
    severity: {
      type: String,
      default: "LOW",
    },
    name: {
      type: String,
      default: "CVE-2024-1234",
    },
    description: {
      type: String,
      default: "Описание CVE",
    },
    recomendation: {
      type: String,
      default: "Рекомендация к  СVE",
    },
  },
  computed: {
   markdownToHtml(){
     return marked(this.recomendation, {breaks: true, pedantic: true});
    }
  },
  methods: {
    color(sev) {
      const colors = {
        LOW: "#FFEC8B",
        MEDIUM: "#F8C373",
        HIGH: "#EB8788",
        CRITICAL: "#D62828",
      };
      return colors[sev];
    },
  },
});
</script>

<style scoped lang="sass">
button
  border: none
  background: none
  img
    height: 3rem
.modal
    position: fixed

    top: 0
    left: 0
    width: 100%
    height: 100%
    background: rgba(0, 0, 0, 0.5)
    box-shadow: 0px 4px 21.4px 0px rgba(0, 0, 0, 0.25)
    display: flex
    justify-content: center
    align-items: center


.modal-content
    display: flex

    background: #FFF
    padding: 20px
    width: 80rem
    height: 50rem
    padding: 2rem
    border-radius: 0.9rem
    overflow: auto
    overflow-x: hidden
    flex-direction: column
    font-family: "Inter", sans-serif

    .row
        justify-content: space-between
        display: flex
        width: 100%
        height: 4rem
        margin-top: 1rem
        margin-bottom: 1rem

        .name
            align-self: center
            font-size: 30px
            font-weight: 600

            &::after
                content: ''
                display: block
                height: 4px
                border-radius: 10px
                background: #D62828
                width: 100%
        p
            align-self: center
            font-size: 26px
            font-weight: 400
.data
    display: flex
    background: #F1F2F5
    width: auto
    font-size: 20px
    border-radius: 0.9rem
    padding: 2rem
    height: auto


</style>
