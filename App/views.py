from django.shortcuts import render, HttpResponse
from django.views.generic import ListView


# Create your views here.

# 首页
# def index(request):
#     return render(request, 'index_new.html')
class IndexView(ListView):
    template_name = 'index_new.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'index_new.html')

    def post(self, request, *args, **kwargs):
        return render(request, 'index_new.html')


# 注册
# def register(request):
#     return render(request, 'register.html')
# 注册pass
class RegisterView(ListView):
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'register.html')

    def post(self, request, *args, **kwargs):
        return render(request, 'register.html')


# 顶部  底部
def top(request):
    return render(request, 'head_foot/head.html')


def foot(request):
    return render(request, 'head_foot/foot.html')


# 商品详情
def detail(request):
    return render(request, 'detail_1.html')
