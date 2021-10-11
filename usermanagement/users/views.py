from django.contrib.auth.models import User
from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from .models import Userprofile

from .forms import UserCreationForm,UserProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json

# Create your views here.
def about(request):
    return render(request,'about.html')













def signup(request):
    form=UserCreationForm()

    if request.method=="POST":
        form=UserCreationForm(request.POST)
        profileform=UserProfileForm(request.POST)
        if form.is_valid() and profileform.is_valid():
            user=form.save()
            profile=profileform.save(commit=False)

            profile.user=user

            profile.save()


            user = form.cleaned_data.get('email')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')
    else:
        form=UserCreationForm()
        profileform=UserProfileForm()





    context={'form':form,'profileform':profileform}
    return render(request, 'signup.html', context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
	
    if request.method == 'POST':
        #username = request.POST.get('username')
        email = request.POST.get('emailorusername')
        password =request.POST.get('password')

        if email.find('@') ==-1:
            user= authenticate(request, username=email, password=password)
        else:
            u=User.objects.get(email=email)
            user = authenticate(request, username=u.username, password=password) 

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Email OR password is incorrect')

    context = {}
    return render(request, 'login2.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/login')   
def home(request):
    users=User.objects.filter(is_staff=False)
    profiles=[]
    for user in users:
        profile=Userprofile.objects.get(user=user)
        dict={}
        dict['id']=user.id
        dict['email']=user.email
        dict['username']=user.username
        dict['address']=profile.address
        profiles.append(dict)
    return render(request,'home.html',{'users':profiles})

def deleteUser(request,id):
    #id=request.GET
    user=User.objects.get(id=id).delete()
    return redirect('home')

def editprofile(request):
    id=request.POST.get('id')
    address=request.POST.get('address')
    user=User.objects.get(id=id)
    profile=Userprofile.objects.get(user=user)
    profile.address=address
    profile.save()

    return redirect('home')