<script>
import { defineComponent } from "vue";
import requestSender from "components/reqeust-sender";
import {useQuasar} from "quasar";


export default defineComponent({
  name: 'AuthPage',
  setup() {
    const $q = useQuasar();

    return {
      showNotify (text) {
        $q.notify({
          message: text,
          type: 'negative'
        })
      }
    }
  },
  data() {
    return {
      name: '',
      password: ''
    };
  },
  methods: {
    onSubmitLogin() {
      const resp = requestSender('post', 'http://127.0.0.1:8000/api/auth/login/', {
        "username": this.name,
        "password": this.password
      })
      resp.then((res) => (localStorage.access_token = res.data.access_token)).catch((err) => (this.showNotify(err.response.data.detail)));
      this.$router.push('scan');
    },
    onSubmitReg() {
      const resp = requestSender('post', 'http://127.0.0.1:8000/api/auth/create/', {
        "username": this.name,
        "password": this.password
      })
      resp.then((res) => (this.onSubmitLogin())).catch((err) => (this.showNotify(err.response.data.detail)));
    },
  },
})
</script>

<template>
  <q-page-container class="background">
    <q-list class="auth-list">
      <q-item class="header-text text-align-center">
        Войти или Зарегистрироваться
        <img src="../../assets/strip.svg" style="width:569px; align-self: center;"/>
      </q-item>
      <q-item>
        <input class="input default-text" placeholder="Имя" v-model="name"/>
      </q-item>
      <q-item>
        <input class="input default-text" type="password" name="password" v-model="password" placeholder="Пароль"/>
      </q-item>
      <div class="row">
        <q-item class="col-6">
          <button class="default-text sub-button" @click="onSubmitLogin">Войти</button>
        </q-item>
        <q-item class="col-6">
          <button class="default-text sub-button" @click="onSubmitReg">Зарегистрироваться</button>
        </q-item>
      </div>
    </q-list>
  </q-page-container>
</template>

<style lang="sass" scoped>
.background
  background-image: url("../../assets/auth-background.svg")
  background-repeat: no-repeat
  height: 100dvh
  width: 100dvw
  background-size: cover
  display: flex
  flex-wrap: wrap
  justify-content: center
  align-content: center

.auth-list
  display: flex
  flex-direction: column
  width: 828px
  height: 622px
  background: white
  box-shadow: rgba(0, 0, 0, .05) 0 27px 104.6px
  border-radius: 24px
  justify-content: center
  align-content: center
  flex-wrap: wrap

.input
  width: 738px
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
  width: 359px
  height: 101px
  border: none
  border-radius: 24px
  background-color: #D62828
  color: white

  &:hover
    background-color: #C21414

.text-align-center
  display: flex
  flex-direction: column
  text-align: center
  margin-bottom: 41px
</style>
