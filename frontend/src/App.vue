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
            <span :class="['arrow', { rotated: selectMenu === 'category'}]">▶</span>
            Board
          </li>
          
          <li @click="toggleMenu('unity')" id="menu-unity">
            <span :class="['arrow', { rotated: selectMenu === 'unity'}]">▶</span>
            Unity
          </li>
          <ul :class="{ open: selectMenu === 'unity'}" id="list-unity">
            <li class="list-items">
              <router-link :to="{ name: 'PostList', params: { category: '2d' }}">
                2D
              </router-link>
            </li>
            <li class="list-items">
              <router-link :to="{ name: 'PostList', params: { category: '3d' }}">
                3D
              </router-link>
            </li>
          </ul>

          <li @click="toggleMenu('ai')" id="menu-ai">
            <span :class="['arrow', { rotated: selectMenu === 'ai'}]">▶</span>
            AI
          </li>
          <ul :class="{ open: selectMenu === 'ai'}" id="list-ai">
            <li class="list-items">
              <router-link :to="{ name: 'PostList', params: { category: 'android-permission' }}">
                Android Permission
              </router-link>
            </li>
            <li class="list-items">
              <router-link :to="{ name: 'PostList', params: { category: 'chatbot' }}">
                Chatbot
              </router-link>
            </li>
            <li class="list-items">
              <router-link :to="{ name: 'PostList', params: { category: 'classification' }}">
                Classification
              </router-link>
            </li>
          </ul>

          <li @click="toggleMenu('full')" id="menu-full">
            <span :class="['arrow', { rotated: selectMenu === 'full'}]">▶</span>
            Full Stack
          </li>
          <ul :class="{ open: selectMenu === 'full'}" id="list-full">
            <li class="list-items">
              <router-link :to="{ name: 'PostList', params: { category: 'flea-market' }}">
                Flea Market
              </router-link>
            </li>
            <li class="list-items">
              <router-link :to="{ name: 'PostList', params: { category: 'green-code' }}">
                Green Code
              </router-link>
            </li>
          </ul>

          <li @click="toggleMenu('about')" id="menu-about">
            <span :class="['arrow', { rotated: selectMenu === 'about' }]">▶</span>
            About
          </li>
          <ul :class="{ open: selectMenu === 'about' }" id="list-about">
            <li class="list-items"><router-link to="/about">소개</router-link></li>
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
export default {
  data() {
    return {
      selectMenu: null,
    };
  },
  methods: {
    toggleMenu(menuName) {
      this.selectMenu = this.selectMenu === menuName ? null : menuName;
    },
  },
};
</script>

<style>
/* 기본 스타일 */
</style>
