

from django.db import models, transaction
from django.db.models import Model

from cart.models import Cart
from member.models import Member
from model.models import Period
from product.models import Product

# 매일 새로운 시퀀스 생성
# 결제 완료 시 해당 날짜의 시퀀스 1 증가


# Create your models here.
class Pay(models.Model):
    # 해당 컬럼에 값을 INSERT할 때,
    # 화면에 보여지는 값과 DBMS에 들어갈 값을 따로 정하기 위해 사용한다.
    # [(DBMS, 화면), ...]
    PAY_STATUS = [
        ('Done', '결제 완료'),
        ('Cancel', '결제 취소')
    ]

    member = models.ForeignKey(Member, null=False, blank=False, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, blank=False, on_delete=models.SET_NULL)
    # 결제할 상품의 개수
    product_count = models.IntegerField(null=False, default=0)
    # 결제할 상품의 총 가격
    product_total_price = models.IntegerField(null=False, default=0)
    # 주문 번호
    sequence = models.BigIntegerField(null=False, default=0)
    # 결제 날짜
    create_date = models.DateField(null=False, blank=False, auto_now_add=True)
    # 결제 완료, 취소 구분
    pay_status = models.CharField(max_length=10, null=False, blank=False, default='Done', choices=PAY_STATUS)

    class Meta:
        db_table = "tbl_pay"
        ordering = ["-create_date"]


# models.Manager 상속받으면 내부의 메소드를 모델의 objects로 접근할 수 있다.
# 단, Manager에 있는 메소드 사용 후 체이닝을 할 때에는 또 다시 Manager의 메소드를 사용할 수는 없다.
class SequenceManager(models.Manager):
    # 매일 00시에 시퀀스가 한 개 생성된다.
    def init_sequence(self, date):
        # 오늘 첫 결제일 경우 해당 날짜가 Sequence에 없기 때문에
        # 이 때에만 create()해준다.
        if not self.filter(create_date=date).aexists():
            self.create(create_date=date)

        # 이미 시퀀스가 해당 날짜에 있으면,
        # if self.filter(create_date=date).exists():
        #     # 새롭게 만들지 말고, 기존 시퀀스 값을 0으로 초기화
        #     self.update(sequence=0)
        # else:
        #     # 전달받은 날짜의 시퀀스가 없기 때문에, 새롭게 만들기
        #     self.create(create_date=date)


    def get_sequence(self, date):
        # select_for_update(): 다른 트랜잭션에서 추가 전 조회가 발생할 수 있기 때문에, 이를 막아준다(Lock).
        # 대신 사용할 때에는 반드시 transaction.atomic() 영역 안에서 사용해야 한다.
        return self.filter(create_date=date).select_for_update(nowait=False, of=('self',)).first().sequence

    def update_sequence(self, sequence):
        # 전달받은 현재 시퀀스에 1을 더해준다.
        sequence = sequence + 1
        # 기존 시퀀스를 1 증가한 시퀀스로 UPDATE한다.
        self.update(sequence=sequence)
        return sequence

    def get_next_sequence(self, date):
        # 1 증가된 시퀀스를 리턴한다.
        return self.update_sequence(self.get_sequence(date))


class Sequence(models.Model):

    sequence = models.BigIntegerField(null=False, default=0)
    create_date = models.DateField(null=False, blank=False)

    # 알맞은 Manager()객체를 현재 모델의 objects에 포함시킨다.
    objects = SequenceManager()

    class Meta:
        db_table = 'seq_pay'


