from django.shortcuts import render, HttpResponse
from django.views.generic import ListView


# Create your views here.

# 首页
class IndexView(ListView):
    template_name = 'index_new.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'index_new.html')

    def post(self, request, *args, **kwargs):
        return render(request, 'index_new.html')


# 注册
class RegisterView(ListView):
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'register.html')

    def post(self, request, *args, **kwargs):
        return render(request, 'register.html')


# 顶部+底部
class TopView(ListView):
    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'base.html')

    def post(self, request, *args, **kwargs):
        return render(request, 'base.html')


# 商品详情
class DetailView(ListView):
    template_name = 'detail_1.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'detail_1.html')

    def post(self, request, *args, **kwargs):
        return render(request, 'detail_1.html')


# 登录华为
class LoginHuaweiView(ListView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        return render(request, 'login.html')
