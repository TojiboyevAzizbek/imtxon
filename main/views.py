from django.shortcuts import render
from . import models



def index(request):
    baner = models.Banner.objects.last()
    xizmatlar = models.Xizmatlar.objects.all()
    avtoservis_haqida = models.Avtoservis_haqida.objects.last()
    xodimlarimiz = models.Xodimlarimiz.objects.all()
    blog = models.Blog.objects.all()

    context = {
        'baner':baner,
        'xizmatlar':xizmatlar,
        'avtoservis_haqida':avtoservis_haqida,
        'xodimlarimiz':xodimlarimiz,
        'blog':blog
    }
    return render(request, 'index.html', context)



def avtoservis_haqida(request):
    avtoservis_haqida = models.Avtoservis_haqida.objects.last()
    context = {
        'avtoservis_haqida':avtoservis_haqida
    }
    return render(request, 'avtoservis_haqida.html',context)


def aloqa(request):

    if request.method == 'POST':
        try:
            models.Aloqa.objects.create(
                name=request.POST['name'],
                phone=request.POST['phone'],
                email=request.POST['email'],
                body=request.POST['message'],
                
            )
        except:
            ...
    return render(request, 'aloqa.html')

def xizmatlar(request):
    xizmatlar = models.Xizmatlar.objects.all()
    context = {
        'xizmatlar':xizmatlar
    }
    return render(request, 'xizmatlar.html',context)

def xodimlarimiz(request):
    xodimlarimiz = models.Xodimlarimiz.objects.all()
    context = {
        'xodimlarimiz':xodimlarimiz
    }
    return render(request, 'xodimlarimiz.html',context)

def blog(request):
    blog = models.Blog.objects.all()
    context = {
        'blog':blog
    }
    return render(request, 'blog.html',context)






