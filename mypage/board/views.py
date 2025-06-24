from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
def create(request):
    if request.method == 'GET':
        return render(request, "board/create.html")
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        newPost = Post(title=title, content=content)
        newPost.save()
        url = '/board/' + str(newPost.id)
        return redirect(url)