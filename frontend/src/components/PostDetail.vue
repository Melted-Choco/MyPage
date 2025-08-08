<template>
    <div>
        <div v-if="loading">불러오는 중...</div>
        <div v-else-if="error">{{ error }}</div>
        <div v-else>
            <h1>{{ post.title }}</h1>
            <p style="color: #888;">작성일: {{ new Date(post.post_date).toLocaleDateString() }}</p>
            <div v-html="post.content" style="padding: 12px; border: 1px solid #ccc;"></div>
        </div>
    </div>
</template>

<script>
export default {
    props: ['id'],
    data() {
        return {
            post: {},
        };
    },
    mounted() {
        fetch(`http://localhost:8000/board/api/posts/${this.id}`)
            .then(res => res.json())
            .then(data => {
                console.log(data);
                this.post = data;
            });
    },
};
</script>

<style scoped>
.post-content {
    padding: 12px;
    border: 1px solid #ccc;
}
</style>