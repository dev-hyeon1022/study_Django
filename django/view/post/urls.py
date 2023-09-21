from django.urls import path

from post.views import PostWriteView, PostDetailView, PostUpdateView, PostListView, PostDeleteView

app_name = 'post'

urlpatterns = [
    # path('list/<int:page>/<int:size>/', PostListView.as_view(), name='list'),
    path('list/<int:page>/', PostListView.as_view(), name='list'),
    path('list/', PostListView.as_view(), name='list_init'),
    path('write/<int:page>/', PostWriteView.as_view(), name='write'),
    path('detail/<int:post_id>/<int:page>/', PostDetailView.as_view(), name='detail'),
    path('update/<int:post_id>/<int:page>/', PostUpdateView.as_view(), name='update'),
    path('delete/<int:post_id>/', PostDeleteView.as_view(), name='delete')
]
