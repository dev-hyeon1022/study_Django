import random

from django.db.models import F
from django.test import TestCase

from member.models import Member
from post.models import Post
from reply.models import Reply


# Create your tests here.
class PostTest(TestCase):

    # members = list(Member.objects.all())
    # posts = []
    #
    # for i in range(0, 97):
    #     idx = random.randint(0, len(members) - 1)
    #     posts.append(Post(post_title=f'테스트 제목{i + 1}', post_content=f'테스트 내용{i + 1}', member=members[idx]))
    #
    # Post.objects.bulk_create(posts)

    # 9번 회원의 게시글

    # Post의 정보만 가져온다.
    # print(Post.objects.filter(member=Member.objects.get(id=9)).query)
    # print(Post.objects.filter(member=Member.objects.get(id=9)).count())
    # print(Post.objects.filter(member_id=9).values('id', 'post_title', 'post_content', 'member__member_name'))
    # print(Post.objects.filter(member_id=9).annotate(member_name=F('member__member_name'))
    #       .values('id', 'post_title', 'post_content', 'member_name'))
    
    # 정방향 참조
    # print(Post.objects.get(id=21).member.member_name)
    
    # 역방향 참조(_set)
    # Post.objects.filter(member=12).all()
    # posts = Member.objects.get(id=12).post_set.all()
    # print(posts)
    # print(posts.query)

    # 직접 select_related()를 사용하여 JOIN을 하지 않고
    # 필요한 필드를 아래와 같이 사용할 수 있다.
    # [접근할 객체명]__[필드명] : 자동으로 JOIN된다.


    # 정방향 참조 시 해당 필드의 null 상태에 따라 내부와 외부 조인이 나뉜다.
    # null=False: INNER JOIN
    # null=True: OUTER JOIN

    # 역방향 참조 시 무조건 외부 조인으로 실행된다.

    # 예시
    # A필드에 b가 있다.
    # a로 b필드에 접근하면 정방향이고, b의 null 상태에 따라 내부 또는 외부조인이 실행된다.
    # b로 a필드에 접근하면 역방향이고, b의 모든 정보가 나와야하므로 항상 외부조인이 실행된다.

    # print(Post.objects.select_related('member').query)
    # print(Post.objects.values('member__member_name').query)
    # print(Member.objects.values('post__post_title').query)

    # 게시글 전체 목록
    # print(Post.objects.all())

    # 게시글 1개 조회
    # post = Post.objects.get(id=55)

    # 해당 게시글의 댓글 목록 조회
    # print(Reply.objects.filter(post=post, reply_depth=1))
    # print(post.reply_set.all())

    # 게시글과 게시글 작성자 정보 한 번에 조회
    # print(Post.objects.values('post_title', 'post_content', 'member__member_name'))
    # print(Post.objects.annotate(member_name=F('member__member_name'))
    #     .values('post_title', 'post_content', 'member_name'))
    pass














