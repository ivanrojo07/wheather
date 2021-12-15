from django.db.models.base import Model
from django.forms import ModelForm, TextInput, fields, widgets
from .models import City

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name' : TextInput( attrs = { 'class':'input', 'placeholder': 'City Name' } ),
        }