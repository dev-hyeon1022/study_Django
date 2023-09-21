from django.db import models

from member.models import Member
from post.models import Post


# Create your models here.
class Reply(models.Model):
    post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, null=False, on_delete=models.CASCADE)
    reply_content = models.CharField(null=False, blank=False, max_length=300)

    class Meta:
        db_table = "tbl_reply"
        ordering = ["-id"]
