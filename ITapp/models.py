from django.db import models
from datetime import date
from django.urls import reverse
# from django.contrib.auth.models import User

# ----------------------------------------------------------
class Menu(models.Model):
    """Строка основного меню"""
    name = models.CharField("Название пункта меню", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)
    position = models.PositiveIntegerField('Позиция', default=1)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"
# ----------------------------------------------------------
class Service(models.Model):
    """Услуги"""
    name = models.CharField("Наименование услуги", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Банер", upload_to="img/", default='')
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

# ----------------------------------------------------------
class Specs(models.Model):
    """Характеристики"""
    name = models.CharField("Характеристика", max_length=100)
    description = models.TextField("Описание")
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Характеристика"
        verbose_name_plural = "Характеристики"



# ----------------------------------------------------------
class SolSpecs(models.Model):
    """Характеристики решений"""
    Title = models.CharField("Характеристика IT продудкта", max_length=100)
    Solution = models.ForeignKey("Solution", verbose_name="IT_продукт", on_delete=models.CASCADE, related_name="solution_specifications")
    Specs = models.ForeignKey(Specs, verbose_name="Характеристика", on_delete=models.CASCADE, related_name="specification_solutions")
    # Specs = models.ManyToManyField(Specs, verbose_name="Характеристика")
    value = models.CharField("Значение", max_length=100)  

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name = "Характеристика IT продудкта"
        verbose_name_plural = "Характеристики IT продудкта"

# ------------------------------------------------------------

class Solution(models.Model):
    """Готовые решения
    attributes: name
                desk
                image
        
    """
    name = models.CharField(verbose_name="Наименование", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="img/")
    # solution_specifications = models.ManyToManyField(SolSpecs, verbose_name="Характеристика")
    @property
    def price(self):
        for solspec in self.solution_specifications.all():
            if "Стоимость" in solspec.Title:
                return solspec.value

        
    @property
    def specifications(self):
        return [
                {'name': solution_specification.Specs.name,
                'description': solution_specification.Specs.description,
                "title": solution_specification.Title,
                "value": solution_specification.value
            } for solution_specification in self.solution_specifications.all()
        ]



    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "IT_продукт"
        verbose_name_plural = "IT_продукты"

# ----------------------------------------------------------
class AboutCompany(models.Model):
    """О компании"""
    description = models.TextField("О компании")
    image = models.ImageField("Банер", upload_to="img/")
    contacts = models.TextField("Наши контакты")
    mapimg = models.ImageField("Карта", upload_to="img/")
    
    def __str__(self):
        return self.description
    class Meta:
        verbose_name = "О компании"
        verbose_name_plural = "О компании"
# --------------------------------------------------------------
from django.core.validators import RegexValidator

class UserApplication(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    name = models.CharField("Имя", max_length=100)
    email = models.EmailField("Email")
    company = models.CharField("Компания", max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?7?\d{9,16}$', message="Номер телефона в формате: '+7-999-999-99-99'")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True) 
    message = models.TextField("Сообщение")
    
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщение"

# ------------------------------------------------------------
class Benefits (models.Model):
    """предложения/акции"""
    title = models.CharField("Заголовок", max_length=100)
    deckription = models.TextField("Описание")
    image = models.ImageField("Банер", upload_to="img/")
    
    def __str__(self):
        return self.title 
                
    class Meta:
        verbose_name = "Акции"
        verbose_name_plural = "Акция"

# ------------------------------------------------------------        
class Purchases (models.Model):
    """покупки"""
    title = models.CharField("Заголовок", max_length=100)
    deckription = models.TextField("Описание")
    price = models.CharField("Стоимость", max_length=100)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Покупка"
        verbose_name_plural = "Покупки"