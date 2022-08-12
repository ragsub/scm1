from django.http import Http404, HttpRequest
from django.shortcuts import redirect, render
from django.db import IntegrityError
from django.db.models import Q, Sum
from django.contrib import messages
from django.forms import modelformset_factory
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


from SCM.settings import ITEMS_IN_PAGE
from SCM.Shop.models import Cart
from SCM.Shop.forms import AddCartForm
from SCM.Shop.filters import ProductInStoreFilter
from SCM.Tenant.models import Tenant
from SCM.Tenant.utils import tenant_context 
from SCM.Store.models import Store, ProductInStore
from SCM.Store.forms import AddProductInStoreForm
from SCM.Product.models import Category, Product


items_in_page = ITEMS_IN_PAGE

# Create your views here.
def view_shop(request:HttpRequest,tenant_name, shop_name):
    context = {}

    tenant = Tenant.objects.get(tenant=tenant_name)
    if not tenant:
        raise Http404('Page not found')

    
    with tenant_context(tenant):
        store = Store.objects.get(Q(description=shop_name))
        if not store:
            raise Http404('Page not found')

        context['title'] = store.description
        count = count_products(request.user, tenant, store)
        context['items_in_cart'] = count

        ProductInStoreFormset = modelformset_factory(ProductInStore, form=AddProductInStoreForm, extra=0)
        qs = ProductInStore.objects.filter(Q(store=store) & Q(active=True))
        category_qs = Category.objects.filter(Q(product__productinstore__store=store) & Q(product__productinstore__active=True)).distinct()
        product_in_store_filter = ProductInStoreFilter(request.GET, queryset=qs, active_categories_in_shop=category_qs)

        #paginate the filtered and grouped set
        paginator = Paginator(product_in_store_filter.qs,items_in_page)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['filter'] = product_in_store_filter
        context['page_obj'] = page_obj

        product_formset = ProductInStoreFormset(queryset=page_obj.object_list)
        context['formset'] = product_formset

        return render(request=request,template_name='shop/shop.html',context=context)

@login_required
def add_to_cart(request, tenant_name, shop_name, product_name):
    tenant = Tenant.objects.get(tenant=tenant_name)
    next_url = request.GET['next']
    if not tenant:
        raise Http404('Page not found')
    
    with tenant_context(tenant):
        store = Store.objects.get(Q(description=shop_name))
        if not store:
            raise Http404('Page not found')

        product = Product.objects.get(Q(description=product_name))
        if not product:
            raise Http404('Page not found')

        product_in_store = ProductInStore.objects.get(Q(store=store) & Q(product=product))
        if product_in_store is None:
            raise Http404('Page not found')

        cart_exists = Cart.objects.filter(store=store,product=product,user=request.user)
        if cart_exists:
            cart_exists = cart_exists[0]
            cart_exists.quantity = cart_exists.quantity+1
            cart_exists.total_price = cart_exists.quantity * cart_exists.price
        else:
            cart_exists = Cart(user=request.user, store=store, product=product, quantity=1, price=product_in_store.discounted_price, total_price=product_in_store.discounted_price)
        cart_exists.save()

    return redirect(next_url)

def count_products(user, tenant, store):
    count = Cart.objects.filter(user=user, tenant=tenant,store=store).aggregate(Sum('quantity'))['quantity__sum']
    if not count:
        count = 0
    return count

@login_required
def view_cart(request, tenant_name, shop_name):
    context = {}
    tenant = Tenant.objects.get(tenant=tenant_name)
    if not tenant:
        raise Http404('Page not found')
    
    with tenant_context(tenant):
        store = Store.objects.get(Q(description=shop_name))
        if not store:
            raise Http404('Page not found')


        context['title'] = store.description + ' cart'
        context['tenant'] = tenant.tenant
        context['store'] = store.description
        CartFormset = modelformset_factory(Cart, form=AddCartForm, extra=0)

        qs = Cart.objects.filter(store=store,user=request.user)

        cart_formset = CartFormset(queryset=qs)

        context['formset'] = cart_formset

        return render(request=request,template_name='shop/cart.html',context=context)


def edit_cart(request, tenant_name, shop_name, id):
    context = {}
    context['model_name'] = Cart._meta.verbose_name
    context['edit_url'] = 'SCM.Shop:edit_cart'
    context['delete_url'] = 'SCM.Shop:delete_cart'
    context['shop_name'] = shop_name

    cart_instance = Cart.objects.get(pk=id)
    context['edit_record_n'] = 'edit_record_' + str(id)

    if request.method == 'POST':
        form = AddCartForm(request.POST, request.FILES, instance=cart_instance)
        if form.is_valid():
            context['form'] = form
            try:
                form.save()
            except IntegrityError as e:
                if "unique_store_product" in e.args[0]: 
                    messages.add_message(request=request,level=messages.ERROR,message='Product already exists in this store')
            else:
                return render(request=request,template_name='shop/cart_edit_success.html',context=context)
        else:
            context['form'] = form
    else:
        cart_instance = Cart.objects.get(pk=id)
        context['form'] = AddCartForm(instance = cart_instance)
    return render(request=request,template_name='shop/cart_edit.html',context=context)

def delete_cart(request, tenant_name, shop_name, id):
    context={}
    context['name'] = Cart._meta.verbose_name
    context['delete_url'] = 'SCM.Shop:delete_cart'
    cart_instance = Cart.objects.get(pk=id)
    context['edit_record_n'] = 'edit_record_' + str(cart_instance.id)
    context['shop_name'] = shop_name

    if request.method=="POST":
        try:
            cart_instance.delete()
        except IntegrityError as p:
            if "Product" in p.args[0]:
                messages.add_message(request=request,level=messages.ERROR,message='Category ' + str(cart_instance) + ' has products defined. It cannot be deleted')
                context['instance'] = cart_instance
        else:
            return render(request=request,  template_name='scm/delete_success.html', context=context)
    else:
        context['instance'] = cart_instance
    return render(request=request,template_name='shop/cart_delete.html',context=context)
