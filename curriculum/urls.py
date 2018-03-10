from django.urls import path, include
from . import upload, play

urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')), django自带的用户表单
    path('upload/', upload.upload_view, name='upload'),
    path('play/', play.play_view, name='play'),
]
