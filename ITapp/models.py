from django.db import models
from django.core.validators import RegexValidator,  MinValueValidator
from django.contrib.auth.models import User

class Menu(models.Model):
    """Строка основного меню"""
    name = models.CharField("Название пункта меню", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)
    position = models.PositiveIntegerField('Позиция', default=1)

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    def __str__(self):
        return self.name
    

class Service(models.Model):
    """Услуги"""
    name = models.CharField("Наименование услуги", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Банер", upload_to="img/", default='')
    
    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.name


class Specifications(models.Model):
    """Характеристики"""
    name = models.CharField("Характеристика", max_length=100)
    description = models.TextField("Описание")
    
    class Meta:
        verbose_name = "Характеристика"
        verbose_name_plural = "Характеристики"

    def __str__(self):
        return self.name


class SolutionSpecifications(models.Model):
    """Характеристики решений"""
    title = models.CharField("Характеристика IT продудкта", max_length=100)
    solution = models.ForeignKey("Solution", verbose_name="IT_продукт", on_delete=models.CASCADE, related_name="solution_specifications")
    specification = models.ForeignKey(Specifications, verbose_name="Характеристика", on_delete=models.CASCADE, related_name="specification_solutions")
    # Specs = models.ManyToManyField(Specs, verbose_name="Характеристика")
    value = models.CharField("Значение", max_length=100)  

    class Meta:
        verbose_name = "Характеристика IT продукта"
        verbose_name_plural = "Характеристики IT продуктов"
    
    def __str__(self):
        return self.title    


class Solution(models.Model):
    """Готовые решения"""
    name = models.CharField(verbose_name="Наименование", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="img/")
    price = models.DecimalField(decimal_places=2, max_digits=15, null=True,
                                validators=[MinValueValidator(0)],
                                verbose_name="Стоимость")
    # solution_specifications = models.ManyToManyField(SolSpecs, verbose_name="Характеристика")
    # @property
    # def price(self):
    #     for solspec in self.solution_specifications.all():
    #         if "Стоимость" in solspec.Title:
    #             return solspec.value
        
    # @property
    # def specifications(self):
    #     return [
    #             {'name': solution_specification.Specs.name,
    #             'description': solution_specification.Specs.description,
    #             "title": solution_specification.Title,
    #             "value": solution_specification.value
    #         } for solution_specification in self.solution_specifications.all()
    #     ]

    class Meta:
        verbose_name = "IT_продукт"
        verbose_name_plural = "IT_продукты"

    def __str__(self):
        return self.name


class AboutCompany(models.Model):
    """О компании"""
    description = models.TextField("О компании")
    image = models.ImageField("Банер", upload_to="img/")
    contacts = models.TextField("Наши контакты")
    mapimg = models.ImageField("Карта", upload_to="img/")
    
    class Meta:
        verbose_name = "О компании"
        verbose_name_plural = "О компании"

    def __str__(self):
        return self.description


class UserApplication(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    name = models.CharField("Имя", max_length=100)
    email = models.EmailField("Email")
    company = models.CharField("Компания", max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?7?\d{9,16}$', message="Номер телефона в формате: '+7-999-999-99-99'")
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True) 
    message = models.TextField("Сообщение")
    
    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return self.title


class Benefits (models.Model):
    """предложения/акции"""
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Банер", upload_to="img/")
    
    class Meta:
        verbose_name = "Акции"
        verbose_name_plural = "Акции"

    def __str__(self):
        return self.title 


class Purchases (models.Model):
    """покупки"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE, verbose_name="IT решение", null=True)
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество",)
    total_price = models.DecimalField(decimal_places=2, max_digits=15, verbose_name="Стоимость", null=True)
    pay_type = models.CharField(verbose_name="Способ оплаты", max_length=100, null=True)
    status = models.CharField(verbose_name="Статус", max_length=100, null=True)

    class Meta:
        verbose_name = "Покупка/Заказ"
        verbose_name_plural = "Покупки/Заказы"
    
    def __str__(self):
        return self.name

class Addresses(models.Model):
    """Адрес пользователя"""
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    street = models.CharField(max_length=100, verbose_name='Улица')
    home_number = models.CharField(max_length=50, verbose_name='Номер дома')
    appartment = models.CharField(max_length=50, verbose_name='Номер квартиры')
    city = models.CharField(max_length=100, verbose_name='Город')
    postal_code = models.CharField(max_length=20, verbose_name='Индекс')
    email = models.EmailField()
    
    class Meta:
        verbose_name = "Адреса пользователей"
        verbose_name_plural = "Адреса пользователей"
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    address = models.ForeignKey(Addresses, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False, verbose_name='Статус платежа')
    paid_type = models.CharField(max_length=10, verbose_name='тип оплаты', choices=[("card", "карта" ), ("after", "Постоплата")], null=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Solution, on_delete=models.CASCADE, verbose_name="IT решение", null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity


class Cart(models.Model):
    """Корзина. Заголовок"""
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name="Заголовок корзины")
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE, verbose_name="IT решение",)
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество",)

    class Meta:
        verbose_name = "Позиция корзины"
        verbose_name_plural = "Позиции корзины"

    def __str__(self):
        return f"{self.quantity} x {self.solution.name}"

    def total_price(self):
        return self.quantity * self.solution.price