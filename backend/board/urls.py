from django.urls import path

from . import views

app_name = 'board'

urlpatterns = [
    # ex: /board/
    path('', views.index, name='index'),
    # ex: /board/5/
    path('<int:post_id>/', views.detail, name='detail'),
    # Vue API
    path('api/posts/<int:post_id>/', views.post_api_detail, name='post_api_detail'),
    path('api/posts/', views.post_api_index, name='post_api_index'),
    # ex: /board/create/
    path('create/', views.create, name='create'),
    # ex: /board/update/5/
    path('update/<int:post_id>/', views.update, name='update'),
    # ex: /board/delete/5/
    path('delete/<int:post_id>/', views.delete, name='delete'),
    # ex: /board/about/
    path('about/', views.about, name='about'),
]
