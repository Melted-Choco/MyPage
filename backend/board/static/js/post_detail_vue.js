// Vue 앱
function loadPostApp(postId) {
    const { createApp } = Vue;

    createApp({
        data() {
            return {
                post: null,
                loading: true,
                error: null
            };
        },
        created() {
            fetch(`/board/api/posts/${postId}/`) // post_api_detail 호출
                .then(res => res.json())
                .then(data => {
                    this.post = data;
                    this.loading = false;
                })
                .catch(err => {
                    this.error = '불러오는데 실패했습니다.';
                    this.loading = false;
                });
        },
        template: `
            <div>
                <div v-if="loading">불러오는 중...</div>
                <div v-else-if="error">{{ error }}</div>
                <div v-else>
                    <h1>{{ post.title }}</h1>
                    <p style="color: #888;">작성일: {{ new Date(post.post_date).toLocaleDateString() }}</p>
                    <div v-html="post.content" style="padding: 12px; border: 1px solid #ccc;"></div>
                </div>
            </div>
        `
    }).mount("#post-app");
}