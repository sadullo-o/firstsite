from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

import datetime

# Create your views here.

# frontend bilan boglaydigan kodlar shu yerda yoziladi

def asosiy(request):

    return render(request, 'main/index.html')


def about(request):
    talabalar = ['Ali', 'Rustam', 'Hasan', 'Husan']
    # malumotlarni views dan templatega uzatish uchun
    context = {
        'talabalar': talabalar,
        'univer': 'TUIT'
    }

    return render(request, 'main/about.html', context)


def tovarlar(request):

    return render(request, 'main/tovarlar.html')

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
