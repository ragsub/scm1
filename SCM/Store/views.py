from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.utils import IntegrityError
from django.contrib.auth.decorators import login_required

from SCM.Store.filters import LocationFilter
from SCM.Store.models import Store
from SCM.Store.forms import AddLocationForm, UploadLocationForm

items_in_page=5

# Create your views here.
@login_required
def view_stores(request):
    context = {}
    location_filter = LocationFilter(request.GET, queryset=Store.objects.all())

    #paginate the filtered and grouped set
    paginator = Paginator(location_filter.qs,items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['filter'] = location_filter
    context['page_obj'] = page_obj

    return render(request=request,template_name='location/locations.html',context=context)

@login_required
def add_store(request):

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
                    print (e)
            else:
                messages.add_message(request=request,level=messages.SUCCESS,message='Location added successfully' )
        else:
            print('form is not valid')
        context['form'] = form
        
    else:
        context['form'] = AddLocationForm()
    return render(request=request,template_name='scm/add.html',context=context)

@login_required
def edit_store(request, location_id):
    context = {}
    location_instance = Store.objects.get(pk=location_id)
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
        location_instance = Store.objects.get(pk=location_id)
        context['form'] = AddLocationForm(instance = location_instance)
    return render(request=request,template_name='scm/edit.html',context=context)

@login_required
def delete_store(request, location_id):
    context={}
    context['name'] = Store._meta.verbose_name
    location_instance = Store.objects.get(pk=location_id)
    if request.method=="POST":
        location_instance.delete()
        messages.add_message(request=request,level=messages.SUCCESS,message='Location deleted successfully')
    else:
        context['instance'] = location_instance
    return render(request=request,template_name='scm/delete.html',context=context)