from django.db import models

from member.models import Member
from model.models import Period
from post.models import Post


# Create your models here.
class Reply(Period):
    REPLY_STATUS = [
        ('Y', '일반 댓글'),
        ('N', '비밀 댓글')
    ]

    reply_content = models.TextField(blank=False, null=False)
    reply_status = models.CharField(max_length=1, blank=False, null=False, choices=REPLY_STATUS, default='Y')
    reply_group_id = models.IntegerField(null=True)
    reply_depth = models.PositiveSmallIntegerField(null=False)
    member = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL)
    post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_reply"

    def __str__(self):
        return self.reply_content
