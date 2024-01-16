<template>
  <q-layout view="lHh Lpr lFf">
    <q-toolbar class="flex toolbar justify-around">
      <div class="flex flex-row-gap">
        <menu-button :href="'scans'" :text="'Мои сканы'" />
        <menu-button :href="'dashboard'" :text="'Доска'" />
      </div>
      <div v-if="!checkIfLogin">
        <menu-button :href="'auth'" :text="'Вход'" />
      </div>
      <div v-else> <menu-button :href="'logout'" :text="'User'" /></div>
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
  computed: {
    checkIfLogin() {
      if (localStorage.access_token) {
        return true;
      } else {
        return false;
      }
    }
  }
});
</script>

<style lang="sass" scoped>
.toolbar
  position: absolute
  right: 0
  width: 36%
  min-height: 10vh
  left: auto
  background-color: white
  border-radius: 0 0 0 24px
  box-shadow: rgba(0, 0, 0, 0.05) 0 27px 104.6px

.flex-row-gap
  gap: 58px
</style>
