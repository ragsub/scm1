from django import forms

class ReceiveURLParametersInFormMixin:
    tenant_name = None

    def __init__(self, tenant_name=None, id=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tenant_name = tenant_name

class CustomModelForm(ReceiveURLParametersInFormMixin, forms.ModelForm):
    pass
