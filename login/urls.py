from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from mainPage import views as main_views
urlpatterns = [
    
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('mainPage/', main_views.mainPage, name='mainPage'),
   
]
