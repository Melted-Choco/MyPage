<template>
  <div id="app">
    <!-- <PostDetail :postId="3" /> -->
    <header>
      <!-- <router-link to="/"> -->
      <a href="/">
        <h1>My Board</h1>
      </a>
      <!-- </router-link> -->
    </header>

    <div class="container">
      <aside>
        <h2>Menu</h2>
        <ul id="menu-list">
          <li @click="toggleMenu('category')" id="menu-category">
            <span :class="{ rotated: openMenu === 'category'}">▶</span>
            Board
          </li>
          <!-- 여기부터 진행 -->
          <ul :class="{ open: openMenu === 'category'}">
            <li><router-link to="/category/1">Category 1</router-link></li>
            <li><router-link to="/category/2">Category 2</router-link></li>
          </ul>

          <li @click="toggleMenu('about')">
            <span :class="{ rotated: openMenu === 'about' }">▶</span>
            About
          </li>
          <ul :class="{ open: openMenu === 'about' }">
            <li><router-link to="/about">소개</router-link></li>
          </ul>
        </ul>
      </aside>

      <main>
        <router-view />
      </main>
    </div>

    <footer>
      &copy; 2025 My Board. All rights reserved.
    </footer>
  </div>
</template>

<script>
import PostDetail from './components/PostDetail.vue'

export default {
  data() {
    return {
      openMenu: null,
    };
  },
  methods: {
    toggleMenu(menuName) {
      this.openMenu = this.openMenu === menuName ? null : menuName;
    },
  },
};
</script>

<style>
/* 기본 스타일 */
</style>
