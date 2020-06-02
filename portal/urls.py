from django.urls import path
from .import views

urlpatterns = [

    path('', views.home, name='home'),
    path('createdetail/', views.createdetail, name='createdetail'),
    path('updatedetail/<int:pk>', views.updatedetail, name='updatedetail'),
    path('deletedetail/<int:pk>', views.deletedetail, name='deletedetail'),

]