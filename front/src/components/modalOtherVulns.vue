<template>
  <div v-if="isOpen" class="modal">
    <div class="modal-content">
      <div class="row">
        <p class="name">ДРУГИЕ УЯЗВИМОСТИ</p>
        <div style="display: flex">
          
          
         
        </div>
        <button class="exit" @click="closeModal"><img src="/cross.svg" /></button>
      </div>
      <div v-for="tabels in vulns" :key="tabels">
        <div class="data" v-for="vuln in tabels.vulns" :key="vuln">
            {{ vuln.description }}
        </div>
       
      </div>
    </div>
  </div>
</template>

<script>
import { marked } from "marked";
import { defineComponent } from "vue";
export default defineComponent({
  name: "modalOtherVulns",
  props: {
    isOpen: Boolean,
    closeModal: Function,
    vulns: Array,
  },
  computed: {},
  methods: {},
});
</script>

<style scoped lang="sass">
.exit
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
    padding: 1rem
    height: auto
    margin-top: 1rem
</style>
