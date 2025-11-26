from django.db import models

class Products(models.Model):
  product_name = models.CharField(max_length=200, verbose_name="Наименование товара")
  about_item = models.TextField(verbose_name="Подробнее о товаре")
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name = 'товар'
    verbose_name_plural = 'товары'
    db_table = 'products'

  def __str__(self):
    return self.product_name
  