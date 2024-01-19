<script>
import { defineComponent } from "vue";
import chart from "../../components/chart.vue";
import dashboardScan from "../../components/dashboardScan.vue";
import axios from "axios";
import formatTimeDelta from "../timedelta.js";

export default defineComponent({
  name: "DashboardPage",
  components: { chart, dashboardScan },
  component: ["chart", "dashboardScan"],
  beforeMount() {
    axios({
      method: "get",
      url: process.env.API + "/scan/my/",
      data: {},
      responseType: "json",
      headers: {
        ContextType: "application/jsom",
        Authorization: `Bearer ${localStorage.getItem("access_token")}`,
      },
    })
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
            headers: {
              ContextType: "application/jsom",
              Authorization: `Bearer ${localStorage.getItem("access_token")}`,
            },
          })
            .then((res) => {
              const newScans = [res.data, ...this.dashboardScans].sort(
                (a, b) => a.id - b.id
              );
              this.dashboardScans = [...newScans].reverse();
              console.log(this.dashboardScans);
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
    timeDelta(time) {
      return formatTimeDelta(time);
    },
    countVulns(data) {
      let vulns = 0;
      let cves = 0;
      if (typeof data.vulnerability_data.vulns != "undefined") {
        data.vulnerability_data.vulns.forEach((table) => {
          vulns += table.vulns.length;
        });
      }

      if (typeof data.vulnerability_data.cves != "undefined") {
        cves = data.vulnerability_data.cves.length;
      }

      return cves + vulns;
    },
    countScore(data) {
      const severityCounts = {};
      if (typeof data.vulnerability_data.cves == "undefined") {
        return {};
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
        <div v-for="scan in this.dashboardScans" :key="scan.id">
          <div class="bar">
            <chart
              :id="scan.id"
              :countLow="this.countScore(scan).LOW"
              :countMedium="this.countScore(scan).MEDIUM"
              :countHigh="this.countScore(scan).HIGH"
              :countCritical="this.countScore(scan).CRITICAL"
            />
            <dashboardScan
              :id="scan.id"
              :name="scan.name"
              :description="scan.description"
              :status="scan.status"
              :ip="scan.ip"
              :service="scan.type"
              :timedelta="timeDelta(scan.datetime)"
              :vulnNumber="this.countVulns(scan)"
            />
          </div>
        </div>
      </div>
      <div class="start-scan-column">scanning component</div>
    </div>
  </q-page-container>
</template>

<style scoped lang="sass">
.bar
  display: flex
</style>
