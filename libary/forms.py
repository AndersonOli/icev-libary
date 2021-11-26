from django.forms import ModelForm
from django import forms
from .models import Book

class BookForm(ModelForm):
  class Meta:
    model = Book
    fields = ['title', 'author', 'num_pages', 'year_launched', 'description']

