from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Message


def chat_bet(request):
    users = User.objects.all()  # Get all users

    user_messages = {}
    # Fetch messages for each user
    for user in users:
        messages_for_user = Message.objects.filter(sender=user).values("content", "timestamp")  # Change 'user' to 'i'
        user_messages[user.username] = messages_for_user

    context = {
        "users": users,
        "user_messages": user_messages
    }
    return render(request, "base.html", context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_auth = authenticate(request, username=username, password=password)

        if user_auth is not None:
            auth_login(request, user_auth)  # Log in the user
            return redirect('chat')  # Redirect to the chat view
        else:
            # Display error messages for invalid login
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Invalid password. Please try again.')
            else:
                messages.error(request, 'No user found with that username. Please register first.')

    return render(request, 'login.html')


def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email_address = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        
        if not username or not email_address or not password or not confirm_password:
            messages.error(request, 'All fields are required.')
        elif password != confirm_password:
            messages.error(request, 'Passwords do not match.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        elif User.objects.filter(email=email_address).exists():
            messages.error(request, 'Email is already in use.')
        else:
            
            user = User.objects.create_user(username=username, password=password, email=email_address)
            user.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')

    return render(request, 'register.html')


def log_out(request):
    auth_logout(request) 
    return redirect('login')
