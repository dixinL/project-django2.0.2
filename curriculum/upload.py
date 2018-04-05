from django.shortcuts import render, redirect
from .forms import UploadForm
from .models import CurriculumInfo
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required
import datetime
import os
# Create your views here.


UPLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'upload_dir')


# 分块写入文件 return 文件存储的位置
def handle_uploaded_file(f, file_name, series):
    path = os.path.join(UPLOAD_DIR, series)
    if not os.path.exists(path):  # 判断是否存在文件或目录path
        os.makedirs(path)
    with open(os.path.join(path, file_name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return path


# 检测用户是否有上传文件的权限，如果没有返回主页
@permission_required('curriculum.upload_file',login_url='/')
# 上传界面
def upload_view(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            number = str(form.cleaned_data['number'])
            date = datetime.date.today()
            owner = User.objects.get(username=request.user.username)
            series = form.cleaned_data['series']
            file_name = series + number +request.user.username + str(date) + '.mp4'
            path = handle_uploaded_file(request.FILES['file'], file_name=file_name, series=series)
            new_curriculum = CurriculumInfo(date=date,
                                            owner=owner,
                                            series=series,
                                            # TODO:判断上传文件类型后决定如何存储file_name
                                            file_name=file_name[:-4],
                                            path=path,
                                            grade=form.cleaned_data['grade'],
                                            price=form.cleaned_data['price'],
                                            number=form.cleaned_data['number']
                                            )
            new_curriculum.save()
        else:
            return render(request, 'curriculum/upload.html', {'form': form})
        return redirect('upload')
    else:
        form = UploadForm()
        return render(request, 'curriculum/upload.html', {'form': form})
