<script>
import { defineComponent } from "vue";
import { useQuasar } from "quasar";

import axios from "axios";

export default defineComponent({
  name: "startScan",
  setup() {
    const $q = useQuasar();

    return {
      showNotify(text) {
        $q.notify({
          message: text,
          type: "negative",
        });
      },
    };
  },
  data() {
    return {
      ip: "",
      port: "",
      name: "",
      description: "",
    };
  },
  methods: {
    onSubmitStart() {
      let isAllow = true;
      const ipv4Pattern =
        /^((25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$/;
      const portPattern = /^[0-9]{1,5}$/;
      const textPattern = /^[\u0400-\u04FF.(),:;A-Za-z0-9 ]+$/;
      if (ipv4Pattern.test(this.ip) !== true) {
        this.showNotify("Введите корректный IP адрес");
        isAllow = false;
      }

      if (portPattern.test(this.port) !== true) {
        this.showNotify("Введите корректный порт");
        isAllow = false;
      }

      if (textPattern.test(this.name) !== true) {
        this.showNotify(
          "Название может содержать только цифры, латинские, кириллические буквы, а так же знаки .(),:;"
        );
        isAllow = false;
      }
      if (textPattern.test(this.description) !== true) {
        this.showNotify(
          "Описание может содержать только цифры, латинские, кириллические буквы, а так же знаки .(),:;"
        );
        isAllow = false;
      }

      if (isAllow) {
        axios({
          method: "post",
          url: process.env.API + "/scan/start/",
          data: {
            name: this.name,
            description: this.description,
            ip: this.ip,
            port: this.port,
          },
          responseType: "json",
          headers: {
            ContextType: "application/jsom",
            Authorization: `Bearer ${localStorage.getItem("access_token")}`,
          },
        })
          .then((res) => {
            console.log(res.data);
            this.$router.push(`/report/${res.data.scan_id}`);
          })
          .catch((err) => this.showNotify("Не удается начать сканирование"));
      }
    },
  },
  props: {},
  computed: {},
});
</script>

<template>
  <q-list class="auth-list">
    <div class="header-text text-align-center">
      Сканировать
      <img src="../assets/strip.svg" style="width: 100%; align-self: center" />
    </div>
    <div>
      <input class="input default-text" placeholder="IP" v-model="ip" />
    </div>
    <div>
      <input class="input default-text" placeholder="Порт" v-model="port" />
    </div>
    <div>
      <input class="input default-text" placeholder="Название" v-model="name" />
    </div>
    <div>
      <input
        class="input default-text"
        placeholder="Описание"
        v-model="description"
      />
    </div>

    <div class="row">
      <button class="default-text sub-button" @click="onSubmitStart">
        Сканировать
      </button>
    </div>
  </q-list>
</template>

<style scoped lang="sass">

.row
  max-width: 100%

.auth-list
  display: flex
  flex-direction: column
  max-width: 100%  // Set maximum width to 100% of the parent container
  height: auto     // Set height to auto to allow it to adjust based on content
  background: white
  border-radius: 24px
  justify-content: center
  align-content: center
  flex-wrap: wrap
  padding: 2rem 3rem 2rem    // Add padding for better spacing
  

.input
  width: 100%       // Set width to 100% to adjust based on the parent container
  height: 85px
  border: none
  border-radius: 24px
  padding-left: 36px
  outline: none
  background-color: #F1F2F5
  color: #434343
  margin-top: 1rem

  &:focus, &:hover
    background-color: #E7E8E8

.sub-button
  width: 100%       // Set width to 100% to adjust based on the parent container
  height: 100%
  border: none
  border-radius: 24px
  background-color: #D62828
  color: white
  padding: 2rem 0rem 2rem
  margin: 1rem

  &:hover
    background-color: #C21414

.text-align-center
  display: flex
  flex-direction: column
  text-align: center
  margin-bottom: 41px


@media screen and (max-width: 600px)
  .auth-list
    padding: 2rem
    margin: 0 1rem 0

  .input, .sub-button
    width: 100%

  .col-6:not(:last-child)
    flex: 1
    .sub-button

      width: 100%
  .col-6:not(:first-child)
    flex: 2
    .sub-button
        width: 150%
</style>
