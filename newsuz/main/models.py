import datetime

from django.db import models

# Create your models here.
# malumotlar bazasida yaratiladigan table va uning ustunlari shu yerda yaratiladi


class Yangiliklar(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    type = models.CharField(max_length=50, default='')

# mahalliy
# dunyo

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'news'



class Info(models.Model):
    title = models.CharField(max_length=100)
    info = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'info'
        verbose_name_plural = 'Infos'




class Contact(models.Model):
    ism = models.CharField(max_length=50)
    mavzu = models.CharField(max_length=50)
    matn = models.TextField()
    vaqt = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.ism


class Fikr(models.Model):
    ism = models.CharField(max_length=50)
    fikr = models.TextField()
    vaqt = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.ism

# 1. python manage.py makemigrations

# 2. python manage.py migrate