from django.forms import modelformset_factory
from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.utils import IntegrityError
from django.db.models.deletion import ProtectedError
from django.contrib.auth.decorators import login_required

from SCM.Store.filters import StoreFilter, ProductInStoreFilter
from SCM.Store.models import Store, ProductInStore
from SCM.Store.forms import AddStoreForm, AddProductInStoreForm
from SCM.settings import ITEMS_IN_PAGE

items_in_page = ITEMS_IN_PAGE

# Create your views here.

@login_required
def view_stores(request):
    context = {}
    context['title'] = Store._meta.verbose_name
    StoreFormset = modelformset_factory(Store, form=AddStoreForm, extra=0)

    store_filter = StoreFilter(request.GET, queryset=Store.objects.all())

    #paginate the filtered and grouped set
    paginator = Paginator(store_filter.qs,items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['filter'] = store_filter
    context['page_obj'] = page_obj

    store_formset = StoreFormset(queryset=page_obj.object_list)
    context['formset'] = store_formset

    return render(request=request,template_name='store/store.html',context=context)

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
    context['edit_url'] = "SCM.Store:edit_store"
    context['delete_url'] = "SCM.Store:delete_store"

    store_instance = Store.objects.get(pk=id)
    context['edit_record_n'] = 'edit_record_' + str(id)
    if request.method == 'POST':
        form = AddStoreForm(request.POST, request.FILES, instance=store_instance)
        if form.is_valid():
            context['form'] = form

            try:
                form.save()
            except IntegrityError as e:
                if "unique_store_code" in e.args[0]: 
                    messages.add_message(request=request,level=messages.ERROR,message='Store with code already exists')
                elif "unique_store_description" in e.args[0]:
                    messages.add_message(request=request,level=messages.ERROR,message='Store with description already exists')
            else:
                return render(request=request,template_name='scm/edit_success.html',context=context)
    else:
        store_instance = Store.objects.get(pk=id)
        context['form'] = AddStoreForm(instance = store_instance)
    return render(request=request,template_name='scm/edit.html',context=context)

@login_required
def delete_store(request,id):
    context={}
    context['name'] = Store._meta.verbose_name
    context['delete_url'] = 'SCM.Store:delete_store'
    store_instance = Store.objects.get(pk=id)
    context['edit_record_n'] = 'edit_record_' + str(store_instance.id)

    if request.method=="POST":
        try:
            store_instance.delete()
        except ProtectedError as p:
            if "ProductInStore" in p.args[0]:
                messages.add_message(request=request,level=messages.ERROR,message='Store ' + str(store_instance) + ' has products defined. It cannot be deleted')
                context['instance'] = store_instance
        else:
            return render(request=request,  template_name='scm/delete_success.html', context=context)
    else:
        context['instance'] = store_instance
    return render(request=request,template_name='scm/delete.html',context=context)


@login_required
def view_products_in_store(request):
    context = {}
    context['title'] = ProductInStore._meta.verbose_name
    ProductInStoreFormset = modelformset_factory(ProductInStore, form=AddProductInStoreForm, extra=0)

    product_in_store_filter = ProductInStoreFilter(request.GET, queryset=ProductInStore.objects.select_related('store','product'))

    #paginate the filtered and grouped set
    paginator = Paginator(product_in_store_filter.qs,items_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['filter'] = product_in_store_filter
    context['page_obj'] = page_obj

    product_in_store_formset = ProductInStoreFormset(queryset=page_obj.object_list)
    context['formset'] = product_in_store_formset

    return render(request=request,template_name='store/product_in_store.html',context=context)


@login_required
def add_product_in_store(request):

    context = {}
    context['model_name'] = ProductInStore._meta.verbose_name

    if request.method == 'POST':
        form = AddProductInStoreForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except IntegrityError as e:
                if "unique_store_product" in e.args[0]: 
                    messages.add_message(request=request,level=messages.ERROR,message='Product already exists in this store')
                else:
                    print (e)
            else:
                messages.add_message(request=request,level=messages.SUCCESS,message= str(form.instance) + ' added successfully' )
        else:
            print('form is not valid')
        context['form'] = form
        
    else:
        context['form'] = AddProductInStoreForm()
    return render(request=request,template_name='scm/add.html',context=context)

@login_required
def edit_product_in_store(request, id):
    context = {}
    context['model_name'] = ProductInStore._meta.verbose_name
    context['edit_url'] = "SCM.Store:edit_product_in_store"
    context['delete_url'] = "SCM.Store:delete_product_in_store"


    product_in_store_instance = ProductInStore.objects.get(pk=id)
    context['edit_record_n'] = 'edit_record_' + str(id)
    print(request.POST)
    if request.method == 'POST':
        form = AddProductInStoreForm(request.POST, request.FILES, instance=product_in_store_instance)
        if form.is_valid():
            context['form'] = form

            try:
                form.save()
            except IntegrityError as e:
                if "unique_store_product" in e.args[0]: 
                    messages.add_message(request=request,level=messages.ERROR,message='Product already exists in this store')
            else:
                return render(request=request,template_name='scm/edit_success.html',context=context)
        
    else:
        product_in_store_instance = ProductInStore.objects.get(pk=id)
        context['form'] = AddProductInStoreForm(instance = product_in_store_instance)
    return render(request=request,template_name='scm/edit.html',context=context)

@login_required
def delete_product_in_store(request,id):
    context={}
    context['name'] = ProductInStore._meta.verbose_name
    context['delete_url'] = 'SCM.Store:delete_product_in_store'
    product_in_store_instance = ProductInStore.objects.get(pk=id)
    context['edit_record_n'] = 'edit_record_' + str(product_in_store_instance.id)

    if request.method=="POST":
        product_in_store_instance.delete()
        messages.add_message(request=request,level=messages.SUCCESS,message='Store '+ str(product_in_store_instance)+ ' deleted successfully')
        return render(request=request,  template_name='scm/delete_success.html', context=context)
    else:
        context['instance'] = product_in_store_instance
    return render(request=request,template_name='scm/delete.html',context=context)