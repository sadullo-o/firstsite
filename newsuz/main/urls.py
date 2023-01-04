from django.urls import path
from .views import asosiy, about, tovarlar, details

urlpatterns = [
    path('', asosiy, name='main'),  # 127.0.0.1:8000
    path('about', about, name='about'), #  127.0.0.1:8000/about
    path('mahsulotlar', tovarlar, name='tovarlar'),
    path('mahsulotlar/<str:pk>', details, name='detail')

]