from django.urls import path, include
from .views import PostList, PostDetail

app_name = 'news'

urlpatterns = [
    path('news/', PostList.as_view(), name='all_posts'),
    path('news/<int:pk>', PostDetail.as_view(), name='postDetail'),
]