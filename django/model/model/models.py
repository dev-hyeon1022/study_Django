from django.db import models


class Period(models.Model):
    create_date = models.DateTimeField(null=False, auto_now_add=True)
    update_date = models.DateTimeField(null=False, auto_now=True)

    class Meta:
        abstract = True
