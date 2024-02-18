from django import forms

class MessageForm(forms.Form):
    message  = forms.CharField(label='values')
    mess_1  = forms.CharField(label='values')
     