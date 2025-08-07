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
            <li @click="fetchPosts('2d')" class="list-items">2D</li>
            <li @click="fetchPosts('3d')" class="list-items">3D</li>
          </ul>

          <li @click="toggleMenu('ai')" id="menu-ai">
            <span :class="['arrow', { rotated: selectMenu === 'ai'}]">▶</span>
            AI
          </li>
          <ul :class="{ open: selectMenu === 'ai'}" id="list-ai">
            <li @click="fetchPosts('android-permission')" class="list-items">Android Permission</li>
            <li @click="fetchPosts('chatbot')" class="list-items">Chatbot</li>
            <li @click="fetchPosts('classification')" class="list-items">Classification</li>
          </ul>

          <li @click="toggleMenu('full')" id="menu-full">
            <span :class="['arrow', { rotated: selectMenu === 'full'}]">▶</span>
            Full Stack
          </li>
          <ul :class="{ open: selectMenu === 'full'}" id="list-full">
            <li @click="fetchPosts('flea-market')" class="list-items">Flea Market</li>
            <li @click="fetchPosts('green-code')" class="list-items">Green Code</li>
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
        <PostList :posts="posts" />
      </main>
    </div>

    <footer>
      &copy; 2025 My Board. All rights reserved.
    </footer>
  </div>
</template>

<script>
import PostList from './components/PostList.vue';

export default {
  components: { PostList },
  data() {
    return {
      selectMenu: null,
      posts: [],
    };
  },
  methods: {
    toggleMenu(menuName) {
      this.selectMenu = this.selectMenu === menuName ? null : menuName;
    },
    fetchPosts(category) {
      fetch(`http://localhost:8000/board/api/posts/?category=${category}`)
        .then(response => response.json())
        .then(data => {
          this.posts = data.posts;
        });
    },
  },
};
</script>

<style>
/* 기본 스타일 */
</style>
