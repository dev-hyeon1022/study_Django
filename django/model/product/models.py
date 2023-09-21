from django.db import models

from member.models import Member
from model.models import Period


# Create your models here.
class Product(Period):
    product_name = models.CharField(max_length=50, blank=False, null=False)
    product_price = models.IntegerField(null=False, default=0)
    product_stock = models.IntegerField(null=False, default=0)

    class Meta:
        db_table = "tbl_product"

    def __str__(self):
        return self.product_name