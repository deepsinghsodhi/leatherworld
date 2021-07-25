from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminhome),
    path('manageusers/', views.manageusers),
    path('manageuserstatus/', views.manageuserstatus),
    path('managecategories/', views.managecategories),
    path('managesubcategory/', views.managesubcategory),
    path('manageproduct/', views.manageproduct),
    path('viewproduct/', views.viewproduct),
    path('fetchSubCategory/', views.fetchSubCategory),
]
