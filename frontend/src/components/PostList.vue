<template>
  <div>
    <ul>
      <li v-for="post in posts" :key="post.id">
        <h3>{{ post.title }}</h3>
        <p>Category: {{ post.category }}, Date: {{ post.post_date }}</p>
        <br>
        <p>{{ post.content }}</p>
      </li>
    </ul>
  </div>
</template>

<script>

export default {
  props: {
    posts: {
        type: Array,
        required: true,
        default: () => [],
    },
  },
};
</script>
