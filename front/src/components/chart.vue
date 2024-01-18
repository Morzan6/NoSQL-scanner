<template>
  <div id="chart" class="chart"></div>
</template>

<script>
import { defineComponent } from "vue";
import { Chart } from "frappe-charts";
export default defineComponent({
  name: "Chart",
  props: {
    isEmpty: {
      type: Boolean,
      default: true
    },
    countLow: {
      type: Number,
      default: 0
    },
    countMedium: {
      type: Number,
      default: 0
    },
    countHigh: {
      type: Number,
      default: 0
    },
    countCritical: {
      type: Number,
      default: 0
    }
  },
  computed: {
    data() {
      return  {
        labels: this.isEmpty ? ["CVE НЕТ"] : ["LOW", "MEDIUM", "HIGH", "CRITICAL"],
        datasets: [
          {
            name: "CVEs",
            chartType: "line",
            values: this.isEmpty ? [1] : [this.countLow, this.countMedium, this.countHigh, this.countCritical],
          },
        ],
      }
    }
  },
  mounted() {
    const chart = new Chart("#chart", {
      tittle: "",
      data: this.data,
      type: "pie",
      height: 270,
      colors:
        this.isEmpty
          ? ["#2D2D2D"]
          : ["#FFEC8B", "#F8C373", "#EB8788", "#D62828"],
    });
  },
});
</script>
<style scoped lang="sass">
.chart
 display: flex
 background: #FFF
 border-radius: 0.6875rem
 width: 310px
 padding: 0px
 box-shadow: 0px 27px 104.6px 0px rgba(0, 0, 0, 0.05)
</style>
