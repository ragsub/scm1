from django.forms.utils import ErrorList

class CustomErrorList(ErrorList):
    template_name = 'scm/error_template.html'