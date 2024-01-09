from django import forms
from . import models
from .models import Book_Comment


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = "__all__"



class CommentForm(forms.ModelForm):
    class Meta:
        model = Book_Comment
        fields = "__all__"


