from django.shortcuts import render, redirect
from django.views import View

from member.models import Member


# Create your views here.
class MemberJoinView(View):

    def get(self, request, *args, **kwargs):
        # request와 실제 경로를 작성하여 이동한다.
        return render(request, 'member/join.html')

    def post(self, request, *args, **kwargs):
        token, member_email, member_password, member_name, member_age, member_birth = request.POST.values()
        Member.objects.create(member_email=member_email, member_password=member_password, member_name=member_name, member_age=member_age, member_birth=member_birth)
        # 이동할 urls 경로를 작성한다.
        # return redirect('/member/login')
        return redirect('member:login')


class MemberLoginView(View):
    def get(self, request):
        return render(request, 'member/login.html')

    def post(self, request):
        token, member_email, member_password = request.POST.values()
        if Member.objects.filter(member_email=member_email, member_password=member_password).exists():
            request.session['member_email'] = member_email
            return redirect('post:list_init')
            # return redirect('member:success')
        return redirect('member:login')
        # return redirect('member:fail')


class MemberLogoutView(View):
    def get(self, request):
        request.session.modified = True
        del request.session['member_email']
        print(request.session.get('member_email'))
        return redirect('member:login')














