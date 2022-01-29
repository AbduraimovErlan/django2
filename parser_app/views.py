from django.http import HttpResponse
from django.views.generic import ListView, FormView
from . import parser, models, forms
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic



class Shows_p_ListView(generic.ListView):
    template_name = "shows_list_p.html"
    queryset = models.Film.objects.all()

    def get_queryset(self):
        return models.Film.objects.filter().order_by("-id")



class Shows_p_DetailView(generic.DetailView):
    template_name = "shows_detail_p.html"

    def get_object(self, **kwargs):
        shows_id = self.kwargs.get("id")
        return get_object_or_404(models.Film, id=shows_id)







class ParserFormView(FormView):
    template_name = "parser.html"
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            # return HttpResponse('Parser Success')
            return redirect(reverse('parser:shows_all_p'))
        else:
            return super(ParserFormView, self).post(request, *args, **kwargs)
