from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.utils import IntegrityError
from django.contrib.auth.decorators import login_required

from SCM.Store.filters import StoreFilter
from SCM.Store.models import Store
from SCM.Store.forms import AddStoreForm
from SCM.settings import ITEMS_IN_PAGE

items_in_page = ITEMS_IN_PAGE

# Create your views here.
@login_required
def view_stores(request):
    context = {}
    context['title'] = Store._meta.verbose_name
    store_filter = StoreFilter(request.GET, queryset=Store.objects.values('id','code','description','detail'))

    #paginate the filtered and grouped set
    paginator = Paginator(store_filter.qs,items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['filter'] = store_filter
    context['page_obj'] = page_obj

    return render(request=request,template_name='store/locations.html',context=context)

@login_required
def add_store(request):

    context = {}
    context['model_name'] = Store._meta.verbose_name

    if request.method == 'POST':
        form = AddStoreForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except IntegrityError as e:
                if "unique_store_code" in e.args[0]: 
                    messages.add_message(request=request,level=messages.ERROR,message='Store with code already exists')
                elif "unique_store_description" in e.args[0]:
                    messages.add_message(request=request,level=messages.ERROR,message='Store with description already exists')
                else:
                    print (e)
            else:
                messages.add_message(request=request,level=messages.SUCCESS,message='Store ' + str(form.instance) + ' added successfully' )
        else:
            print('form is not valid')
        context['form'] = form
        
    else:
        context['form'] = AddStoreForm()
    return render(request=request,template_name='scm/add.html',context=context)

@login_required
def edit_store(request, id):
    context = {}
    context['model_name'] = Store._meta.verbose_name

    store_instance = Store.objects.get(pk=id)
    if request.method == 'POST':
        form = AddStoreForm(request.POST, instance=store_instance)
        if form.is_valid():
            try:
                form.save()
            except IntegrityError as e:
                if "unique_store_code" in e.args[0]: 
                    messages.add_message(request=request,level=messages.ERROR,message='Store with code already exists')
                elif "unique_store_description" in e.args[0]:
                    messages.add_message(request=request,level=messages.ERROR,message='Store with description already exists')
            else:
                messages.add_message(request=request,level=messages.SUCCESS,message='Store '+str(form.instance) + ' updated successfully')
        
        context['form'] = form
        
    else:
        store_instance = Store.objects.get(pk=id)
        context['form'] = AddStoreForm(instance = store_instance)
    return render(request=request,template_name='scm/edit.html',context=context)

@login_required
def delete_store(request, id):
    context={}
    context['name'] = Store._meta.verbose_name
    store_instance = Store.objects.get(pk=id)
    if request.method=="POST":
        store_instance.delete()
        messages.add_message(request=request,level=messages.SUCCESS,message='Store '+ str(store_instance)+ ' deleted successfully')
    else:
        context['instance'] = store_instance
    return render(request=request,template_name='scm/delete.html',context=context)