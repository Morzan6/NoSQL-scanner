<script>
import { defineComponent } from "vue";
import chart from "../../components/chart.vue"
import requestSender from "components/request-sender";

export default defineComponent({
  name: "DashboardPage",
  components: { chart },
  component: ['chart'],
  beforeMount() {
    const resp = requestSender(
      "get",
      process.env.API + "/scan/my/",
      {},
      localStorage.getItem("access_token")
    );
    resp
      .then((res) => {
        this.scans = res.data;
        this.isLoading = false;
      })
      .catch((err) => this.showNotify(err.response.data.detail));
    this.lastScans();
  },
  data() {
    return {
      scans: [],
      dashboardScans: []
    };
  },
  methods: {
    lastScans() {
      const oldScans = this.scans.slice(-3)

      oldScans.forEach(scan => {
        requestSender(
          "get",
          process.env.API + "/scan/get/?id=" + scan.id,
          {},
          localStorage.getItem("access_token")
        ).then((res) => {
          this.dashboardScans.push(res.data)
        })
          .catch((err) => this.showNotify(err.response.data.detail));
      })


    },
  }
}
);

</script>

<template>
  <q-page-container class="background">
    <div class="columns">
      <div class="scans-column">
        <chart />
        {{ this.dashboardScans }}
      </div>
      <div class="start-scan-column">scanning component</div>
    </div>
  </q-page-container>
</template>

<style scoped lang="sass">
</style>
