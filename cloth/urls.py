from django.urls import path
from . import views


app_name = "productsCL"
urlpatterns = [
    path("productsCL/", views.ProductListViewCL.as_view(), name="productCL_list"),
    path("productsCL0/", views.ProductListViewCL0.as_view(), name="productCL0_list_all"),
    path("productsCL1/", views.ProductListViewCL1.as_view(), name="productCL1_list"),
    path("productsCL2/", views.ProductListViewCL2.as_view(), name="productCL2_list"),
    path("productsCL3/", views.ProductListViewCL3.as_view(), name="productCL3_list"),
    path("productsCLCOMM/", views.ProductListViewCLCOMM.as_view(), name="productsCL_list_COMM"),
    path("add-orderCL/", views.OrderCreateViewCL.as_view(), name="orderCL_create"),
    path('add-comment-productsCL/', views.CommentCreateViewCL.as_view(), name='add-comment-productsCL'),
    path("productsCL/<int:idCL>/", views.ProductDetailViewCL.as_view(), name="productCL_detail"),



]