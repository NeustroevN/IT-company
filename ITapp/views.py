from django.shortcuts import render, get_object_or_404, redirect
from .models import AboutCompany
from .models import Benefits
from .models import Service
from .models import Solution
from .models import Cart, CartItem
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth import logout
from .forms import AplicationForm
from .forms import UserPurchase
# from django.contrib import messages
from .models import OrderItem
from .forms import OrderCreateForm
from .forms import UserAddressForm
from .models import Order


def index(request):
    benefits = Benefits.objects.all() 
    return render(request, "index.html", {"our_benefits": benefits})
   

def about(request):
    our_info = AboutCompany.objects.all() 
    return render(request, "about.html", {"info": our_info})
def contact(request):
    our_info = AboutCompany.objects.all() 
    return render(request, "contact.html", {"info": our_info})
def service(request):
    our_service = Service.objects.all()
    return render(request, "service.html", {"our_service": our_service})

def application(request):
    return render(request, "application.html")

def logoutUser(request):
    logout(request)
    return redirect('index')


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def application_view(request):
    form = AplicationForm()
    return render(request, 'application.html', {'form': form})

def appform(request): 
    if request.method == "POST": 
        form = AplicationForm(request.POST) 
        if form.is_valid(): 
            try: 
                form.save() 
                return redirect('/index') 
            except: 
                pass 
    else: 
        form = AplicationForm() 
    return render(request,'application.html',{'form':form}) 



def purchase_view(request):
    form = UserPurchase()
    return render(request, 'solution.html', {'form': form})

def solution(request):
    our_solution = Solution.objects.all()
    return render(request, "solution.html", {"our_solution": our_solution})

def purform(request): 
    # messages.success(request, 'Запущен purform')
    if request.method == "POST": 
        form = UserPurchase(request.POST) 
        # form = solution(request.POST)
        if form.is_valid(): 
            try: 
                form.save() 
                return redirect('/index') 
            except: 
                pass 
    else: 
        form = UserPurchase() 
    return render(request,'solution.html', {'form': form})        


# ------------------ CART --------------------------------------
def count_cart_solution(request):
    # cart_id = request.session.get('cart_id')
    # request.session['items_total'] = CartItem.objects.filter(cart=cart_id).count()
    
    user_id = request.user.id
    # cart = Cart.objects.filter(user_id=user_id).all()
    cart = get_object_or_404(Cart, user_id=user_id)
    cart_id = cart.id
    if not cart_id:
        request.session['items_total'] = 0   
    else:
        request.session['items_total'] = CartItem.objects.filter(cart=cart_id).count()   


# def add_to_purchases(request, solution_id):


#     remove_from_cart(solution_id=solution_id)
#     count_cart_solution(request)
#     return redirect('solution')

def add_to_cart(request, solution_id):
    # solution = get_object_or_404(Solution, id=solution_id)
    # cart_id = request.session.get('cart_id')
    # # cart = Cart.objects.create(user=request.user)
    # # request.session['cart_id'] = cart.id
    # if not cart_id:
    #     cart = Cart.objects.create(user=request.user)
    #     request.session['cart_id'] = cart.id
    # else:
    #     cart = get_object_or_404(Cart, id=cart_id)
    # cart_item, created = CartItem.objects.get_or_create(cart=cart, solution=solution)
    # if not created:
    #     cart_item.quantity += 1
    # cart_item.save()

    # --------------------------------
    solution = get_object_or_404(Solution, id=solution_id)
    user_id = request.user.id
    # usercarts = Cart.objects.get(user_id=user_id)
    # usercarts = get_object_or_404(Cart, user_id=user_id)
    usercarts = Cart.objects.filter(user_id=user_id).all()
    if not usercarts:
        cart = Cart.objects.create(user=request.user)
    else:
        cart = get_object_or_404(Cart, user_id=user_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, solution=solution)
    if not created:
        cart_item.quantity += 1
    cart_item.save()

    count_cart_solution(request)
    return redirect('solution')


def update_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    if request.method == 'POST':
        cart_item.quantity = int(request.POST.get('quantity', 1))
        cart_item.save()
    return redirect('cart_detail')

def cart_detail(request):
    # cart_id = request.session.get('cart_id')
    # if not cart_id:
    #     return render(request, 'cart_detail.html', {'cart': None, 'total_price': 0})

    # cart = get_object_or_404(Cart, id=cart_id)

    # # cart = get_object_or_404(Cart, cart=cart_id)
    # # cart = get_object_or_404(Cart, id=cart_id, user_id=request.user.id)
    # # cart = Cart.objects.all(user=request.user)
    # # cart = get_object_or_404(Cart, id=cart_id, user=user_in)
    # total_price = sum(item.total_price() for item in cart.cartitem_set.all())
    # count_cart_solution(request)
    # return render(request, 'cart_detail.html', {'cart': cart, 'total_price': total_price})

    user_id = request.user.id
    # cart = Cart.objects.filter(user_id=user_id).all()
    cart = get_object_or_404(Cart, user_id=user_id)
    if not cart:
        return render(request, 'cart_detail.html', {'cart': None, 'total_price': 0})
    total_price = sum(item.total_price() for item in cart.cartitem_set.all())
    count_cart_solution(request)
    return render(request, 'cart_detail.html', {'cart': cart, 'total_price': total_price})


def remove_from_cart(request, solution_id):
    # cart_id = request.session.get('cart_id')
    # cart = get_object_or_404(Cart, id=cart_id)
    user_id = request.user.id
    cart = get_object_or_404(Cart, user_id=user_id)
    cart_item = get_object_or_404(CartItem, cart=cart, solution_id = solution_id)
    cart_item.delete()
    # cart.delete()
    count_cart_solution(request)
    # return redirect('cart_detail')
    return redirect('solution')



def order_create(request):
    # cart = Cart(request)
    
    cart = get_object_or_404(Cart, user_id=request.user.id)



    if not cart:
        return render(request, 'cart_detail.html', {'cart': None, 'total_price': 0})
    else:
        total_price = sum(item.total_price() for item in cart.cartitem_set.all())
        if request.method == 'POST':
            form = UserAddressForm(request.POST)
            formOrder = OrderCreateForm(request.POST)
            # form = OrderCreateForm(request.POST)
            # form.pay
            if form.is_valid():
                adress = form.save()
                # order = form.save()

                Order.objects.create(user=request.user.id,
                                    address=adress,
                                    paid_type=formOrder)
                order = formOrder

                for item in cart.cartitem_set.all():
                    solution = get_object_or_404(Solution, id = item.solution_id)
                    price_of_solution = solution.price * item.quantity 
                    OrderItem.objects.create(order=order,
                                            product=item.solution,
                                            price=price_of_solution,
                                            quantity=item.quantity)
                # очистка корзины
                # cart.clear()
                
                # if order.paid_type == 'карта':
                    
                
                return render(request, 'order_created.html',
                            {'order': order})
        else:
            form = UserAddressForm 
            formOrder = OrderCreateForm
            # OrderCreateForm
        return render(request, 'order_create.html',
                    {'cart': cart, 'form': form, 'formOrder': formOrder, 'total_price': total_price})