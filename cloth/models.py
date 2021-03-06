from django.db import models


class CustomerCL(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class TagCL(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductCL(models.Model):
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='', null=True)
    price = models.PositiveIntegerField()
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(TagCL)

    def __str__(self):
        return self.name


class OrderCL(models.Model):
    STATUS = (
        ("Обробатывается", "Обробатывается"),
        ("Выехал", "Выехал"),
        ("Доставлен", "Доставлен"),
    )
    customer = models.ForeignKey(CustomerCL, on_delete=models.CASCADE)
    product = models.ForeignKey(
        ProductCL, on_delete=models.CASCADE, related_name="order_product"
    )
    date_created = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=200, choices=STATUS)

    def __str__(self):
        return self.product.name



class ProductCL_Comment(models.Model):
    postCL = models.ForeignKey(ProductCL, on_delete=models.CASCADE, related_name='commentsCL', null=True)
    nameCL = models.CharField(max_length=80, null=True)
    bodyCL = models.TextField(null=True)
    emailCL = models.EmailField(null=True)
    createdCL = models.DateTimeField(auto_now_add=True, null=True)
    updatedCL = models.DateTimeField(auto_now=True, null=True)
    activeCL = models.BooleanField(default=True, null=True)


    def __str__(self):
        return 'Comment by {} on {}'.format(self.nameCL, self.postCL)