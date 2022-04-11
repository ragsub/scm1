from django.urls import path

from SCM.Location.views import view_locations, add_location

app_name = 'SCM.Location'

urlpatterns=[
    path('view/', view_locations, name='view_locations'),
    path('add/',add_location,name='add_location')
]