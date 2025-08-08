<template>
  <div>
    <ul class="post-list">
      <li v-for="post in posts" :key="post.id">
        <div class="post-number">{{ post.id }}</div>
        <router-link :to="{ name: 'PostDetail', params: { id: post.id } }">
          {{ post.title }}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>

export default {
  props: ['category'],
  data() {
    return {
      posts: [],
    };
  },
  mounted() {
    this.fetchPosts();
  },
  watch: {
    category() { // :category 변경될 때마다 fetchPosts 재실행
      this.fetchPosts();
    },
  },
  methods: {
    fetchPosts() {
      fetch(`http://localhost:8000/board/api/posts/?category=${this.category}`)
        .then(res => res.json())
        .then(data => {
          this.posts = data.posts;
        });
    },
  },
};
</script>
