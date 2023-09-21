from django.db import models

from model.models import Period


# python manage.py startapp [애플리케이션명]
# python manage.py makemigrations : 테이블 반영 준비
# python manage.py migrate : 테이블 반영

# python manage.py migrate --fake [앱이름] zero : 마이그레이션 삭제


# Create your models here.
class Member(Period):
    member_email = models.CharField(blank=False, null=False, max_length=50, unique=True)
    member_password = models.CharField(blank=False, null=False, max_length=50)
    member_name = models.TextField(null=False, blank=True)
    member_age = models.PositiveSmallIntegerField(null=False, default=0)
    member_status = models.BooleanField(null=False, default=True)

    class Meta:
        # 테이블명 작성
        db_table = 'tbl_member'
        ordering = ['-id']

    def __str__(self):
        return self.member_email
