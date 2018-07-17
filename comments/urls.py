from django.urls import path
from .views import post_comment

app_name = 'comments'

urlpatterns = [
    path('comment/post/<int:post_pk>', post_comment, name='post_comment'),
]