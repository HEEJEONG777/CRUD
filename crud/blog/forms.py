from django import forms    
from .models import Human

class CreateForm(forms.ModelForm):
    class Meta:
        model = Human
        fields = ['name']