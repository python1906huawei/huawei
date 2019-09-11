from django.shortcuts import render, HttpResponse


# Create your views here.

# 首页
def index(request):
    return render(request,'index.html')

# 注册
def register(request):
    return render(request,'register.htm')