from django import forms


from .models import Banco, Sucursal, Deposito

    

class DespositosForm(forms.ModelForm):
    
    class Meta:
        model =  Deposito
        fields = ('__all__')

    def clean(self):
        cleaned_data = super().clean()
        fecha = cleaned_data.get('fecha')
        print(fecha)
        if not Deposito.objects.filter(created__icontains =  fecha).exists():
            raise forms.ValidationError('No es posible agregar depositos a fechas anteriores, por favor verifique su fecha e intente nuevamente')
        return cleaned_data