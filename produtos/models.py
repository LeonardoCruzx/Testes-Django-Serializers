from django.db import models

from cloudinary.models import CloudinaryField
# Create your models here.
class CategoriaModel(models.Model):
    name = models.CharField(
        verbose_name="nome",
        max_length=30,
        null=False,
        blank=False,
        unique=True
    )
    def __str__(self):
        return self.nome

class ProdutoModel(models.Model):
    name = models.CharField(
        verbose_name="nome",
        max_length=30,
        null=False,
        blank=False
    )
    category = models.ForeignKey(
        "CategoriaModel",
        verbose_name="categorias",
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    price = models.FloatField(
        verbose_name="preco",
        null=False,
        blank=False
    )
    description = models.CharField(
        verbose_name="descrição",
        max_length=200,
        null=False,
        blank=False
    )
    product_picture = CloudinaryField(
        "product_pictures/product_picture",
        default="product_pictures/default_product_picture",
        null=True
    )

    def __str__(self):
        return self.nome



