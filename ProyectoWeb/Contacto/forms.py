from django import forms

class Formulario(forms.Form):
    Nombre=forms.CharField(label="Asunto",max_length=60,required=True)
    email=forms.EmailField(label="Email",required=True)
    mensaje=forms.CharField(label="Mensaje",required=True, widget=forms.Textarea)