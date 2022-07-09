from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.userAccount, name="profile"),
    path('add_brush',views.addBrush, name='add_brush'),
]