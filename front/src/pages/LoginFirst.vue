<script>
import { defineComponent } from "vue";

export default defineComponent({
  name: "LoginFirstPage",
  methods: {
        redirectToAuth() {
            this.$router.push('/auth');
         },
      },
});
</script>

<template>
    <q-page-container class="background">
        <div class="box header-text">
            <p>Войдите, чтобы пользоваться сервисом</p>
            <button class="default-text sub-button" @click="redirectToAuth(); console.log(1)">
                Войти
            </button>
        </div>
    </q-page-container>

</template>

<style scoped lang="sass">

.sub-button
  width: 200px
  padding: 1rem
  border: none
  border-radius: 24px
  background-color: #D62828
  color: white

  &:hover
    background-color: #C21414

.box
  display: flex
  width: 828px
  padding: 2rem
  max-height: 622px
  background: white
  box-shadow: rgba(0, 0, 0, .05) 0 27px 104.6px
  border-radius: 24px
  justify-content: center
  align-items: center
  flex-direction: row
  flex-wrap: wrap
  body.screen--xs &
    margin-left: 1rem
    margin-right: 1rem
    font-size: 26px
  body.screen--sm &
    margin-left: 1rem
    margin-right: 1rem
    flex-direction: column
    font-size: 30px
</style>