from django import forms

from base.models import Anfitrião


class FamiliaForm(forms.ModelForm):
    
    class Meta:
        model = Anfitrião
        fields = "__all__"