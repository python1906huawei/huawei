from django.conf.urls import url

from App import views

urlpatterns = [
    # 首页
    url(r'^$', views.IndexView.as_view(), name='index'),
    # 注册
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    # 顶部+底部  通用继承
    url(r'^top/$', views.TopView.as_view(), name='top'),

    # 商品详情
    url(r'^detail/$', views.DetailView.as_view(), name='detail'),

    # 登录
    url(r'^login/$', views.LoginHuaweiView.as_view(), name='login-huawei')

]
