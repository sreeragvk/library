from django import forms
from library.models import Book

class Bookform(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'