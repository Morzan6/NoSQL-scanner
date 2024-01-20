<template>
  <div :id="niceId" class="chart"></div>
</template>

<script>
import { defineComponent } from "vue";
import { Chart } from "frappe-charts";
export default defineComponent({
  name: "Chart",
  props: {
    id: {
      default:'chart'
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
    niceId(){
      return `chart${this.id}`
    },
    data() {
      return  {
        height: 280,
        labels: this.state ? ["CVE НЕТ"] : ["LOW", "MEDIUM", "HIGH", "CRITICAL"],
        datasets: [
          {
            name: "CVEs",
            chartType: "line",
            values: this.state ? [1337] : [this.countLow, this.countMedium, this.countHigh, this.countCritical],
          },
        ],
      }
    },
    state() {
     
    if ( this.countLow !== 0 || this.countMedium !== 0 || this.countHigh !== 0 || this.countCritical !== 0) {
      return false
    } else {
      return true
    }
    }
  },
  mounted() {
    const chart = new Chart(`#${this.niceId}`, {
      tittle: "CVEs",
      data: this.data,
      type: "pie",
      height: 270,
      colors:
      this.state
          ? ["#2D2D2D"]
          : ["#FFEC8B", "#F8C373", "#EB8788", "#D62828"],
    });
    
  },
  methods: {
   checkHeight() {

   }
  }
});
</script>
<style scoped lang="sass">
.chart
 display: flex
 background: #FFF
 border-radius: 0.6875rem
 width: 310px
 padding: 0px
 box-shadow: 0px 27px 104.6px 0px rgba(0, 0, 0, 0.1)
 margin-bottom: 1rem
 

</style>
