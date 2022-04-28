from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.utils import IntegrityError

from SCM.Location.filters import LocationFilter
from SCM.Location.models import Location
from SCM.Location.forms import AddLocationForm, UploadLocationForm
from SCM.Location.tasks import upload_location_file
from SCM.Tenant.utils import get_current_tenant

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
    context['page_obj'] = page_obj

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

def edit_location(request, location_id):
    context = {}
    location_instance = Location.objects.get(pk=location_id)
    if request.method == 'POST':
        form = AddLocationForm(request.POST, instance=location_instance)
        if form.is_valid():
            try:
                form.save()
            except IntegrityError as e:
                if "unique_location_code" in e.args[0]: 
                    messages.add_message(request=request,level=messages.ERROR,message='Location with code already exists')
                elif "unique_location_description" in e.args[0]:
                    messages.add_message(request=request,level=messages.ERROR,message='Location with description already exists')
            else:
                messages.add_message(request=request,level=messages.SUCCESS,message='Location updated successfully')
        
        context['form'] = form
        
    else:
        location_instance = Location.objects.get(pk=location_id)
        context['form'] = AddLocationForm(instance = location_instance)
    return render(request=request,template_name='location/edit.html',context=context)

def upload_location(request):
    context = {}
    if request.method == 'POST':
        form = UploadLocationForm(request.POST, request.FILES)
        if form.is_valid():
            csv = request.FILES['file']
            tenant = get_current_tenant()
            upload_location_file.delay(request.user.id, tenant.id, csv.read().decode())
            messages.add_message(request, messages.SUCCESS, 'Upload submitted. Check status on email')
        else:
            context['form'] = form
    else:
        form = UploadLocationForm()
        context['form'] = form
    return render(request, 'location/upload_file.html', context)
