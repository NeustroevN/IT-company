# from django.db import models
from django import forms 
from .models import UserApplication
from .models import Purchases
from .models import Order
from .models import Addresses

class AplicationForm(forms.ModelForm): 
    class Meta: 
        model = UserApplication 
        fields = "__all__"

class UserPurchase(forms.ModelForm):
    class Meta:
        model = Purchases
        fields = "__all__"

class UserAddressForm(forms.ModelForm):
    class Meta:
        model = Addresses
        fields = ['street', 'home_number', 'appartment', 'city', 'postal_code', 'email']

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['paid_type']
        
        
        



# class Feedback(models.Model):
#     title = models.CharField("Заголовок", max_length=100)
#     name = models.CharField("Имя", max_length=100)
#     email = models.EmailField("Email")
#     company = models.CharField("Компания", max_length=100)
#     phone = models.CharField("Телефон", max_length=17) 
#     message = models.TextField("Сообщение")