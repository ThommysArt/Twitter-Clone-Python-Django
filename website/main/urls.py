from django.urls import path
from django.conf.urls import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.Login, name='login'),
    path('home', views.home, name='home'),
    path('login', views.Login, name='login'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('tweet', views.tweet, name='tweet'),
    path('profile', views.profile, name='profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
]


