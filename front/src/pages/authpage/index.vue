<script>
import { defineComponent } from "vue";
import requestSender from "components/request-sender";
import { useQuasar } from "quasar";
import { useCounterStore } from "stores/auth";

export default defineComponent({
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
      name: "",
      password: "",
    };
  },
  methods: {
    verify() {
      let isOk = true;
      const usernamePattern = /^[A-Za-z0-9_@!]{4,25}$/;
      if (usernamePattern.test(this.name) !== true) {
        console.log("asdsad");
        isOk = false;
        this.showNotify(
          "Имя пользователя должно быть длиной от 4 до 25 символов и может состоять только цифр, латинских букв и символов _@!"
        );
      }
      if (this.password.length < 8) {
        isOk = false;
        this.showNotify("Длина пароля должна быть больше 8 символов");
      }

      return isOk;
    },
    onSubmitLogin() {
      const store = useCounterStore();
      const resp = requestSender("post", process.env.API + "/auth/login/", {
        username: this.name,
        password: this.password,
      });
      resp
        .then((res) => {
          localStorage.access_token = res.data.access_token;
          store.isLogin = true;
          this.$router.go("/auth");
        })
        .catch((err) => this.showNotify(err.response.data.detail));
    },
    onSubmitReg() {
      if (this.verify() === true) {
        const resp = requestSender("post", process.env.API + "/auth/create/", {
          username: this.name,
          password: this.password,
        });
        resp
          .then((res) => this.onSubmitLogin())
          .catch((err) => this.showNotify(err.response.data.detail));
      }
    },
  },
});
</script>

<template>
  <q-page-container class="background-auth">
    <q-list class="auth-list">
      <q-item class="header-text text-align-center">
        Войти или Зарегистрироваться
        <img
          src="../../assets/strip.svg"
          style="width: 100%; align-self: center"
        />
      </q-item>
      <q-item>
        <input class="input default-text" placeholder="Имя" v-model="name" />
      </q-item>
      <q-item>
        <input
          class="input default-text"
          type="password"
          name="password"
          v-model="password"
          placeholder="Пароль"
        />
      </q-item>
      <div class="row">
        <q-item class="col-6">
          <button class="default-text sub-button" @click="onSubmitLogin">
            Войти
          </button>
        </q-item>
        <q-item class="col-6">
          <button class="default-text sub-button" @click="onSubmitReg">
            Зарегистрироваться
          </button>
        </q-item>
      </div>
    </q-list>
  </q-page-container>
</template>

<style lang="sass" scoped>
.row
  max-width: 100%

.auth-list
  display: flex
  flex-direction: column
  max-width: 100%  // Set maximum width to 100% of the parent container
  height: auto     // Set height to auto to allow it to adjust based on content
  background: white
  box-shadow: rgba(0, 0, 0, .05) 0 27px 104.6px
  border-radius: 24px
  justify-content: center
  align-content: center
  flex-wrap: wrap
  padding: 2rem 3rem 2rem    // Add padding for better spacing

.input
  width: 100%       // Set width to 100% to adjust based on the parent container
  height: 101px
  border: none
  border-radius: 24px
  padding-left: 36px
  outline: none
  background-color: #F1F2F5
  color: #434343

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

  &:hover
    background-color: #C21414

.text-align-center
  display: flex
  flex-direction: column
  text-align: center
  margin-bottom: 41px

// Media query for smaller screens
@media screen and (max-width: 600px)
  .auth-list
    padding: 2rem
    margin: 0 1rem 0

  .input, .sub-button
    width: 100%   // Adjust width to 100% for smaller screens

  .col-6:not(:last-child)
    flex: 1
    .sub-button

      width: 100%
  .col-6:not(:first-child)
    flex: 2
    .sub-button
        width: 150%
</style>
