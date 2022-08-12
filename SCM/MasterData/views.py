from unicodedata import category
from django.forms import modelformset_factory

from SCM.CustomGenericView.views import CustomListView, CustomCreateView, CustomUpdateView, CustomDeleteView
from SCM.MasterData.filters import StoreFilter, CategoryFilter
from SCM.MasterData.models import Store, Category
from SCM.MasterData.forms import AddStoreForm, AddCategoryForm
from SCM.settings import ITEMS_IN_PAGE

items_in_page = ITEMS_IN_PAGE

# Create your views here.

class ViewStores(CustomListView):
    model = Store
    template_name='masterdata/store.html'
    paginate_by = items_in_page
    filterset_class = StoreFilter
    permission_required = ('Store.view_store')
    formset_name = modelformset_factory(Store, form=AddStoreForm, extra=0)

class CreateStore(CustomCreateView):
    model = Store
    form_class = AddStoreForm
    permission_required = ('Store.add_store')

class UpdateStore(CustomUpdateView):
    model = Store
    form_class = AddStoreForm
    permission_required = ('Store.change_store')

class DeleteStore(CustomDeleteView):
    model = Store
    permission_required = ('Store.delete_store')

class ViewCategories(CustomListView):
    model = Category
    template_name='masterdata/category.html'
    paginate_by = items_in_page
    filterset_class = CategoryFilter
    permission_required = ('Category.view_category')
    formset_name = modelformset_factory(Store, form=AddCategoryForm, extra=0)

class CreateStore(CustomCreateView):
    model = Category
    form_class = AddCategoryForm
    permission_required = ('Category.add_category')

class UpdateStore(CustomUpdateView):
    model = Store
    form_class = AddStoreForm
    edit_url = 'SCM.MasterData:edit_category'
    delete_url = 'SCM.MasterData:delete_category'
    permission_required = ('Store.change_category')

class DeleteStore(CustomDeleteView):
    model = Store
    edit_url = 'SCM.MasterData:edit_category'
    delete_url = 'SCM.MasterData:delete_category'
    shop_url = 'SCM.shop:view_category'
    permission_required = ('Store.delete_category')
