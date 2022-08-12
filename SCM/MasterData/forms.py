from django import forms
from django.db.models import Q

from SCM.Tenant.models import Tenant
from SCM.MasterData.models import Store, Category
from SCM.CustomGenericView.forms import CustomModelForm

class AddStoreForm(CustomModelForm):

    class Meta:
        model = Store
        fields = ['code','description','detail','latitude','longitude']
        widgets = {
            'code': forms.TextInput(),
            'description': forms.TextInput(),
            'detail': forms.TextInput(),
            'latitude': forms.TextInput(),
            'longitude': forms.TextInput()
        }

    def clean_code(self):
        code = self.cleaned_data['code']
        tenant_name = self.tenant_name

        if 'code' in self.changed_data:
            tenant = Tenant.objects.get(tenant=tenant_name)
            if Store.objects.filter(Q(tenant=tenant) & Q(code=code)).exists():
                raise forms.ValidationError(('Store with code %(value)s already exists'), code='duplicate_code', params={'value': code})

        return code
      
    def clean_description(self):
        description = self.cleaned_data['description']
        
        tenant_name = self.tenant_name
        if 'description' in self.changed_data:
            tenant = Tenant.objects.get(tenant=tenant_name)
            if Store.objects.filter(Q(tenant=tenant) & Q(description=description)).exists():
                raise forms.ValidationError(('Store with description %(value)s already exists'), code='duplicate_description', params={'value': description})

        return description


class AddCategoryForm(CustomModelForm):

    class Meta:
        model = Category
        fields = ['code','description','detail']
  
    def clean_code(self):
        code = self.cleaned_data['code']
        tenant_name = self.tenant_name

        if 'code' in self.changed_data:
            tenant = Tenant.objects.get(tenant=tenant_name)
            if Store.objects.filter(Q(tenant=tenant) & Q(code=code)).exists():
                raise forms.ValidationError(('Category with code %(value)s already exists'), code='duplicate_code', params={'value': code})

        return code
      
    def clean_description(self):
        description = self.cleaned_data['description']
        
        tenant_name = self.tenant_name
        if 'description' in self.changed_data:
            tenant = Tenant.objects.get(tenant=tenant_name)
            if Store.objects.filter(Q(tenant=tenant) & Q(description=description)).exists():
                raise forms.ValidationError(('Category with description %(value)s already exists'), code='duplicate_description', params={'value': description})

        return description