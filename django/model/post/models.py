from django.db import models

from member.models import Member
from model.models import Period


# Create your models here.
class Post(Period):
    post_title = models.CharField(blank=False, null=False, max_length=50)
    post_content = models.TextField(blank=False, null=False)
    member = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = "tbl_post"

    def __str__(self):
        return self.post_title


class PostFile(Period):
    post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/%Y/%m/%d')

    class Meta:
        db_table = "tbl_post_file"
