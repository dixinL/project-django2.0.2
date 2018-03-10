from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# 课程模型
# TODO：label：一个为上传文件加入的标签选项、用来搜索。最好用下拉菜单形式
class CurriculumInfo(models.Model):
    date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='curriculum_info')
    file_name = models.CharField(max_length=50)
    path = models.FilePathField()
    series = models.CharField(verbose_name='系列', max_length=50)
    price = models.IntegerField(verbose_name='价格')
    grade = models.CharField(verbose_name='年级', max_length=50)

    class Meta:
        # permissions 会在数据库创建属于该模块的一个自定义权限
        permissions = (
            ('upload_file', '可以上传文件'),
        )


