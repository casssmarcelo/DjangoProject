from django import forms
from .models import Item
from .models import Author


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email', 'bio']
