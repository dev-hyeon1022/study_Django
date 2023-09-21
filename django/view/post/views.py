import math

from django.conf import settings
from django.shortcuts import render, redirect
from django.views import View

from member.models import Member
from post.models import Post, PostFile


# Create your views here.

# 게시글 목록
class PostListView(View):
    def get(self, request, page=1):
        size = 5
        offset = (page - 1) * size
        limit = page * size
        total = Post.objects.all().count()
        pageCount = 5
        endPage = math.ceil(page / pageCount) * pageCount
        startPage = endPage - pageCount + 1
        realEnd = math.ceil(total / size)
        endPage = realEnd if endPage > realEnd else endPage
        pageUnit = (page - 1 // 5) + 1
        if endPage == 0:
            endPage = 1

        context = {
            'posts': list(Post.objects.all())[offset:limit],
            'startPage': startPage,
            'endPage': endPage,
            'page': page,
            'realEnd': realEnd,
            'member_name': Member.objects.get(member_email=request.session['member_email']).member_name,
        }
        return render(request, 'post/list.html', context)


# 게시글 작성
class PostWriteView(View):
    def get(self, request, page):
        return render(request, "post/write.html", {'member_name': Member.objects.get(member_email=request.session['member_email']).member_name, 'page': page})

    def post(self, request, page=1):
        datas = request.POST
        files = request.FILES

        datas = {
            'member_id': Member.objects.get(member_email=request.session['member_email']).id,
            'post_title': datas['post_title'],
            'post_content': datas['post_content']
        }

        post = Post.objects.create(**datas)
        # 태그 한 개 multiple
        for file in files.getlist('file1'):
            PostFile.objects.create(post=post, image=file)

        # 태그 여러 개
        # for key in files:
        #     PostFile.objects.create(post=post, image=files[key])
        # PostFile.objects.create(post=post, image=files['file'])
        return redirect(post.get_absolute_url(page))


# 게시글 조회
class PostDetailView(View):
    def get(self, request, post_id, page):
        print(post_id)
        post = Post.objects.get(id=post_id)
        context = {
            'post': post,
            'post_files': list(post.postfile_set.all()),
            'page': page
        }
        return render(request, "post/detail.html", context)


# 게시글 수정
class PostUpdateView(View):
    def get(self, request, post_id, page):
        print(post_id)
        post = Post.objects.get(id=post_id)
        context = {'post': post, 'member_name': '한동석', 'page': page}
        # render(request, to, context): 바로 html 화면으로 이동
        return render(request, "post/update.html", context)

    def post(self, request, post_id, page):
        datas = request.POST
        datas = {
            'post_title': datas['post_title'],
            'post_content': datas['post_content']
        }
        Post.objects.filter(id=post_id).update(**datas)
        # redirect(to): URL로 이동하여 다른 View에서 render()로 html 화면 이동
        return redirect(Post.objects.get(id=post_id).get_absolute_url(page))


# 게시글 삭제
class PostDeleteView(View):
    def get(self, request, post_id):
        Post.objects.get(id=post_id).delete()
        return redirect('post:list_init')
