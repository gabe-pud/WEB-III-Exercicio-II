from django import forms
from app.models import Desenvolvedor
from app.models import Contato

class FormDesenvolvedor(forms.ModelForm):
    class Meta:
        model = Desenvolvedor
        fields = "__all__"

class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        fields = "__all__"
    
    
