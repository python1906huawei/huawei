from django.conf.urls import url

from App import views

urlpatterns = [
    # 首页
    url(r'^$', views.IndexView.as_view(), name='index'),
    # 注册
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    # 顶部+底部  通用继承
    url(r'^top/$', views.top, name='top'),

    # 商品详情
    url(r'^detail/$', views.detail, name='detail')

]
