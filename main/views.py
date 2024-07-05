from django.shortcuts import render
from . import models

def index(request):
    news = models.News1.objects.all()
    news2 = models.News2.objects.all()
    news3 = models.News3.objects.all()

    context = {
        'news':news,
        'news2':news2,
        'news3':news3
    }

    return render(request,'index.html',context)
