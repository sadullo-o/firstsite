from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Yangiliklar, Info
import datetime

# Create your views here.

# frontend bilan boglaydigan kodlar shu yerda yoziladi

def asosiy(request):
    news = Yangiliklar.objects.all()
    context = {
        'news': news
    }

    return render(request, 'main/index.html', context)


def about(request):
    infos = Info.objects.all()

    context = {
        'info': infos
    }

    return render(request, 'main/about.html', context)


def tovarlar(request):
    contacts = Info.objects.all()

    contex = {
        'contacts': contacts
    }

    return render(request, 'main/tovarlar.html', contex)

def details(request, pk):
    context = {
        'meva': pk.title()
    }

    return render(request, 'main/mevalar/meva.html', context)


# def about(request):
#     hozir = datetime.datetime.now()
#     return HttpResponse(hozir)



# o'zingiz haqingizda sayt
# Main, MyProjects, About Me, Contact
