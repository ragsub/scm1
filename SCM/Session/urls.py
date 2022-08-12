from django.urls import path
from SCM.Session.views import LoginUser, logout_user

app_name = 'SCM.Session'

urlpatterns=[
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]
