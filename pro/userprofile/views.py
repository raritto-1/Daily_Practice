from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

def fun(request):
    return render(request, "base.html")


def search_bar(request): 
    if request.method == "POST":
        search_query = request.POST.get("search")
        if search_query:
            users = User.objects.filter(username__icontains=search_query)  
            if users.exists():
                print(users)
                return render(request, "base.html", {"users": users})
            else:
                return render(request, 'base.html', {'error': 'Username not found'})
    return render(request, "base.html")
        
     


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("fun")
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Invalid password")  
            else:
                messages.error(request, 'No user found with that username. Please register first.')

    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email_address = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
                
        if not username or not email_address or not password or not confirm_password:
            messages.error(request, "Please fill every detail")
        elif password != confirm_password:
            messages.error(request, "Passwords do not match")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        elif User.objects.filter(email=email_address).exists():
            messages.error(request, "Email is already registered")
        else:
            user = User.objects.create_user(username=username, password=password, email=email_address)
            user.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')

    return render(request, 'register.html')

def user_logout(request):
    auth_logout(request)
    return redirect('login')



def upload_post(request):
    if request.method == "POST":
        image_field = models.

    
