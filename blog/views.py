from django.shortcuts import render
from blog.models import Post,Bilettts

def post_list (request):
    post = Post.objects.filter(namber = 1)
    post_2 = Post.objects.filter(namber= 2)
    post_3 = Post.objects.filter(namber= 3)
    return render(request, 'blog/post_list.html', {'post': post,'post_2': post_2,'post_3': post_3})

def glavnii_list (request):
    return render (request, 'blog/glavnii_list.html')  # для работы главной страницы


def post_detaili (request, i_pk):
    pos = Post.objects.get(pk=i_pk)
    return render(request, 'blog/post_detaili.html', {'pos': pos})

def kruiz (request,i_pk):
    post = Bilettts.objects.all().filter(pk=i_pk)
    return render(request, 'blog/kruiz.html', {'post': post,})


def fail (request):
    return render (request, 'blog/fail.html')