from django.urls import path
from django.views.generic import TemplateView

from member.views import MemberJoinView, MemberLoginView, MemberLogoutView

app_name = 'member'



urlpatterns = [
    # path('join/', TemplateView.as_view(template_name='member/join.html'))
    path('join/', MemberJoinView.as_view(), name='join'),
    path('login/', MemberLoginView.as_view(), name='login'),
    path('logout/', MemberLogoutView.as_view(), name='logout'),
    path('success/', TemplateView.as_view(template_name='member/success.html'), name='success'),
    path('fail/', TemplateView.as_view(template_name='member/fail.html'), name='fail'),
]
