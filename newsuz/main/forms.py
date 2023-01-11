from django.forms import ModelForm
from .models import Contact, Fikr


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['ism', 'mavzu', 'matn']


class FikrForm(ModelForm):
    class Meta:
        model = Fikr
        fields = ['ism', 'fikr']
