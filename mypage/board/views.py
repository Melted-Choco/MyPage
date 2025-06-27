from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

from .models import Post

def index(request):
    latest_post_list = Post.objects.order_by('-post_date')
    paginator = Paginator(latest_post_list, 10) # 10 posts per one page
    
    page_number = request.GET.get('page') # current page
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'board/index.html', {'page_obj': page_obj})

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
    
@csrf_exempt
def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'GET':
        return render(request, "board/update.html", {'post': post})
    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        post.title = title
        post.content = content
        post.save()
        return render(request, 'board/detail.html', {'post': post})
    