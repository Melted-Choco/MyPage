from django.urls import path

from . import views

app_name = 'board'

urlpatterns = [
    # ex: /board/
    path('', views.index, name='index'),
    # ex: /board/5/
    path('<int:post_id>/', views.detail, name='detail'),
    # ex: /board/create/
    path('create/', views.create, name='create'),
]
