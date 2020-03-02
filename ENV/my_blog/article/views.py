#现在你的views.py应该是这样
from django.shortcuts import render
from django.http import HttpResponse,Http404
from article.models import Article
from datetime import datetime


# Create your views here.
def home_view(request):
    post_list = Article.objects.all()  #获取全部的Article对象
    return render(request, 'home.html', {'post_list' : post_list})


def detail_view(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post})

def hugo_view(request):
 	post_list = Article.objects.all()  #获取全部的Article对象
 	return render(request,'hugo.html',{'post_list' : post_list})