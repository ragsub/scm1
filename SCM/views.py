

class ConvertToFormsetMixin:
    formset_name = None    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        #convert queryset to formset
        formset = self.formset_name(queryset=context['object_list'])
        context['formset'] = formset
        
        #populate the tenant_name
        context['tenant_name'] = self.kwargs.get('tenant_name',None)
        context['title'] = getattr(getattr(self.model,'_meta'),'verbose_name')
        return context

class IncludeTenantPermissionMixin:
    def get_permission_required(self):
        perm = super().get_permission_required()

        tenant = self.kwargs.get('tenant_name',None)
        tenant_permission = getattr(self.model,'__name__') + '.' + tenant
        print(tenant_permission)
        
        new_perm = perm + (tenant_permission,)
        return new_perm

class PassURLParametersToFormMixin:
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # update the kwargs for the form init method with yours
        kwargs.update(self.kwargs)  # self.kwargs contains all url conf params
        return kwargs

class EnhanceEditDeleteViewMixin:
    edit_url = None
    delete_url = None
    shop_url = None

    def get_success_url(self):
        return self.request.GET.get('next',None)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tenant_name'] = self.kwargs.get('tenant_name',None)
        context['model_name'] = getattr(getattr(self.model,'_meta'),'verbose_name')
        context['edit_url'] = self.edit_url
        context['delete_url'] = self.delete_url
        context['shop_url'] = self.shop_url
        context['success_url'] = self.request.GET.get('next',None)
        context['edit_record_n'] = 'edit_record_' + str(self.kwargs.get('id',None))
        context['instance'] = self.object  

        return context



    