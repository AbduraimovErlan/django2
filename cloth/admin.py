from django.contrib import admin
from . import models
from .models import ProductCL, ProductCL_Comment

admin.site.register(models.ProductCL)
admin.site.register(models.CustomerCL)
admin.site.register(models.TagCL)
admin.site.register(models.OrderCL)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('nameCL', 'emailCL', 'postCL', 'createdCL', 'activeCL')
    list_filter = ('activeCL', 'createdCL', 'updatedCL')
    search_fields = ('nameCL', 'emailCL', 'bodyCL')
admin.site.register(ProductCL_Comment, CommentAdmin)