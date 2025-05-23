from django import forms
from .models import EmployerInfo

class EmployerInfoForm(forms.ModelForm):
    class Meta:
        model = EmployerInfo
        fields = '__all__'