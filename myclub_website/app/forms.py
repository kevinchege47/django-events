from django import forms
from django.forms import ModelForm
from .models import Venue

#create a venue form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = "__all__"
        labels={
            "name":'',
            "address":'',
            "zip_code":'',
            "phone":'',
            "web":'',
            "email_address":''
        }
        widgets = {
            "name":forms.TextInput(attrs={'class':'form-control','placeholder':'Venue Name'}),
            "address": forms.TextInput(attrs={'class':'form-control','placeholder':'Adress'}),
            "zip_code": forms.TextInput(attrs={'class':'form-control','placeholder':'Zip Code'}),
            "phone": forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}),
            "web": forms.TextInput(attrs={'class':'form-control','placeholder':'Web'}),
            "email_address": forms.EmailInput(attrs={'class':'form-control','placeholder':'email_address'})
        }
