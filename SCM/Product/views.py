from django.db import IntegrityError
from django.db.models import F
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages


from SCM.Product.models import Category, Product
from SCM.Product.filters import CategoryFilter, ProductFilter
from SCM.Product.forms import AddCategoryForm, AddProductForm
from SCM.settings import ITEMS_IN_PAGE

# Create your views here.
@login_required
def view_categories(request):
    context = {}
    context['title'] = Category._meta.verbose_name

    category_filter = CategoryFilter(request.GET, queryset=Category.objects.values('id','code','description','detail'))

    #paginate the filtered and grouped set
    paginator = Paginator(category_filter.qs,ITEMS_IN_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['filter'] = category_filter
    context['page_obj'] = page_obj

    return render(request=request,template_name='product/category.html',context=context)

@login_required
def add_category(request):
    context = {}
    context['model_name'] = Category._meta.verbose_name
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except IntegrityError as e:
                if "unique_category_code" in e.args[0]: 
                    messages.add_message(request=request,level=messages.ERROR,message='Category with code already exists')
                elif "unique_category_description" in e.args[0]:
                    messages.add_message(request=request,level=messages.ERROR,message='Category with description already exists')
                else:
                    print (e)
            else:
                messages.add_message(request=request,level=messages.SUCCESS,message='Category '+ str(form.instance) +' added successfully' )
        else:
            print('form is not valid')
        context['form'] = form
        
    else:
        context['form'] = AddCategoryForm()
    return render(request=request,template_name='scm/add.html',context=context)

@login_required
def edit_category(request, id):
    context = {}
    context['model_name'] = Category._meta.verbose_name

    category_instance = Category.objects.get(pk=id)
    if request.method == 'POST':
        form = AddCategoryForm(request.POST, instance=category_instance)
        if form.is_valid():
            try:
                form.save()
            except IntegrityError as e:
                if "unique_category_code" in e.args[0]: 
                    messages.add_message(request=request,level=messages.ERROR,message='Category with code already exists')
                elif "unique_category_description" in e.args[0]:
                    messages.add_message(request=request,level=messages.ERROR,message='Category with description already exists')
            else:
                messages.add_message(request=request,level=messages.SUCCESS,message='Category '+str(form.instance)+' updated successfully')
        
        context['form'] = form
        
    else:
        category_instance = Category.objects.get(pk=id)
        context['form'] = AddCategoryForm(instance = category_instance)
    return render(request=request,template_name='scm/edit.html',context=context)

@login_required
def delete_category(request, id):
    context={}
    context['model_name'] = Category._meta.verbose_name

    context['name'] = Category._meta.verbose_name
    category_instance = Category.objects.get(pk=id)
    if request.method=="POST":
        category_instance.delete()
        messages.add_message(request=request,level=messages.SUCCESS,message='Category '+ str(category_instance)+ ' deleted successfully')
    else:
        context['instance'] = category_instance
    return render(request=request,template_name='scm/delete.html',context=context)

@login_required
def view_products(request):
    context = {}
    context['title'] = Product._meta.verbose_name

    product_filter = ProductFilter(request.GET, 
        queryset=Product.objects.all()
        .values()
        .annotate(category=F('category__description'))
        .values('category','code','description','detail','photo','id')
    )

    #paginate the filtered and grouped set
    paginator = Paginator(product_filter.qs, ITEMS_IN_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['filter'] = product_filter
    context['page_obj'] = page_obj
    
    print(page_obj.object_list)
    
    return render(request=request,template_name='product/product.html',context=context)

@login_required
def add_product(request):
    context = {}
    context['model_name'] = Product._meta.verbose_name
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
            except IntegrityError as e:
                if "unique_product_code" in e.args[0]: 
                    messages.add_message(request=request,level=messages.ERROR,message='Product with code already exists')
                elif "unique_product_description" in e.args[0]:
                    messages.add_message(request=request,level=messages.ERROR,message='Product with description already exists')
                else:
                    print (e)
            else:
                messages.add_message(request=request,level=messages.SUCCESS,message='Product '+ str(form.instance) +' added successfully' )
        else:
            print('form is not valid')
        context['form'] = form
        
    else:
        context['form'] = AddProductForm()
    return render(request=request,template_name='scm/add.html',context=context)

@login_required
def edit_product(request, id):
    context = {}
    context['model_name'] = Product._meta.verbose_name

    product_instance = Product.objects.get(pk=id)
    if request.method == 'POST':
        form = AddProductForm(request.POST, instance=product_instance)
        if form.is_valid():
            try:
                form.save()
            except IntegrityError as e:
                if "unique_store_code" in e.args[0]: 
                    messages.add_message(request=request,level=messages.ERROR,message='Product with code already exists')
                elif "unique_store_description" in e.args[0]:
                    messages.add_message(request=request,level=messages.ERROR,message='Product with description already exists')
            else:
                messages.add_message(request=request,level=messages.SUCCESS,message='Product '+str(form.instance) + ' updated successfully')
        
        context['form'] = form
        
    else:
        product_instance = Product.objects.get(pk=id)
        context['form'] = AddProductForm(instance = product_instance)
    return render(request=request,template_name='scm/edit.html',context=context)

@login_required
def delete_product(request, id):
    context={}
    context['model_name'] = Product._meta.verbose_name

    context['name'] = Product._meta.verbose_name
    product_instance = Product.objects.get(pk=id)
    if request.method=="POST":
        product_instance.delete()
        messages.add_message(request=request,level=messages.SUCCESS,message='Product '+ str(product_instance)+ ' deleted successfully')
    else:
        context['instance'] = product_instance
    return render(request=request,template_name='scm/delete.html',context=context)