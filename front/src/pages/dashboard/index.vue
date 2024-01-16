<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "DashboardPage",
});
</script>

<template>
  <q-page-container class="background">
    <div class="columns">
      <div class="scans-column">
        3 scans with diogram
      </div>
      <div class="start-scan-column">
        scanning component
      </div>
    </div>
  </q-page-container>
 </template>
 
 <style scoped lang="sass">

.columns 
  display: flex
  justify-content: space-between
  width: 95%
  height: 90vh
  margin-top: 2rem
  justify-items: center
 
.start-scan-column
  flex: 1
  background-color: red
  margin-top: 6rem

.scans-column 
  flex: 1.8
  background-color: red
  margin-right: 2rem
 </style>
