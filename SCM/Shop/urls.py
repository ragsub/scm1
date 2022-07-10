from django.urls import path

from SCM.Shop.views import view_shop

app_name = 'SCM.Shop'

urlpatterns=[
    path('<str:tenant_name>/<str:shop_name>/', view_shop, name='view_shop'),
]