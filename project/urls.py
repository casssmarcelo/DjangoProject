from django.contrib import admin
from django.urls import path, include
from app.views import author_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', author_list, name='home'),
    path('authors/', include('app.urls')),

]
