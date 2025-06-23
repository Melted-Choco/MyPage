from django.shortcuts import render, get_object_or_404

from .models import Post

def index(request):
    latest_post_list = Post.objects.order_by('-post_date')[:10] # only Top 10
    context = {
        'latest_post_list': latest_post_list,
    }
    return render(request, 'board/index.html', context)

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'board/detail.html', {'post': post})
