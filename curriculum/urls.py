from django.urls import path
from . import upload, play

urlpatterns = [
    path('upload/', upload.upload_view, name='upload'),
    path('play/', play.paly_view, name='play'),
]
