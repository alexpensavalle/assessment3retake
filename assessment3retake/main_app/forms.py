from django import forms 
from .models import Item
  
# create a ModelForm 
class ItemForm(forms.ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = Item 
        fields = "__all__"