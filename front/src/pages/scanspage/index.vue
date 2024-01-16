<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "ScanPage",
});
</script>

<template>
  <q-page-container class="background">
    <div class="columns">
      <div class="reports-column">
        list of reports
      </div>
      <div class="scan-column">
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

 
.columns 
  display: flex
  justify-content: space-between
  width: 95%
  height: 90vh
  margin-top: 2rem
  justify-items: center
 
.scan-column
  flex: 1
  background-color: red
  margin-top: 6rem

.reports-column 
  flex: 1.8
  background-color: red
  margin-right: 2rem

 
 </style>

