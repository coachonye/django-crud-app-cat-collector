from django import forms
from .models import Cat

class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = ['name', 'breed', 'description', 'age']

from django.forms import ModelForm
from .models import Feeding

class FeedingForm(ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal']
