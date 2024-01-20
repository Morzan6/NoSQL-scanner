<script>
import { defineComponent } from "vue";
import smallScan from "../../components/smallScan.vue";
import requestSender from "components/request-sender";
import formatTimeDelta from "../timedelta.js";

export default defineComponent({
  mounted() {
    this.setChunkSize();
  },
  created() {
    window.addEventListener("resize", this.setChunkSize);
  },
  name: "ScansPage",
  components: { smallScan },
  component: ["smallScan"],
  methods: {
    setChunkSize() {
      if (window.innerWidth < 600) {
        this.chunkSize = 4;
      } else if (window.innerWidth < 900) {
        this.chunkSize = 5;
      } else if (window.innerWidth < 1750) {
        this.chunkSize = 6;
      } else if (window.innerWidth < 2200) {
        this.chunkSize = 7;
      } else if (window.innerWidth < 2500) {
        this.chunkSize = 8;
      } else if (window.innerWidth < 2700) {
        this.chunkSize = 9;
      }
    },
    timeDelta(time) {
      return formatTimeDelta(time);
    },
    prevSlide() {
      if (this.currentPage > 0) {
        this.currentPage--;
      }
    },
    nextSlide() {
      if (this.currentPage < this.chunkedScans().length - 1) {
        this.currentPage++;
      }
    },
    chunkedScans() {
      const scansCopy = [...this.scans];
      const result = [];

      while (scansCopy.length > 0) {
        result.push(scansCopy.splice(0, this.chunkSize));
      }

      return result;
    },
  },
  data() {
    return {
      scans: [],
      currentPage: 0,
      chunkSize: 7,
      isLoading: true,
    };
  },

  beforeMount() {
    const resp = requestSender(
      "get",
      process.env.API + "/scan/my/", 
      {},
      localStorage.getItem("access_token")
    );
    resp
      .then((res) => {
        this.scans = res.data.reverse();
        this.isLoading = false;
      })
      .catch((err) => this.showNotify(err.response.data.detail));
  },
});
</script>

<template>
  <q-page-container class="background">
    <div class="columns">
      <div class="scans-column">
        <img class="loading" src="/loading3.svg" v-if="isLoading" />
        <smallScan
          v-for="s in chunkedScans()[this.currentPage]"
          :key="s.id"
          :id="s.id"
          :name="s.name"
          :ip="s.ip"
          :service="s.type"
          :timedelta="timeDelta(s.datetime)"
        />
        <div v-if="this.scans.length === 0 && !isLoading" class="emptyScan">
          У вас еще нет сканов
        </div>
        <div v-if="chunkedScans().length > 1" class="buttons">
          <button
            class="button"
            style="margin-right: 5rem"
            @click="prevSlide"
            :disabled="this.currentPage === 0"
          >
            Назад
          </button>
          <button
            style="margin-left: 5rem"
            @click="nextSlide"
            class="button"
            :disabled="this.currentPage === chunkedScans().length - 1"
          >
            Вперед
          </button>
        </div>
      </div>

      <div class="start-scan-column">{{ this.currentPage }}</div>
    </div>
  </q-page-container>
</template>

<style scoped lang="sass">

.emptyScan
    width: inherit
    color: #2D2D2D
    background: #FFF
    padding: 1.2rem 1rem 1.2rem
    font-size: 26px

    align-items: center
    justify-content: center

    border-radius: 0.6875rem
    display: flex

    box-shadow: 0px 27px 104.6px 0px rgba(0, 0, 0, 0.05)
    margin-bottom: 1rem


.buttons
  display: flex
  justify-content: center
  margin-bottom: 2rem

.button
  border: none
  position: fixed
  bottom: 36px
  background-color: #D62828
  color: white
  border-radius: 5px
  padding: 4px 9px 4px
  font-weight: 600
  &:hover
    background-color: #C21414
</style>
