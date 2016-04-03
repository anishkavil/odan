from django import forms
from django.contrib.messages.storage.base import Message

class ContactForm(forms.Form):
    
    Name = forms.CharField(max_length=50)
    Email= forms.EmailField()
    Subject = forms.CharField(max_length=100)
    Message = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "80", 'rows': "20", }))
    
    
    