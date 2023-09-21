import requests
from django.shortcuts import render, redirect
from django.views import View

from user.models import User


# Create your views here.
class LoginView(View):
    def get(self, request):
        code = request.GET.get("code")
        query_string = '?Content-type: application/x-www-form-urlencoded;charset=utf-8&' \
                       'grant_type=authorization_code&' \
                       'client_id=58c7a23bf4f0c4c562ce6e0fea062614&' \
                       'redirect_uri=http://localhost:10000/user/oauth/redirect&' \
                       f'code={code}'
        response = requests.post(f'https://kauth.kakao.com/oauth/token{query_string}')
        access_token = response.json().get('access_token')
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
        }

        response = requests.post('https://kapi.kakao.com/v2/user/me', headers=headers)

        info = response.json().get('kakao_account')
        nickname = info.get('profile').get('nickname')
        thumbnail_image_url = info.get('profile').get('thumbnail_image_url')
        email = info.get('email')
        request.session['user_email'] = email
        request.session['thumbnail_image_url'] = thumbnail_image_url

        user = User.objects.filter(user_email=email).first()

        if not user:
            User.objects.create(user_email=email, user_name=nickname)

        return redirect('user:mypage')

class MyPageView(View):
    def get(self, request):
        user = User.objects.get(user_email=request.session['user_email'])
        context = {'user': user}
        return render(template_name='mypage.html', request=request, context=context)