from django import forms


class UploadForm(forms.Form):
    grade = forms.CharField(label='年级')
    price = forms.IntegerField(label='价格')
    series = forms.CharField(label='系列')
    file = forms.FileField(label='请上传文件')


