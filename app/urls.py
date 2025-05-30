from django.urls import path
from .views import author_list, author_create, author_update, author_delete

urlpatterns = [
    path('authors/', author_list, name='author_list'),
    path('authors/new/', author_create, name='author_create'),
    path('authors/<int:pk>/edit/', author_update, name='author_update'),
    path('authors/<int:pk>/delete/', author_delete, name='author_delete'),
]
