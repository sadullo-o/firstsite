from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Yangiliklar, Info, Fikr
from .forms import ContactForm, FikrForm
import datetime

# Create your views here.

# frontend bilan boglaydigan kodlar shu yerda yoziladi

def asosiy(request):
    news = Yangiliklar.objects.all()
    context = {
        'news': news
    }

    if request.method == 'POST':
        form = FikrForm(request.POST)
        if form.is_valid():
            form.save()
            print('Saqlandi')
            return redirect('main')

        else:
            print('Xatolik boldi')

    return render(request, 'main/index.html', context)


def news(request, pk):

    news = Yangiliklar.objects.all().filter(type=pk)
    context = {
        'news': news
    }

    return render(request, 'main/news.html', context)






def about(request):
    infos = Info.objects.all()
    fikrlar = Fikr.objects.all()

    context = {
        'info': infos,
        'fikrlar': fikrlar
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

def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            print('Saqlandi')
            return redirect('contact')

        else:
            print('Xatolik boldi')


    return render(request, 'main/contact.html')




# def about(request):
#     hozir = datetime.datetime.now()
#     return HttpResponse(hozir)



# o'zingiz haqingizda sayt
# Main, MyProjects, About Me, Contact
