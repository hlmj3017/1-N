from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/detail', views.detail, name='detail'),

    path('create/', views.create, name='create'),

    path('<int:article_id>/comment_create/', views.comment_create, name='comment_create'),
]