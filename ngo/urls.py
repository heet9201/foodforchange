from django.urls import path
from . import views


urlpatterns = [
    path('', (views.ngo_index), name='ngo_index'),
    path('profile', (views.profilepage), name='ngo_profile'),
    path('vneeded', (views.vneeded), name='vneeded'),
    path('nvsession', (views.nvsession), name='nvsession'),
    path('participated_volunteers', (views.vparticipated), name='vparticipated'),
    path('register', (views.ngo_register), name='ngo_register'),
    path('ngo_login_check', (views.ngo_login_check), name='ngo_login_check'),
    path('login', (views.ngo_login), name='ngo_login_page'),
    path('ngo_register_check', (views.ngo_register_check), name='ngo_register_check'),
    path('ngo_session',(views.ngo_session),name = 'ngo_session'),
]