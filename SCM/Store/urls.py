from django.urls import path

from SCM.Store.views import delete_product_in_store, view_stores, add_store, edit_store, delete_store, view_products_in_store, add_product_in_store, edit_product_in_store, delete_product_in_store

app_name = 'SCM.Store'

urlpatterns=[
    path('view/', view_stores, name='view_stores'),
    path('add/', add_store,name='add_store'),
    path('edit/<int:id>',edit_store,name='edit_store'),
    path('delete/<int:id>',delete_store,name='delete_store'),
    path('product/view/', view_products_in_store, name='view_product_in_stores'),
    path('product/add', add_product_in_store, name='add_product_in_store'),
    path('product/edit/<int:id>', edit_product_in_store, name='edit_product_in_store'),
    path('product/delete/<int:id>',delete_product_in_store,name='delete_product_in_store'),

]