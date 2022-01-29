from django.contrib import admin
from . import models
from .models import Book, Book_Comment

admin.site.register(models.Book)
admin.site.register(models.BookRating)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
admin.site.register(Book_Comment, CommentAdmin)

