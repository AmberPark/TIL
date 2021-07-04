<template>
  <div id="app">
    <div>
      <b-navbar toggleable="lg" type="dark" variant="dark">
        <b-navbar-nav>
          <b-nav-item href="#">Home</b-nav-item>
          <b-nav-item href="#">Introduce</b-nav-item>
          <b-nav-item href="#">Page</b-nav-item>
        </b-navbar-nav>  
      </b-navbar>
    </div>
    <Home />
  </div>
</template>

<script>
import Home from './components/Home.vue'
export default {
  name : 'App',
  components: {
    Home,
  }
}
</script>

<style>

</style>