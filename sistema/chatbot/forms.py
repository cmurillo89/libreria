from django import forms



class chatbot(forms.Form):
    pregunta = forms.CharField(max_length=100)