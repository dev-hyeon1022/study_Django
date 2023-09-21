from django.db import models

from kakao.models import Period


# Create your models here.
class User(Period):
    user_email = models.CharField(blank=False, null=False, max_length=50, unique=True)
    user_name = models.CharField(null=False, max_length=50)
    user_test = models.CharField(null=False, max_length=50)

    class Meta:
        db_table = "tbl_user"