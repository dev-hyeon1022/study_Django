import os
import django
from django.db.models import Q, F, Count, Sum, Max, Min
from django.test import TestCase

from member.models import Member

# Create your tests here.

os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
django.setup()


class MemberTest(TestCase):
     # 클래스 내부에 코드를 작성하면, 커밋 된다.
     # 하지만 메소드 내에서 코드를 작성하면, 롤백 된다.

    # ======================================
    # bulk_create
    # ======================================
    # Member.objects.bulk_create([
    #     Member(member_email='test1@gmail.com', member_password='1234', member_age=30, member_name='한동석',
    #            member_status=True),
    #     Member(member_email='test2@naver.com', member_password='4564', member_age=20, member_name='홍길동',
    #            member_status=True),
    #     Member(member_email='test3@naver.com', member_password='7897', member_age=40, member_name='짱구',
    #            member_status=True),
    #     Member(member_email='test4@google.com', member_password='5555', member_age=50, member_name='철수',
    #            member_status=True),
    #     Member(member_email='test5@nate.com', member_password='9638', member_age=20, member_name='유리',
    #            member_status=True),
    # ])

    # ======================================
    # save
    # ======================================
    # member = Member.objects.create(
    #     member_email='test@nate.com',
    #     member_password='1234',
    #     member_age=20,
    #     member_name='한동석',
    #     member_status=True)

    # member = Member(member_email='test@nate.com',
    #                 member_password='1234',
    #                 member_age=20,
    #                 member_name='한동석',
    #                 member_status=True)
    # member.save()
    # # select id, member_email, member_password, member_name, member_age, member_status from tbl_member
    # print(Member.objects.get(id=1))

    # ======================================
    # bulk_create (자동 롤백)
    # ======================================
    # def test_bulk_create(self):
    #     # print(Member.objects.all().query)
    #     # print(list(Member.objects.all()))
    #     print(Member.objects.values('member_email').query)
    #     print(Member.objects.values('member_email'))
    #     print(Member.objects.values_list('member_email'))
    #
    #     for i in Member.objects.values_list('member_email'):
    #         print(i)

    # ======================================
    # get_or_create
    # ======================================
    # Member.objects.create(member_email='tedhan1204@gmail.com', member_name='한동석', member_password='1234',
    #                           member_age=20, member_status=False)
    #
    # member = Member.objects.get_or_create(member_email='tedhan1204@gmail.com', member_name='한동석', member_password='1234',
    #                                           member_age=20, member_status=False)
    # print(member)

    # ======================================
    # filter
    # ======================================
    # print(Member.objects.filter(member_name='짱구'))
    # print(Member.objects.filter(member_name__contains='유'))
    # print(Member.objects.filter(member_email__endswith='com'))
    # print(Member.objects.filter(member_email__in=['test1@nate.com', 'test9@gmail.com']))
    # print(Member.objects.filter(member_email__icontains='T').count())

    # ======================================
    # exclude()
    # ======================================
    # print(Member.objects.exclude(member_email='test3@naver.com'))
    # print(Member.objects.exclude(member_email__in=['test1@gmail.com', 'test2@naver.com']))

    # ======================================
    # AND, OR
    # ======================================
    # print(Member.objects.filter(member_email__contains='test')
    #       & Member.objects.filter(member_age__lte=30))
    # print(Member.objects.filter(member_email__contains='test')
    #       | Member.objects.filter(member_age__lte=30))
    # print(Member.objects.filter(member_email__contains='test', member_age__lte=30))
    #
    # condition1 = Q(member_email__contains='test')
    # condition2 = Q(member_age__lte=30)
    #
    # print(Member.objects.filter(condition1 | condition2))

    # ======================================
    # order_by()
    # ======================================
    # print(Member.objects.all().order_by('member_name'))
    # print(Member.objects.all().order_by('-id'))

    # Meta 클래스에서 ordering = ['-id']로 설정
    # print(Member.objects.all())

    # ======================================
    # slicing
    # ======================================
    # [start:end:step]
    # slicing에서 step을 사용하면 전체 조회 쿼리가 발생된 후 list로 변환되어 slicing된다.
    # Django ORM은 기본 LAZY방식이기 때문에 처음부터 전체 쿼리가 발생하지 않는다.
    # 하지만 step을 사용하면 처음부터 전체 쿼리가 발생하기 때문에 성능면에서는 step을 쓰지 않는 것이 좋다.

    # print(Member.objects.all()[1:].query)
    # print(Member.objects.all()[0:4:2])

    # ======================================
    # annotate()
    # ======================================
    # values()를 사용하고 annotate()를 사용하면 추가 연산에 대한 결과 컬럼을 만들 수 있고
    # annotate()를 사용하고 values를 사용하면 기존 컬럼을 다른 이름으로 변경할 수 있다.
    # print(Member.objects.annotate(email=F('member_email')).values('email', 'member_name'))
    # print(Member.objects.annotate(age=F('member_age') - 1).values('member_name', 'age'))
    # print(Member.objects.values('member_age').annotate(count=Count('id')))
    # 회원의 이용 상태 별 명 수
    # for i in list(Member.objects.values('member_status').annotate(member_count=Count('id'))):
    #     print('이용가능' if i['member_status'] else '이용불가', f'{i["member_count"]}명')

    # ======================================
    # aggregate
    # ======================================
    # print(Member.objects.aggregate(total_count=Sum('id'))['total_count'] + 10)
    # for i in list(Member.objects.annotate(name=F('member_name'))):
    #     print(i.name)

    # annotate()는 QuerySet 객체로 리턴하기 때문에 뒤에 이어서 filter() 등을 사용할 수 있으며,
    # 개별 행 처리이므로 전체 집계가 불가능하다.
    # aggregate()는 전체를 대상으로 집계하며, 뒤에 이어서 다른 절을 사용할 수 없다.
    # print(Member.objects.aggregate(max_age=Max('member_age')))
    # print(Member.objects.aggregate(min_age=Min('member_age')))
    # print(Member.objects.aggregate(max_age=Max('member_age'), min_age=Min('member_age')))

    # ======================================
    # update()
    # ======================================
    # Member.objects.filter(id=8).update(member_email='updated@test.com')
    # print(Member.objects.all())

    # ======================================
    # save() for update
    # ======================================

    member = Member.objects.get(id=10)
    member.member_name = '맹구'
    member.save()
    pass
