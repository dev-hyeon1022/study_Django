from django.test import TestCase

from cart.models import Cart
from member.models import Member
from product.models import Product


# Create your tests here.
class ProductTest(TestCase):
    Product.objects.create(product_name='볼펜', product_price='800', product_stock='100')
    pass