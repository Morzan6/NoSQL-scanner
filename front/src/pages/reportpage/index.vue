<script>
import { defineComponent } from "vue";
import axios from "axios";
import formatTimeDelta from "../timedelta.js";
import chart from "../../components/chart.vue";
import modalCVE from "../../components/modalСVE.vue";
import startScan from "../../components/startScan.vue";
import modalOtherVulns from "../../components/modalOtherVulns.vue";

export default defineComponent({
  name: "ReportPage",
  props: ["id"],
  components: { chart, modalCVE, modalOtherVulns, startScan },
  component: ["chart"],
  data() {
    return {
      scan: [],
      isLoading: true,
      modalOpen: [],
      modalOtherOpen: false,
      openStart: false,
      linkToReport: ""
    };
  },
  beforeMount() {
    let id = this.$route.params.id;

    axios({
        method: "get",
        url: process.env.API + "/scan/report/?id=" + id,
        data: {},
        responseType: "json",
        headers: {
          ContextType: "application/jsom",
          Authorization: `Bearer ${localStorage.getItem("access_token")}`,
        }, 

      }).then((res) => {
        this.linkToReport =  "/static" + res.data.path;
      })

    

    axios({
      method: "get",
      url: process.env.API + "/scan/get/?id=" + id,
      data: {},
      responseType: "json",
      headers: {
        ContextType: "application/jsom",
        Authorization: `Bearer ${localStorage.getItem("access_token")}`,
      },
    })
      .then((res) => {
        this.scan = res.data;
        this.isLoading = false;
      })
      .catch((err) => {
        this.$router.push("/dashboard");
      });
  },
  methods: {
    timeDelta(time) {
      return formatTimeDelta(time);
    },
    countScore(data) {
      const severityCounts = {};
      if (typeof data.vulnerability_data?.cves == "undefined") {
        return {};
      }
      data.vulnerability_data.cves.forEach((entry) => {
        let severity = entry.base_severity_v3;
        if (entry.base_severity_v3 === "") {
          severity = entry.base_severity_v2;
        }
        if (severity) {
          severityCounts[severity] = (severityCounts[severity] || 0) + 1;
        }
      });
      return severityCounts;
    },
    countVulns(data) {
      const counts = { CVEs: 0, Other: 0 };
      if (typeof data.vulnerability_data?.cves != "undefined") {
        counts.CVEs = data.vulnerability_data.cves.length;
      }

      if (typeof data.vulnerability_data?.vulns != "undefined") {
        let vulns = 0;
        data.vulnerability_data.vulns.forEach((table) => {
          vulns += table.vulns.length;
        });

        counts.Other = vulns;
      }

      return counts;
    },
    score(cve) {
      if (cve.base_score_v3 === "") {
        return cve.base_score_v2;
      }
      return cve.base_score_v3;
    },
    severity(cve) {
      if (cve.base_severity_v3 === "") {
        return cve.base_severity_v2;
      }
      return cve.base_severity_v3;
    },
    colorCVE(sev) {
      const colors = {
        LOW: "#FFEC8B",
        MEDIUM: "#F8C373",
        HIGH: "#EB8788",
        CRITICAL: "#D62828",
      };
      return colors[sev];
    },
    openModal(index) {
      this.modalOpen[index] = true;
    },
    closeModal(index) {
      this.modalOpen[index] = false;
    },
  },
  computed: {
    serviceImage() {
      return `/db-icons/${this.scan.type}.svg`;
    },
  },
});
</script>

<template>
  <q-page-container class="background">
    <div class="columns">
      <div class="scans-column">
        <button class="mobile-start-scan" @click="openStart = !openStart">
          Сканировать 
        </button>
        <startScan class="start-modal" v-if="openStart"/>
        <img class="loading" src="/loading3.svg" v-if="isLoading" />
        <div class="main-container" v-if="!isLoading">
          <div class="row">
            <p class="name">{{ scan.name }}</p>
            <p class="time">{{ timeDelta(scan.datetime) }}</p>
          </div>
          <div class="row">
            <p class="description">{{ scan.description }}</p>
            <div style="display: flex">
              <img class="service" :src="serviceImage" />
              <p class="version">{{ scan.version }}</p>
            </div>
          </div>
          <div class="middle-row">
            <div class="info">
              <div class="f-column">
                <p class="status">{{ scan.status }}</p>
                <div>
                  ID
                  <p>{{ scan.id }}</p>
                </div>
                <div>
                  Порт
                  <p>{{ scan.port }}</p>
                </div>
              </div>
              <div class="s-column">
                <div>
                  CVEs
                  <p>{{ countVulns(this.scan).CVEs }}</p>
                </div>
                <div>
                  Другие
                  <p>{{ countVulns(this.scan).Other }}</p>
                </div>
                <div>
                  IP
                  <p>{{ scan.ip }}</p>
                </div>
              </div>
            </div>
            <div class="chart">
              <chart
                :id="scan.id"
                :countLow="this.countScore(scan).LOW"
                :countMedium="this.countScore(scan).MEDIUM"
                :countHigh="this.countScore(scan).HIGH"
                :countCritical="this.countScore(scan).CRITICAL"
              />
            </div>
          </div>
          <div class="cve-list">
            <div class="cve" v-if="countVulns(this.scan).CVEs === 0">
              СVE не найдено
            </div>
            <div v-else>
              <div
                v-for="(cve, index) in scan.vulnerability_data.cves"
                :key="index"
              >
                <button class="cve" @click="openModal(index)">
                  <p>{{ cve.id }}</p>
                  <p :style="{ color: this.colorCVE(this.severity(cve)) }">
                    {{ this.severity(cve) }}
                  </p>
                  <p>{{ this.score(cve) }}</p>
                </button>
                <modalCVE
                  :isOpen="modalOpen[index]"
                  :closeModal="() => closeModal(index)"
                  :name="cve.id"
                  :severity="this.severity(cve)"
                  :score="this.score(cve).toString()"
                  :description="cve.description"
                  :recomendation="cve.rec"
                ></modalCVE>
              </div>
            </div>
          </div>
          <div class="other-list">
            <button
              class="cve"
              @click="modalOtherOpen = !modalOtherOpen"
              v-if="countVulns(this.scan).Other !== 0"
              style="width: 60%; display: flex; flex-direction: row"
            >
              ДРУГИЕ УЯЗВИМОСТИ
              <p style="margin-left: 2rem; color: #8d8a8a">
                {{ countVulns(this.scan).Other }}
              </p>
            </button>
            <modalOtherVulns
              :vulns="scan.vulnerability_data.vulns"
              :isOpen="modalOtherOpen"
              :closeModal="
                () => {
                  modalOtherOpen = false;
                }
              "
            />
            <a
              class="button"
              :href="linkToReport"
              v-if="
                countVulns(this.scan).CVEs !== 0 ||
                countVulns(this.scan).Other !== 0
              "
              >СКАЧАТЬ ОТЧЁТ</a
            >
          </div>
        </div>
      </div>
      <div class="start-scan-column"><startScan /></div>
    </div>
  </q-page-container>
</template>

<style scoped lang="sass">
.chart
  @media screen and (max-width: 700px)
    margin-top: 1rem
    
.middle-row
  display: flex

  flex-direction: row
  justify-content: space-between
  align-items: center

  @media screen and (max-width: 700px)
    flex-direction: column
    align-items: start
    

.other-list
  display: flex
  align-items: center
  .button
    margin-left: 1rem
    box-shadow: 0px 27px 104.6px 0px rgba(0, 0, 0, 0.3)
    text-decoration: none
    margin-top: 1rem
    border-radius: 1rem
    background: #FFF
    padding: 0.6875rem
    min-width: 6rem
    height: 3rem
    display: flex
    align-items: center
    justify-content: center
    font-family: "Inter", sans-serif
    font-size: 14px
    color: #2D2D2D
    font-weight: 600
    border: none
    &:hover
      background: #E8E8E8
.cve
  background: #F1F2F5
  padding: 1rem
  border-radius: 0.7rem
  font-size: 24px
  width: 100%
  border: none
  font-weight: 500
  display: flex
  justify-content: space-between
  margin-top: 1rem
  p:not(:last-child)
    width: 30%
    align-self: center
  p:last-child
    width: 5rem
    align-self: center
  &:hover
    background: #D0D0D0
.main-container
 font-family: "Inter", sans-serif
 background: #fff
 width: inherit
 box-shadow: 0px 27px 104.6px 0px rgba(0, 0, 0, 0.05)
 display: flex
 padding: 3rem
 height: 90vh
 border-radius: 0.9rem
 overflow: auto
 flex-direction: column
 overflow-x: hidden
 color: #2D2D2D
 @media screen and (max-width: 700px)
    padding: 2rem

 & > *:not(:first-child)
  margin-top: 1rem
 .row
  display: flex
  width: inherit
  flex-direction: row
  justify-content: space-between
  align-items: center
  
  

  .name
    max-width: 28rem
    font-size: 36px
    font-weight: 600
    text-overflow: ellipsis
    &::after
      content: ''
      display: block
      height: 4px
      border-radius: 10px
      background: #D62828
      width: 100%
  .time
    display: flex
    font-size: 24px
    color: #8D8A8A

  .description
    font-size: 22px
  .version
    font-size: 28px
    color: #8D8A8A

  .service
    margin-right: 2rem
    width: auto
    height: 3rem
    flex-shrink: 0


.info
  font-size: 26px
  display: flex
  flex-direction: row
  justify-content: space-between
  width: 55%
  .status
    font-weight: 600
    &::after
      content: ''
      display: block
      height: 4px
      border-radius: 10px
      background: #D62828
      width: 100%
  .f-column
    display: flex
    flex-direction: column
    div:not(:first-child)
      margin-top: 1rem
  .s-column
    display: flex
    flex-direction: column
    margin-left: 2rem
    div:not(:first-child)
      margin-top: 1rem
  div
    display: flex
  p:not(.status)
    margin-left: 1.5rem
    color: #8D8A8A
</style>
