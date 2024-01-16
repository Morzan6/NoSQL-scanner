<template>
  <q-layout view="lHh Lpr lFf">
    <q-toolbar class="flex toolbar justify-around">
      <div class="flex flex-row-gap">
        <menu-button :href="'scans'" :text="'Мои сканы'" />
        <menu-button :href="'dashboard'" :text="'Доска'" />
      </div>
      <div v-if="!checkIfLogin">
        <menu-button :href="'auth'" :text="buttonName()" />
      </div>
      <div v-else> <menu-button @click="logout()" :href="'/auth'" :text="'User'" /></div>
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
  methods: {
    logout() {
      localStorage.removeItem("access_token");
      this.text="Вход";
    },
    buttonName() {
      if (!localStorage.getItem("access_token")) {
        return 'Вход';
      } else {
        return 'User';
      }
    }
  },
  computed: {
    checkIfLogin() {
      if (localStorage.access_token) {
        return true;
      } else {
        return false;
      }
    },
  }
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
  body.screen--sm &
    width: 60%
  body.screen--xs &
    width: inherit

.flex-row-gap
  gap: 58px
</style>
