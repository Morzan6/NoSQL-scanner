<template>
  <q-layout view="">
    <q-toolbar class="flex toolbar justify-around">
      <div class="flex flex-row-gap">
        <menu-button :href="'scans'" :text="'Мои сканы'" />
        <menu-button :href="'dashboard'" :text="'Панель'" />
      </div>
      <div v-if="!checkIfLogin()">
        <menu-button :href="'auth'" :text="text" @click="this.$router.go('/auth'); this.text = 'Вход'"/>
      </div>
      <div v-else> <menu-button @click="logout()" :href="'auth'" :text="text" /></div>
    </q-toolbar>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent } from "vue";
import MenuButton from "components/menu-button-component.vue";

export default defineComponent({
  name: "MainLayout",
  components: { MenuButton },
  component: ["MenuButton"],
  data(){
    return {
      text: 'Выход'
    }
  },
  methods: {
    logout() {
      localStorage.removeItem("access_token");
      this.text="Вход";
      buttonName();
    },
    buttonName() {
      if (!localStorage.getItem("access_token")) {
        this.text = 'Вход';
      } else {
        this.text =  'Выход';
      }
    },
    checkIfLogin() {
      if (localStorage.access_token) {
        return true;
      } else {
        return false;
      }
    },
  },
  
});
</script>

<style lang="sass" scoped>
.toolbar
  position: absolute
  right: 0
  width: 36%
  min-height: 8vh
  left: auto
  background-color: white
  border-radius: 0 0 0 24px
  box-shadow: rgba(0, 0, 0, 0.05) 0 27px 104.6px
  padding: 1rem
  @media (min-width: 768px) 
  /* Стили для устройств с шириной viewport, находящейся в диапазоне 768px - 991px */
  width: 100%

  /* Устройства со средним экраном (ноутбуки и компьютеры, 992px и выше) */
  @media (min-width: 992px)
    width: 100%
    /* Стили для устройств с шириной viewport, находящейся в диапазоне 992px - 1199px */


  /* Устройства с большим экраном (компьютеры, 1200px и выше) */
  @media (min-width: 1600px)
    width: 36%
    /* Стили для устройств с шириной viewport >1200px */

 

.flex-row-gap
  gap: 58px
</style>
