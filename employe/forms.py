from django import forms
from .models import Employe

class employeForms(forms.ModelForm):
    class Meta :
        model = Employe
        fields = ["nom", "email", "poste", "salaire"]
        widgets = {
            'nom' : forms.TextInput(attrs ={
                'class' : 'input w-full',
                'placeholder' : 'Entrer votre nom'
            }),
            
            'email' : forms.TextInput(attrs ={
                'class' : 'input w-full',
                'placeholder' : 'Entrer votre email'
            }),
            
            'poste' : forms.TextInput(attrs ={
                'class' : 'input w-full',
                'placeholder' : 'Entrer votre poste'
            }),
            
            'salaire' : forms.TextInput(attrs ={
                'class' : 'input w-full',
                'placeholder' : 'salaire'
            })
        } 