from django import forms
from . import models


class OrderFormCL(forms.ModelForm):
    class Meta:
        model = models.OrderCL
        fields = "__all__"


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.ProductCL_Comment
        fields = "__all__"