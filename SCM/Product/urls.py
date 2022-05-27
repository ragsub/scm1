from django.urls import path

from SCM.Product.views import delete_product, view_categories, add_category, edit_category, delete_category, view_products, add_product, edit_product, delete_product

app_name = 'SCM.Product'

urlpatterns=[
    path('view_categories/', view_categories, name='view_categories'),
    path('add_category/', add_category,name='add_category'),
    path('edit_category/<int:id>',edit_category,name='edit_category'),
    path('delete_category/<int:id>',delete_category,name='delete_category'),
    path('view_products/',view_products,name='view_products'),
    path('add_product/', add_product,name='add_product'),
    path('edit_product/<int:id>', edit_product,name='edit_product'),
    path('delete_product/<int:id>',delete_product,name='delete_product'),




]