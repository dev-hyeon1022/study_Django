from django.urls import path

from reply.views import ReplyListAPI, ReplyWriteAPI, ReplyUpdateAPI, ReplyDeleteAPI

app_name = 'reply'

urlpatterns = [
    path('list/<int:post_id>', ReplyListAPI.as_view(), name='list'),
    path('write/', ReplyWriteAPI.as_view(), name='write'),
    path('update/', ReplyUpdateAPI.as_view(), name='update'),
    path('delete/', ReplyDeleteAPI.as_view(), name='delete_post'),
    path('delete/<int:id>/', ReplyDeleteAPI.as_view(), name='delete_get'),
]