from django.forms import ModelForm
from .models import *

# class ContactForm(forms.Form):
#     name=forms.CharField(max_length=50)
#     email=forms.EmailField()
#     text=forms.CharField(max_length=1000,widget=forms.Textarea)

class ContactForm(ModelForm):
    class Meta:
        model=contact
        fields=['name','email','message']