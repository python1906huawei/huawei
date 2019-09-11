# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models




class Category(models.Model):
    cid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=60)
    parentid = models.IntegerField()
    compere = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    orderby = models.IntegerField(blank=True, null=True)
    namestyle = models.CharField(max_length=10, blank=True, null=True)
    logo = models.CharField(max_length=200, blank=True, null=True)
    themenum = models.IntegerField(blank=True, null=True)
    replynum = models.IntegerField(blank=True, null=True)
    lastpost = models.CharField(max_length=600, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bbs_category'


class Friendlink(models.Model):
    site = models.CharField(max_length=100)
    url = models.CharField(max_length=200, blank=True, null=True)
    logo = models.CharField(max_length=300, blank=True, null=True)
    orderby = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bbs_friendlink'


class Lockip(models.Model):
    ip = models.CharField(max_length=20)
    starttime = models.DateTimeField(blank=True, null=True)
    endtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bbs_lockip'


class Order(models.Model):
    money = models.IntegerField()
    paytime = models.DateTimeField(blank=True, null=True)
    tid = models.ForeignKey('Posts', models.DO_NOTHING, db_column='tid', blank=True, null=True)
    uid = models.ForeignKey('BbsUser', models.DO_NOTHING, db_column='uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bbs_order'


class Posts(models.Model):
    title = models.CharField(max_length=600)
    content = models.TextField(blank=True, null=True)
    replies = models.IntegerField()
    hits = models.IntegerField()
    istop = models.IntegerField()
    iselite = models.IntegerField()
    ishot = models.IntegerField()
    price = models.IntegerField()
    isdel = models.SmallIntegerField()
    publishtime = models.DateTimeField(blank=True, null=True)
    isdisadle = models.SmallIntegerField(blank=True, null=True)
    cid = models.ForeignKey(Category, models.DO_NOTHING, db_column='cid', blank=True, null=True)
    uid = models.ForeignKey('BbsUser', models.DO_NOTHING, db_column='uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bbs_posts'


class BbsReply(models.Model):
    rid = models.AutoField(primary_key=True)
    content = models.CharField(max_length=1000, blank=True, null=True)
    istop = models.IntegerField(blank=True, null=True)
    isdel = models.SmallIntegerField(blank=True, null=True)
    isblock = models.SmallIntegerField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)
    isdisable = models.SmallIntegerField(blank=True, null=True)
    tid = models.ForeignKey(Posts, models.DO_NOTHING, db_column='tid', blank=True, null=True)
    uid = models.ForeignKey('BbsUser', models.DO_NOTHING, db_column='uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bbs_reply'


class Siteinfo(models.Model):
    sitename = models.CharField(max_length=100, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    reference = models.CharField(max_length=200, blank=True, null=True)
    isclose = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bbs_siteinfo'


class User(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    uid = models.AutoField(primary_key=True)
    portrait = models.CharField(max_length=100, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    usertype = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    autologin = models.IntegerField(blank=True, null=True)
    regtime = models.DateTimeField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bbs_user'



class Userdetail(models.Model):
    birthday = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    qq = models.CharField(max_length=15, blank=True, null=True)
    signature = models.CharField(max_length=200, blank=True, null=True)
    quesstion = models.CharField(max_length=100, blank=True, null=True)
    answer = models.CharField(max_length=200, blank=True, null=True)
    grade = models.CharField(max_length=100, blank=True, null=True)
    uid = models.ForeignKey(User, models.DO_NOTHING, db_column='uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bbs_userdetail'
