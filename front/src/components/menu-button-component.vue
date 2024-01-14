<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "MenuButton",
  props: {
    href: {
      type: String,
      default: "",
    },
    text: {
      type: String,
      default: "New menu btn",
    },
  },
  computed: {
    onPage() {
      return window.location.pathname === this.$router.resolve(this.href).path
        ? "on-cur-page"
        : "on-dif-page";
    },
  },
});
</script>

<template>
  <a
    class="default-text"
    :class="onPage"
    v-on:click="$router.replace(this.href)"
    >{{ text }}</a
  >
</template>

<style lang="sass" scoped>
$onPage: v-bind(onPage)

.on-dif-page
    &:hover
      color: #2D2D2D
      transition-duration: 200ms

    &::after
      content: ''
      display: block
      height: 1px
      background: #2D2D2D
      width: 0

    &:hover::after
      width: 100%
      transition-duration: 0.2s

.on-cur-page
  color: #2D2D2D

  &::after
    content: ''
    display: block
    height: 1px
    background: #2D2D2D
    width: 100%
</style>
