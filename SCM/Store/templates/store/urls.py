from django.urls import path

from SCM.Location.views import view_locations, add_location, edit_location, delete_location

app_name = 'SCM.Location'

urlpatterns=[
    path('view/', view_locations, name='view_locations'),
    path('add/', add_location,name='add_location'),
    path('edit/<int:location_id>',edit_location,name='edit_location'),
    path('delete/<int:location_id'>,delete_location,name='delete_location'),
]