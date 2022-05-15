from django.urls import path

from SCM.Store.views import view_stores, add_store, edit_store, delete_store

app_name = 'SCM.Store'

urlpatterns=[
    path('view/', view_stores, name='view_stores'),
    path('add/', add_store,name='add_store'),
    path('edit/<int:location_id>',edit_store,name='edit_store'),
    path('delete/<int:location_id>',delete_store,name='delete_store'),
]