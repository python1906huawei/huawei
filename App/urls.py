from django.conf.urls import url

from App import views

urlpatterns = [
    # 首页
    url(r'^$', views.index, name='index'),
    # 注册
    url(r'^register/$', views.register,name='register'),


]
