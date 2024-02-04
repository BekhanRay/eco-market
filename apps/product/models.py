from django.db import models
from django_resized import ResizedImageField


# ___________________________Category_________________________________________________________

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='category name', unique=True)

    def upload_to(self, filename):
        """
        :param filename:
        :return: image path
        """
        return f'category/{self.name}/{filename}'

    image = ResizedImageField(upload_to=upload_to, verbose_name='Category photo path')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


# ___________________________Type_________________________________________________________

class Type(models.Model):
    name = models.CharField(max_length=100, verbose_name='type name', unique=True)
    category_id = models.ForeignKey('Category', on_delete=models.DO_NOTHING)

    def upload_to(self, filename):
        """
        :param filename:
        :return: image path
        """
        return f'type/{self.name}/{filename}'

    image = ResizedImageField(upload_to=upload_to, verbose_name='Type photo path')


# ___________________________Product_________________________________________________________

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='product name', unique=True)
    description = models.CharField(max_length=254, verbose_name='description')
    price = models.FloatField(verbose_name='Price')
    amount = models.IntegerField(verbose_name='amount of product')

    type_id = models.ForeignKey(Type, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

    @staticmethod
    def is_valid(product_id):
        return Product.objects.filter(id=product_id).exists()


# ___________________________Product_________________________________________________________

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, verbose_name='Product id')

    def upload_to(self, filename):
        """
        :param filename:
        :return: image path
        """
        return f'product/{self.product.name}/{filename}'

    image = ResizedImageField(upload_to=upload_to, verbose_name='photo path')

    def __str__(self):
        return f'Category/{self.product.type_id.name}{self.product.name}/{self.image.verbose_name}'
