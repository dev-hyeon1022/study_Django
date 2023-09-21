from django.db import models

from view.models import Period


# Create your models here.
class Member(Period):
    member_email = models.CharField(max_length=200, unique=True, null=False, blank=False)
    member_password = models.CharField(max_length=200, null=False, blank=False)
    member_name = models.CharField(max_length=200, null=False, blank=False)
    member_age = models.PositiveSmallIntegerField(default=0)
    member_birth = models.DateField(null=False, blank=False)

    class Meta:
        db_table = "tbl_member"


