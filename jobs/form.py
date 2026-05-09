from django import forms
from .models import Job
from .models import Company

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'logo']
