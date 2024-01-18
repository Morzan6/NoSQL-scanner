<script>
import { defineComponent } from "vue";
import chart from "../../components/chart.vue";
import axios from "axios";
import requestSender from "components/request-sender";

export default defineComponent({
  name: "DashboardPage",
  components: { chart },
  component: ["chart"],
  beforeMount() {
    axios({
      method: "get",
      url: process.env.API + "/scan/my/",
      data: {},
      responseType: "json",
      headers: { ContextType: "application/jsom", Authorization: `Bearer ${localStorage.getItem("access_token")}`}
    }
    )
      .then((res) => {
        const scans = res.data;
        this.isLoading = false;

        const oldScans = scans.slice(-3);

        oldScans.forEach((scan) => {
          axios({
            method: "get",
            url: process.env.API + "/scan/get/?id=" + scan.id,
            data: {},
            responseType: "json",
            headers: { ContextType: "application/jsom", Authorization: `Bearer ${localStorage.getItem("access_token")}`}
          }
          )
            .then((res) => {
              console.log(res.data)
              const newScans = [res.data, ...this.dashboardScans].sort()
              this.dashboardScans = [...newScans].reverse()
              console.log(this.dashboardScans)
            })
            .catch((err) => this.showNotify(err.response.data.detail));
        });
      })
      .catch((err) => this.showNotify(err.response.data.detail));
  },
  data() {
    return {
      dashboardScans: [],
      isLoading: true,
    };
  },
  methods: {
    countScore(data) {
      const severityCounts = {};
      if(typeof data.vulnerability_data.cves == 'undefined'){
        return {}
      }
      data.vulnerability_data.cves.forEach((entry) => {
        const severity = entry.base_severity_v2;
        if (severity) {
          severityCounts[severity] = (severityCounts[severity] || 0) + 1;
        }
      });
      return severityCounts;
    },
  },
});
</script>

<template>
  <q-page-container class="background">
    <div class="columns">
      <div class="scans-column">
        <img class="loading" src="/loading3.svg" v-if="isLoading" />
        <div v-for="scan in this.dashboardScans " :key="scan.id">
          <div>
            <chart
              :id="scan.id"
              :countLow="this.countScore(scan).LOW"
              :countMedium="this.countScore(scan).MEDIUM"
              :countHigh="this.countScore(scan).HIGH"
              :countCritical="this.countScore(scan).CRITICAL"
            />
          </div>
        </div>
      </div>
      <div class="start-scan-column">scanning component</div>
    </div>
  </q-page-container>
</template>

<style scoped lang="sass"></style>
