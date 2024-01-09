from django.shortcuts import get_object_or_404
from django.views import generic
from django.views.generic import ListView, DetailView, CreateView
from . import models, forms


class ProductListViewCL0(ListView):
    queryset = models.ProductCL.objects.filter().order_by("-id")
    template_name = "productsCL0_list_all.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter().order_by("-id")

class ProductListViewCL(ListView):
    queryset = models.ProductCL.objects.filter(tags__name='male')
    template_name = "productsCL_list.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name='male')


class ProductListViewCL1(ListView):
    queryset = models.ProductCL.objects.filter(tags__name='female')
    template_name = "productsCL1_list.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name='female')


class ProductListViewCL2(ListView):
    queryset = models.ProductCL.objects.filter(tags__name='baby')
    template_name = "productsCL2_list.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name='baby')

class ProductListViewCL3(ListView):
    queryset = models.ProductCL.objects.filter(tags__name='unisex')
    template_name = "productsCL3_list.html"

    def get_queryset(self):
        return models.ProductCL.objects.filter(tags__name='unisex')














# class ProductListViewCLCOMM(generic.ListView):
#     queryset = models.ProductCL_Comment.objects.filter().order_by("-id")
#     template_name = "productCL_detail_.html"
#
#     def get_queryset(self):
#         return models.ProductCL_Comment.objects.filter().order_by("-id")
#
# class ProductListViewCLCOMM11(ListView):
#     queryset = models.ProductCL.objects.filter().order_by("-id")
#     template_name = "productCL_detail_.html"
#
#     def get_queryset(self):
#         return models.ProductCL.objects.filter().order_by("-id")






class ProductDetailViewCL(DetailView):
    template_name = "productCL_detail.html"

    def get_object(self, **kwargs):
        productCL_id = self.kwargs.get("idCL")
        return get_object_or_404(models.ProductCL, id=productCL_id)



class ProductDetailViewCLCOM(generic.DetailView):
    template_name = "productCL_detail_COM.html"


    def get_object(self, **kwargs):
        productCL11_id = self.kwargs.get("id")
        return get_object_or_404(models.ProductCL, id=productCL11_id)


# class ProductDetailViewCLCOM(DetailView):
#     template_name = "productCL_detail_COM.html"
#
#     def get_object(self, **kwargs):
#         productCL11_id = self.kwargs.get("id")
#         return get_object_or_404(models.ProductCL, id=productCL11_id)




class OrderCreateViewCL(CreateView):
    template_name = "add_orderCL.html"
    form_class = forms.OrderFormCL
    success_url = "/productsCL/"
    queryset = models.OrderCL.objects.all()

    def form_valid(self, form):
        return super(OrderCreateViewCL, self).form_valid(form=form)

class CommentCreateViewCL(generic.CreateView):
    template_name = "add_comment_productsCL.html"
    form_class = forms.CommentForm
    queryset = models.ProductCL_Comment.objects.all()
    success_url = "/productsCL/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CommentCreateViewCL, self).form_valid(form=form)