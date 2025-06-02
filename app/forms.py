from django import forms
from .models import Item, Category, Publisher, Author

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'items']

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'items']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'items']
