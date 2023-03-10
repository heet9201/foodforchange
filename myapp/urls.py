from django.urls import path
from . import views


urlpatterns = [
    path('', (views.index), name='index'),
    path('feed', (views.feed), name='feed'),
    path('leaderboard', (views.leaderboard), name='leaderboard'),
    path('profile', (views.profilepage), name='profile'),
    path('loginpage', views.loginpage, name='loginpage'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signuppage'),
    path('register', (views.register), name='register'),
    path('vsession', (views.session), name='vsession'),
    path('logout', views.logout, name='logout'),
    path('pp_img', views.pp_img, name='pp_img'),
]
