from django.shortcuts import render
from django.db.models import Q
from django.forms import modelformset_factory
from django.core.paginator import Paginator

from SCM.Tenant.models import Tenant
from SCM.Tenant.utils import tenant_context 
from SCM.Store.models import Store, ProductInStore
from SCM.Store.forms import AddProductInStoreForm
from SCM.Shop.filters import ProductInStoreFilter
from SCM.settings import ITEMS_IN_PAGE
from SCM.Product.models import Category, Product


items_in_page = ITEMS_IN_PAGE

# Create your views here.
def view_shop(request,tenant_name, shop_name):
    context = {}
    tenant = Tenant.objects.get(tenant=tenant_name)
    if not tenant:
        print('tenant not found')
    
    with tenant_context(tenant):
        store = Store.objects.get(Q(description=shop_name))
        if not store:
            print('store not found')

        context = {}
        context['title'] = store.description
        
        ProductInStoreFormset = modelformset_factory(ProductInStore, form=AddProductInStoreForm, extra=0)
        #category_qs = Category.objects.all().product_set.all()
        qs = ProductInStore.objects.filter(Q(store=store) & Q(active=True))
        product_qs = Product.objects.filter(Q(productinstore__store=store) & Q(productinstore__active=True))
        category_qs = Category.objects.filter(Q(product__productinstore__store=store) & Q(product__productinstore__active=True)).distinct()
        product_in_store_filter = ProductInStoreFilter(request.GET, queryset=qs, active_products_in_shop=product_qs, active_categories_in_shop=category_qs)

        #paginate the filtered and grouped set
        paginator = Paginator(product_in_store_filter.qs,items_in_page)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['filter'] = product_in_store_filter
        context['page_obj'] = page_obj

        product_formset = ProductInStoreFormset(queryset=page_obj.object_list)
        context['formset'] = product_formset

        return render(request=request,template_name='shop/shop.html',context=context)