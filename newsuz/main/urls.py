from django.urls import path
from .views import asosiy, about, tovarlar, details, news, contact

urlpatterns = [
    path('', asosiy, name='main'),  # 127.0.0.1:8000
    path('about', about, name='about'), #  127.0.0.1:8000/about
    path('mahsulotlar', tovarlar, name='tovarlar'),
    path('mahsulotlar/<str:pk>', details, name='detail'),
    path('news/<str:pk>', news, name='news'),
    path('contact', contact, name='contact')

]