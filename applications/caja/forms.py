from django import forms
from .models import Caja


class CajaForm(forms.ModelForm):
    
  class Meta:
    model = Caja
    fields = ('__all__')
