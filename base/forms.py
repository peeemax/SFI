from django import forms

from base.models import Anfitrião, Morador


class FamiliaForm(forms.ModelForm):
    
    class Meta:
        model = Anfitrião
        fields = "__all__"
        

class MoradorForm(forms.ModelForm):
    
    class Meta:
        model = Morador
        fields = "__all__"