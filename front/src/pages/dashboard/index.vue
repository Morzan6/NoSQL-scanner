<script>
import { defineComponent } from "vue";
import chart from "../../components/chart.vue"
export default defineComponent({
  name: "DashboardPage",
  components: {chart},
  component: ['chart']
});
</script>

<template>
  <q-page-container class="background">
    <div class="columns">
      <div class="scans-column">
        <chart />
        3 scans with diogram
      </div>
      <div class="start-scan-column">scanning component</div>
    </div>
  </q-page-container>
</template>

<style scoped lang="sass">
</style>
