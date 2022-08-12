from django.urls import path
from SCM.Account.views import welcome_user, CustomPasswordChangeView

app_name = 'SCM.Account'

urlpatterns=[
    path('welcome/', welcome_user, name='welcome'),
    path('password/change',CustomPasswordChangeView.as_view(), name='change_password'),
]
