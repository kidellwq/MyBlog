from django.shortcuts import render


def index(request):
    return render(request, 'blog/index.html', {
        'title': '欢迎光临我的博客',
        'welcome': '欢迎访问我的博客首页',
    })
