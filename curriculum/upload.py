from django.shortcuts import render, redirect
from .forms import UploadForm
import datetime
import os
# Create your views here.


UPLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'upload_dir')


def handle_uploaded_file(f, file_name, series):
    form = UploadForm()
    path = os.path.join(UPLOAD_DIR, series)
    print(path)
    if not os.path.exists(path):  # 判断是否存在文件或目录path
        os.makedirs(path)
    with open(os.path.join(path, file_name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload_view(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        # file = request.FILES.get('file')  # 获取上传的文件，如果没有文件，则默认为None
        # if file is None:
        #     err = '请上传正确的文件'
        #     print(err)
        #     return redirect('upload')
        if form.is_valid():
            print('isvalid')
            date = datetime.date.today()
            owner = request.user.username
            series = form.cleaned_data['series']
            file_name = series + owner + str(date) + '.mp4'
            handle_uploaded_file(request.FILES['file'], file_name=file_name, series=series)
            print('handle')
        else:
            return render(request, 'curriculum/upload.html', {'form': form})
        return redirect('/')
    else:
        form = UploadForm()
        return render(request, 'curriculum/upload.html', {'form': form})



