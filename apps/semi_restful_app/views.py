from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from .models import *

def index(request):
    all_users = User.objects.all()
    context = {
        'users': all_users
    }
    return render(request, 'semi_restful_app/index.html', context)

def new(request):
    return render(request, 'semi_restful_app/new.html')

def create(request):
    User.objects.create(
        first_name= request.POST['first_name'], 
        last_name = request.POST['last_name'], 
        Email = request.POST['Email']
        )
    return redirect('/users')

def show(request,user_id):
    the_user = User.objects.get(id=user_id)
    context={
        "user": the_user
    }
    return render(request, 'semi_restful_app/show.html', context)

def edit(request,user_id):
    the_user = User.objects.get(id=user_id)
    context={
        "user": the_user
    }
    return render(request,'semi_restful_app/edit.html', context)

def update(request, user_id):
    the_user = User.objects.get(id=user_id)
    the_user.first_name = request.POST['first_name']
    the_user.last_name = request.POST['last_name']
    the_user.Email = request.POST['Email']
    the_user.save()
    return redirect('/users')

def destroy(request,user_id):
    the_user = User.objects.get(id=user_id)
    the_user.delete()
    return redirect('/users')