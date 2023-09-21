from django.urls import path
from django.views.generic import TemplateView

from user.views import LoginView, MyPageView

app_name = 'user'

urlpatterns = [
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('mypage/', MyPageView.as_view(), name='mypage'),
    path('oauth/redirect/', LoginView.as_view(), name='redirect')
]