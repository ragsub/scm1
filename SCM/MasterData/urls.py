from django.urls import path

from SCM.MasterData.views import ViewStores, CreateStore, UpdateStore, DeleteStore

app_name = 'SCM.MasterData'

urlpatterns=[
    path('store/view/', ViewStores.as_view(), name='view_stores'),
    path('store/add/', CreateStore.as_view(),name='add_store'),
    path('store/edit/<int:id>', UpdateStore.as_view(),name='edit_store'),
    path('store/delete/<int:id>', DeleteStore.as_view(),name='delete_store'),
    path('category/view/', ViewStores.as_view(), name='view_categories'),
    path('category/add/', CreateStore.as_view(),name='add_category'),
    path('category/edit/<int:id>', UpdateStore.as_view(),name='edit_category'),
    path('category/delete/<int:id>', DeleteStore.as_view(),name='delete_category'),
]