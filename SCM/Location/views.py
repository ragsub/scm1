from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.utils import IntegrityError

from SCM.Location.filters import LocationFilter
from SCM.Location.models import Location
from SCM.Location.forms import AddLocationForm

items_in_page=5

# Create your views here.
def view_locations(request):
    context = {}
    location_filter = LocationFilter(request.GET, queryset=Location.objects.all())

    #paginate the filtered and grouped set
    paginator = Paginator(location_filter.qs,items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['filter'] = location_filter
    context['qs'] = page_obj

    return render(request=request,template_name='location/locations.html',context=context)


def add_location(request):

    context = {}
    if request.method == 'POST':
        form = AddLocationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except IntegrityError as e:
                if "unique_location_code" in e.args[0]: 
                    messages.add_message(request=request,level=messages.ERROR,message='Location with code already exists')
                elif "unique_location_description" in e.args[0]:
                    messages.add_message(request=request,level=messages.ERROR,message='Location with description already exists')
            else:
                messages.add_message(request=request,level=messages.SUCCESS,message='Location added successfully' )
        
        context['form'] = form
        
    else:
        context['form'] = AddLocationForm()
    return render(request=request,template_name='location/add.html',context=context)