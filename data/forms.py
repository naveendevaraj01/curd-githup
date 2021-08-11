from django import forms
from data.models import Employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"
