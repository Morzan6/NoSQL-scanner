<script>
import { defineComponent } from "vue";


export default defineComponent({
  name: "ReportPage",
  props: ['id']
});
</script>

<template>
  <q-page-container class="background">
    <div class="columns">
      <div class="scans-column">
        report information {{ id }}
      </div>
      <div class="start-scan-column">
        scanning component
      </div>
    </div>
  </q-page-container>
 </template>
 
 <style scoped lang="sass">

 </style>
