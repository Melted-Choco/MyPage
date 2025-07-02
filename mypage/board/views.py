from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.utils import timezone
from datetime import datetime

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
        # request.POST[] : key가 없으면 예외(MultiValueDictKeyError) 발생
        category = request.POST['category']
        title = request.POST['title']
        content = request.POST['content']
        
        # request.POST.get() : key가 없으면 None 반환
        is_checked = request.POST.get('rand_date')
        selected_date = request.POST.get('selected_date')
        
        print(is_checked)
        if is_checked and selected_date:
            try:
                post_date = datetime.strptime(selected_date, '%Y-%m-%d')
                print(post_date)
            except ValueError:
                post_date = timezone.now()
        else:
            post_date = timezone.now()
        
        newPost = Post(
            category=category,
            title=title,
            content=content,
            post_date=post_date
        )
        newPost.save()
        url = '/board/' + str(newPost.id)
        return redirect(url)
    
@csrf_exempt
def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'GET':
        return render(request, "board/update.html", {'post': post})
    elif request.method == 'POST':
        category = request.POST['category']
        title = request.POST['title']
        content = request.POST['content']
        
        is_checked = request.POST.get('rand_date')
        selected_date = request.POST.get('selected_date')
        
        if is_checked and selected_date:
            try:
                post_date = datetime.strptime(selected_date, '%Y-%m-%d')
            except ValueError:
                post_date = timezone.now()
        else:
            post_date = post.post_date
        
        post.category = category
        post.title = title
        post.content = content
        post.post_date = post_date
        post.save()
        return render(request, 'board/detail.html', {'post': post})
    