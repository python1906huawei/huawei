from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# 用户表
from db.base_model import BaseModel


class User(AbstractUser, BaseModel):
    create_time = models.DateTimeField(blank=True, null=True, verbose_name='创建时间')

    class Meta:
        managed = True
        db_table = 'user'


# 用户信息表
class Userinfo(BaseModel):
    realname = models.CharField(max_length=64, blank=True)

    mobile = models.CharField(max_length=20)

    email = models.CharField(max_length=200, blank=True, null=True)
    # 头像
    portrait = models.FileField(max_length=100, blank=True, null=True, upload_to='pic')

    birthday = models.DateField(blank=True, null=True)
    # 国籍
    nationality = models.CharField(max_length=20, blank=True, null=True)
    # 省
    province = models.CharField(max_length=20, blank=True, null=True)
    # 市
    city = models.CharField(max_length=20, blank=True, null=True)
    # 区
    country = models.CharField(max_length=20, blank=True, null=True)
    # 详细信息
    detail = models.CharField(max_length=200, blank=True, null=True)

    user_id = models.ForeignKey(User, models.CASCADE, related_name='info', verbose_name='所属账户')

    class Meta:
        managed = True
        db_table = 'userinfo'
