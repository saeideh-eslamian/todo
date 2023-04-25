from django import forms
from .models import ToDo

class ToDOForm(forms.ModelForm):
  
     
    class Meta:
        model = ToDo
        fields =('title','description','expiry_date')
        labels ={
            'title': 'Title',
            'description': 'Description',
            'complete':'Complete',
            'expiry_date':'Expiry Date',
        }
        widgets = {
            'expiry_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'complete' : forms.RadioSelect
        }


