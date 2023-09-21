from django.db.models import F, Subquery
from django.test import TestCase

from member.models import Member
from post.models import Post
from reply.models import Reply


# Create your tests here.
class ReplyTest(TestCase):
    member1 = Member.objects.get(id=12)
    member2 = Member.objects.get(id=9)
    # post1 = Post.objects.get(id=54)
    # post2 = Post.objects.get(id=55)

    # Reply.objects.bulk_create([
    #     Reply(reply_content='테스트 댓글1', reply_depth=1, post=post1, member=member1),
    #     Reply(reply_content='테스트 댓글2', reply_depth=1, post=post2, member=member1),
    #     Reply(reply_content='테스트 댓글3', reply_depth=1, post=post1, member=member1),
    #     Reply(reply_content='테스트 댓글4', reply_depth=1, post=post2, member=member2)
    # ])
    # reply = Reply.objects.get(id=3)
    # re_reply = Reply(reply_content='테스트 대댓글3', reply_depth=2, reply_group_id=reply.id, post=reply.post, member=member2)
    # re_reply.save()
    #
    # reply = Reply.objects.get(id=4)
    # re_reply = Reply(reply_content='테스트 대댓글4', reply_depth=2, reply_group_id=reply.id, post=reply.post, member=member1)
    # re_reply.save()

    # 게시글 상세보기 (작성자 필요)
    print(Post.objects.annotate(member_name=F('member__member_name')).values('post_title', 'post_content', 'member_name'))

    # 댓글 목록 (게시글 제목, 작성자 필요)
    post = Post.objects.get(id=54)
    print(Reply.objects.filter(post=post, reply_group_id__isnull=True).annotate(
        member_name=F('member__member_name'),
        post_title=F('post__post_title')
    ).values('post_title', 'reply_content', 'member_name'));

    # 특정 댓글의 대댓글 목록 (댓글 내용, 작성자 필요)
    reply_id = Reply.objects.filter(id=3).values_list('id')[0][0]

    print(Reply.objects.filter(reply_depth=2, reply_group_id=reply_id).annotate(
        re_reply_content=F('reply_content'),
        original_reply_content=Subquery(Reply.objects.filter(id=reply_id).values('reply_content')),
        member_name=F('member__member_name')
    ).values('reply_group_id', 're_reply_content', 'original_reply_content', 'member_name'))
    pass

















