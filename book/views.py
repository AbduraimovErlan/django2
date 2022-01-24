from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from . import models, forms
from django.views import generic

class BooksListView(generic.ListView):
    template_name = "books_list.html"
    queryset = models.Book.objects.all()

    def get_queryset(self):
        return models.Book.objects.filter().order_by("-id")



class BooksDetailView(generic.DetailView):
    template_name = "books_detail.html"

    def get_object(self, **kwargs):
        shows_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=shows_id)



class BooksCreateView(generic.CreateView):
    template_name = "add_books.html"
    form_class = forms.BookForm
    queryset = models.Book.objects.all()
    success_url = "/books/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BooksCreateView, self).form_valid(form=form)



class BooksUpdateView(generic.UpdateView):
    template_name = "book_update.html"
    form_class = forms.BookForm
    success_url = "/books/"

    def get_object(self, *kwargs):
        books_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=books_id)

    def form_valid(self, form):
        return super(BooksUpdateView, self).form_valid(form=form)




class BooksDeleteView(generic.DeleteView):
    template_name = "book_delete.html"
    success_url = "/books/"

    def get_object(self, **kwargs):
        books_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, id=books_id)




