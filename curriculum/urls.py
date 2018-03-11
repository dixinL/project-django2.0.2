from django.urls import path, include
from . import upload, play

urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')), django自带的用户表单
    path('upload/', upload.upload_view, name='upload'),
    path('play_file_obj/<slug:src>/', play.play_file_obj, name='play_file_obj'),
    path('play_ajax_obj/<slug:name>/', play.play_ajax_obj, name='play_ajax_obj'),
    path('play/', play.play_view, name='play'),
]
