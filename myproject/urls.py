from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('products/', views.products),
    path('register/', views.register),
    path('checkEmail/', views.checkEmail),
    path('login/', views.login),
    path('myadmin/',include('myadmin.urls')),
    path('users/',include('users.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)