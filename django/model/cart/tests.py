from django.db.models import Count, Subquery, Max, Sum
from django.test import TestCase

from cart.models import Cart
from member.models import Member
from product.models import Product


# Create your tests here.
class CartTest(TestCase):
    # member = Member.objects.get(id=11)
    # product = Product.objects.get(id=2)
    # Cart(product_count=3, member=member, product=product).save()
    # products = list(Product.objects.all())
    #
    # for product in products:
    #     Cart(product_count=3, member=member, product=product).save()

    # 각 회원의 장바구니 목록 조회
    # print(Cart.objects.values('member__member_name', 'product__product_name', 'product_count').distinct())

    # 전체 회원의 장바구니에서 가장 많이 담긴 상품 정보 조회
    # print(
    #     Product.objects.get(id=
    #     Cart.objects.values('product_id')
    #     .annotate(count=Count('member_id')).filter(count=Cart.objects.values('product_id')
    #     .annotate(count=Count('member_id')).aggregate(max=Max('count'))['max'])[0]['product_id']
    # ))

    # 장바구니에 담긴 상품의 전체 개수가 가장 많은 회원의 정보 조회
    # print(
    #     Cart.objects.values('member_id', 'member__member_name').filter(product_id=
    #     Cart.objects.values('product_id').annotate(count=Sum('product_count')).filter(count=
    #     Cart.objects.values('product_id').annotate(count=Sum('product_count')).aggregate(max=Max('count'))['max'])[0]['product_id'])
    # )

    # 장바구니에 아무것도 담지 않은 회원의 정보 조회
    # print(Member.objects.exclude(id__in=Cart.objects.values('member_id')))

    # 장바구니에 한 번이라도 담긴 상품 목록 조회
    # print(Product.objects.filter(id__in=Cart.objects.values('product_id').distinct()))
    pass

