from django.contrib import admin
from .models import Menu, Service, Specifications, Solution, SolutionSpecifications, AboutCompany, UserApplication, Benefits, Purchases, Cart, CartItem, Order, OrderItem


admin.site.register(Menu)
admin.site.register(Service)
admin.site.register(Specifications)
admin.site.register(Solution)
admin.site.register(SolutionSpecifications)
admin.site.register(AboutCompany)
admin.site.register(UserApplication)
admin.site.register(Benefits)
admin.site.register(Purchases)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(OrderItem)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)