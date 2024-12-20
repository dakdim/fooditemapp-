from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserChangeForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.views import View

# Create your views here.

def register(request):
    if request .method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'welcome {username},your account is created')
            return redirect('login')
            return render(request,'users/register.html',{'form':form})
        
    else:    
       form=RegisterForm()
    return render(request,'users/register.html',{'form':form})
@login_required

def profilepage(request):
    return render(request,'users/profile.html')


