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
    props: {
        postId: Number
    },
    data() {
        return {
            post: null,
            loading: true,
            error: null
        };
    },
    computed: {
        formattedDate() {
            return new Date(this.post.post_date).toLocaleDateString();
        }
    },
    mounted() {
        fetch('http://127.0.0.1:8000/board/api/posts/3/') // 절대경로
            .then(res => res.json())
            /*.then(text => {
                console.log('원본 응답:', text);
            })*/
            .then(data => {
                this.post = data;
                this.loading = false;
            })
            .catch(() => {
                this.error = '불러오는데 실패했습니다.';
                this.loading = false;
            });
    }
};
</script>

<style scoped>
.post-content {
    padding: 12px;
    border: 1px solid #ccc;
}
</style>