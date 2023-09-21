from django.db import transaction
from django.db.models import F, Sum
from django.test import TestCase
from datetime import date

from cart.models import Cart
from member.models import Member
from pay.models import Sequence, Pay


# Create your tests here.
class PayTest(TestCase):
    # 트랜잭션 영역을 생성하면, 원하는 지점부터 하나의 트랜잭션으로 묶어주며,
    # 로직에 맞게 커밋 혹은 롤백을 작성할 수 있다.
    # with transaction.atomic():
        # pid = transaction.savepoint()
        # Sequence.objects.init_sequence(date.today())
        # print(Sequence.objects.get_next_sequence(date.today()))
        # transaction.savepoint_commit(pid)
        # transaction.savepoint_rollback(pid)

    with transaction.atomic():
        # carts = Member.objects.get(id=11).cart_set\
        #     .annotate(
        #     total_price=F('product__product_price') * F('product_count'),
        #     product_price=F('product__product_price')
        # )\
        #     .values('product_id', 'product_count', 'product_price', 'member_id', 'total_price')
        # print(carts)

        # 첫 주문일 때에만 시퀀스 새롭게 생성
        Sequence.objects.init_sequence(date.today())
        # 로그인 된 회원의 장바구니 목록
        carts = Member.objects.get(id=10).cart_set.all()

        # 장바구니에 담은 각 상품 별 총 가격
        cart_with_total_prices = carts.annotate(
            total_price=F('product__product_price') * F('product_count'))\
            .values('id', 'total_price')

        # 현재 결제에 대한 시퀀스는 이전 시퀀스 + 1, 즉, 다음 시퀀스 가져오기
        Sequence.objects.get_next_sequence(date.today())
        # 회원이 장바구니에 담은 상품을 cart에 하나씩 담는다.
        for cart in list(carts):
            for cart_with_total_price in cart_with_total_prices:
                # 그 상품의 장바구니 번호와, 총 가격이 있는 장바구니의 번호가 같다면
                if cart.id == cart_with_total_price['id']:
                    # 결제 내역에 INSERT!
                    Pay.objects.create(
                        member=cart.member,
                        product=cart.product,
                        product_count=cart.product_count,
                        product_total_price=cart_with_total_price['total_price'],
                        sequence=Sequence.objects.get_sequence(date.today()),
                        create_date=date.today()
                    )

        # 총 결제 금액
        print(Pay.objects.values('sequence', 'create_date')
              .annotate(total_price=Sum('product_total_price')))
