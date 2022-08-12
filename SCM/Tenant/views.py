from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import Group


from SCM.User.forms import NewUserForm
from SCM.Tenant.forms import NewTenantForm

from SCM.Tenant.crud import add_user_to_tenant


# Create your views here.
def register_tenant(request):
    context = {}
    if request.method == 'POST':
        user_form = NewUserForm(request.POST, prefix='user')
        tenant_form = NewTenantForm(request.POST, prefix='tenant')

        if user_form.is_valid() and tenant_form.is_valid():
            new_user = user_form.save()
            new_tenant = tenant_form.save()

            tenant_group = Group.objects.create(name=new_tenant.tenant)
            owner_group = Group.objects.get(name='Owner')
            new_user.groups.add(tenant_group, owner_group)

            add_user_to_tenant(new_user, new_tenant)

            messages.add_message(request=request,level=messages.SUCCESS,message='Account added. Login now.')

        
        context['user_form'] = user_form
        context['tenant_form'] = tenant_form

    else:
        context['user_form'] = NewUserForm(prefix='user')
        context['tenant_form'] = NewTenantForm(prefix='tenant')
    
    return render(
        request = request, 
        template_name='tenant/register.html',
        context=context
    )