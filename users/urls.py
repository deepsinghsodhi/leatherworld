from django.urls import path
from . import views

urlpatterns = [
    path('', views.userhome),
    path('vdeals/', views.vdeals),
    path('vscdeals/', views.vscdeals),
    path('vpdeals/', views.vpdeals),
    path('products/<int:myid>', views.productview),
    path('cpuser/', views.cpuser),
    path('epuser/', views.epuser),
    # path('bidproduct/', views.bidproduct),
    # path('bidresult/', views.bidresult),
]
