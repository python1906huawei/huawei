from django.conf.urls import url

from App import views

urlpatterns = [
    # 首页
    url(r'^$', views.IndexView.as_view(), name='index'),
    # 注册
    url(r'^register/$', views.RegisterView.as_view(),name='register'),
    # 顶部
    url(r'^top/$', views.top,name='top'),
    # 底部
    url(r'^foot/$',views.foot,name='foot'),

]
