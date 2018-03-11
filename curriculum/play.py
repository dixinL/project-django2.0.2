from django.shortcuts import render
from django.http import FileResponse
import os

# 暂时的测试播放文件夹，迁移时要注意更改
PLAY_PATH = '/Users/wanghc/Desktop/play_list'


# 渲染播放界面，播放器靠ajax实现
def play_view(request):
    return render(request, 'curriculum/play.html')


# AJAX对象，用来返回一个播放器对象，具体的视频文件需要继续调用其他url
# 参数：name：用来生成一个src（视频源url），传给play_file_obj（src）
def play_ajax_obj(request, name):
    # src = os.path.join("play_file_obj/", name)
    # name = name + '.mp4'
    # file_path = os.path.join(PLAY_PATH, name)
    # response = FileResponse(open(file, 'rb'), content_type='video/mp4')
    return render(request, 'curriculum/play_ajax_obj.html', {
        'name': name,
    })


# 用来返回一个文件对象，用来填充视频内容
def play_file_obj(request, src):
    src = os.path.join(PLAY_PATH, src)+'.mp4'
    response = FileResponse(open(src, 'rb'), content_type='video/mp4')
    return response
