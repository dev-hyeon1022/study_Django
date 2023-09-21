from django.db.models import F
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from member.models import Member
from post.models import Post
from reply.models import Reply
from reply.serializers import ReplySerializer


# Create your views here.
class ReplyListAPI(APIView):
    def get(self, request, post_id):
        # print(dict(request.GET).get('page')[0])
        replies = Reply.objects.filter(post_id=post_id).annotate(member_name=F('member__member_name')).values('id', 'reply_content', 'member_name')
        # return Response(ReplySerializer(replies, many=True).data)
        return Response(replies)


class ReplyWriteAPI(APIView):
    def post(self, request):
        datas = request.data
        datas = {
            'post': Post.objects.get(id=datas.get('post_id')),
            'member': Member.objects.get(member_email=request.session['member_email']),
            # 'member': Member.objects.get(member_email='test@gmail.com'),
            'reply_content': datas.get('reply_content')
        }
        #
        Reply.objects.create(**datas)
        return Response('success')

class ReplyUpdateAPI(APIView):
    def post(self, request):
        datas = request.data

        Reply.objects.filter(id=datas['id']).update(reply_content=datas['reply_content'])
        return Response('success')

class ReplyDeleteAPI(APIView):
    def get(self, request, id):
        print(id)
        Reply.objects.get(id=id).delete()
        return Response('success')

    def post(self, request):
        datas = request.data
        Reply.objects.get(id=datas['id']).delete()
        return Response('success')














