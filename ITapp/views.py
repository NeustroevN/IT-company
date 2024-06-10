from django.shortcuts import render, redirect
from .models import AboutCompany
from .models import Benefits
from .models import Service
from .models import Solution
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth import logout
from .forms import AplicationForm

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
def solution(request):
    our_solution = Solution.objects.all()
    return render(request, "solution.html", {"our_solution": our_solution})

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


from .forms import UserPurchase
def purchase_view(request):
    form = UserPurchase()
    return render(request, 'solution.html', {'form': form})

def purform(request): 
    if request.method == "POST": 
        form = UserPurchase(request.POST) 
        if form.is_valid(): 
            try: 
                form.save() 
                return redirect('/index') 
            except: 
                pass 
    else: 
        form = UserPurchase() 
    return render(request,'solution.html',{'form':form})        