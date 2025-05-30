from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('new/', views.item_create, name='item_create'),
    path('edit/<int:pk>/', views.item_update, name='item_update'),
    path('delete/<int:pk>/', views.item_delete, name='item_delete'),
    path('', views.autor_list, name='autor_list'),
    path('new/', views.autor_create, name='autor_create'),
    path('edit/<int:pk>/', views.autor_update, name='autor_update'),
    path('delete/<int:pk>/', views.autor_delete, name='autor_delete'),
    path('publishers/', views.publisher_list, name='publisher_list'),
    path('publishers/new/', views.publisher_create, name='publisher_create'),
    path('publishers/edit/<int:pk>/', views.publisher_update, name='publisher_update'),
    path('publishers/delete/<int:pk>/', views.publisher_delete, name='publisher_delete'),
]
