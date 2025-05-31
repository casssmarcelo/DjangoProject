from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('new/', views.item_create, name='item_create'),
    path('edit/<int:pk>/', views.item_update, name='item_update'),
    path('delete/<int:pk>/', views.item_delete, name='item_delete'),
    path('items/', views.item_list, name='item_list_alt'),

    path('categories/', views.category_list, name='category_list'),
    path('categories/new/', views.category_create, name='category_create'),
    path('categories/edit/<int:pk>/', views.category_update, name='category_update'),
    path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),

    path('publisher/', views.publisher_list, name='publisher_list'),
    path('publisher/new/', views.publisher_create, name='publisher_create'),
    path('publisher/edit/<int:pk>/', views.publisher_update, name='publisher_update'),
    path('publisher/delete/<int:pk>/', views.publisher_delete, name='publisher_delete'),

]
