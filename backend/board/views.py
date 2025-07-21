from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils import timezone
from datetime import datetime

from .models import Post

CATEGORY_TAGS = {
    '2d': ['프로젝트', '개발일지', '시연'],
    '3d': ['프로젝트', '개발일지', '시연'],
    'android-permission': ['Test1', 'Test2', 'Test3'],
    'chatbot': ['Test1', 'Test2', 'Test3'],
    'classification': ['Test1', 'Test2', 'Test3'],
    'flea-market': ['Test1', 'Test2', 'Test3'],
    'green-code': ['Test1', 'Test2', 'Test3'],
}

def index(request):
    category = request.GET.get('category')
    tag = request.GET.get('tag')
    
    parentCategory = get_parent_category(category)
    tag_list = CATEGORY_TAGS.get(category, [])
    
    latest_post_list = Post.objects.all().order_by('-post_date')
    if category:
        latest_post_list = latest_post_list.filter(category=category).order_by('-post_date')
    if tag:
        latest_post_list = latest_post_list.filter(tag=tag).order_by('-post_date')
        
    paginator = Paginator(latest_post_list, 10) # 10 posts per one page
    
    page_number = request.GET.get('page') # current page
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'selected_category': category,
        'parent_category': parentCategory,
        'tag_list': tag_list,
    }
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest': # AJAX 요청인 경우
        return render(request, 'board/post_list_partial.html', context)
    else:
        return render(request, 'board/index.html', context)
    
def get_parent_category(category):
    mapping = {
        "2d": "Unity",
        "3d": "Unity",
        "android-permission": "AI",
        "chatbot": "AI",
        "classification": "AI",
        "flea-market": "Full Stack",
        "green-code": "Full Stack",
    }
    return mapping.get(category, "Unknown")

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'board/detail_vue.html', {'post': post})

# Vue
def post_api_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    return JsonResponse({
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'post_date': post.post_date.isoformat()
    })

@csrf_exempt
def create(request):
    if request.method == 'GET':
        return render(request, "board/create.html")
    elif request.method == 'POST':
        # request.POST[] : key가 없으면 예외(MultiValueDictKeyError) 발생
        category = request.POST['category']
        tag = request.POST['tag']
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
            tag=tag,
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
    
@csrf_exempt
def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    if request.method == 'POST':
        post.delete()
        return redirect('/board/')
    else:
        return render(request, 'board/detail.html', {
            'post': post,
            'error_message': '삭제는 POST 요청으로만 가능합니다'
        })
        
def about(request):
    return render(request, 'board/about.html')