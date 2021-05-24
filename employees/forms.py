from django import forms
from .models import Field
from django.contrib import messages
class NewEmployeeForm(forms.Form):
    username = forms.CharField(max_length=25,label="Kullanıcı adı",required=True)
    name = forms.CharField(max_length=20,label="Adı",required=True)
    surname = forms.CharField(max_length=20, label="Soyadı",required=True)
    password = forms.CharField(max_length=20,label="Şifre",widget=forms.PasswordInput,required=True)
    salary = forms.IntegerField(min_value=3000,max_value=25000,label="Maaş",required=True)
    home_location_lat = forms.FloatField(min_value=-360,max_value=360,label="Ev Lokasyon Latitude",required=True)
    home_location_long = forms.FloatField(min_value=-360,max_value=360,label="Ev Lokasyon Longitude",required=True)
    field = forms.ModelChoiceField(queryset=Field.objects.all(),required=True)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        surname = self.cleaned_data.get("surname")
        name = self.cleaned_data.get("name")
        salary = self.cleaned_data.get("salary")
        home_location_lat = self.cleaned_data.get("home_location_lat")
        home_location_long = self.cleaned_data.get("home_location_long")
        field = self.cleaned_data.get("field")


        values = {
            "username":username,
            "password":password,
            "surname":surname,
            "name":name,
            "salary":salary,
            "home_location_lat":home_location_lat,
            "home_location_long":home_location_long,
            "field":field
        }
        return values