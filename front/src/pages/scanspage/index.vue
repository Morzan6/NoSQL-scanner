<script>
import { defineComponent } from "vue";
import smallScan from "../../components/smallScan.vue";



export default defineComponent({
  name: "ScanPage",
  components: {smallScan},
  component: ['smallScan']
});
</script>

<template>
  <q-page-container class="background">
    <div class="columns">
      <div class="scans-column">
        <smallScan />
        list of reports
      </div>
      <div class="start-scan-column">
        scanning component
        
      </div>
    </div>
  </q-page-container>
 </template>
 
 <style scoped lang="sass">
.report
 display: flex
 background-color: #F1F2F5
 margin-top: 4rem
 width: 20rem

 </style>

