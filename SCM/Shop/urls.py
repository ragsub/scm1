from django.urls import path

from SCM.Shop.views import view_shop, add_to_cart, view_cart, edit_cart, delete_cart

app_name = 'SCM.Shop'

urlpatterns=[
    path('<str:shop_name>/', view_shop, name='view_shop'),
    path('<str:shop_name>/cart/', view_cart, name='view_cart'),
    path('<str:shop_name>/cart/edit/<int:id>/', edit_cart, name='edit_cart'),
    path('<str:shop_name>/cart/delete/<int:id>/', delete_cart, name='delete_cart'),
    path('<str:shop_name>/<str:product_name>/', add_to_cart, name='add_to_cart'),

]