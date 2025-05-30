from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('item_list')),  # redireciona "/" para a view 'item_list'
    path('', include('app.urls')),
]
