from django.urls import path
from SCM.Session.views import LoginUser, welcome_user, logout_user

app_name = 'SCM.Session'

urlpatterns=[
    path('login/', LoginUser.as_view(), name='login'),
    path('welcome/', welcome_user, name='welcome'),
    path('logout/', logout_user, name='logout'),


]
