from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Post
from django.http import JsonResponse
from django.views.decorators.http import require_POST

@login_required(login_url='login')
def main(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"user": request.user, "posts": posts})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(f"Username: {username}, Password: {password}")

        user = authenticate(request, username=username, password=password)

        if user is None:
            print("Authentication failed!")  # Debugging
            messages.error(request, "Invalid username or password")
        else:
            print(f"Authenticated User ID: {user.id}")  # Debugging
            auth_login(request, user)
            print(f"After login: {request.user.id}")  # Debugging
            return redirect("main")

    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email_address = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        elif User.objects.filter(email=email_address).exists():
            messages.error(request, "Email is already registered")
        else:
            user = User.objects.create_user(username=username, password=password, email=email_address)
            Profile.objects.get_or_create(user=user)  # Safe profile creation
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')

    return render(request, 'register.html')

@login_required
def user_logout(request):
    auth_logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    # Fetch the profile of the logged-in user using request.user
    profile_user = request.user
    posts = Post.objects.filter(user=profile_user).order_by('-created_at')  # Corrected ordering
    
    context = {
        'profile_user': profile_user,
        'posts': posts,
        'is_own_profile': request.user == profile_user  # Check if it's the user's own profile
    }
    return render(request, 'profile.html', context)

@login_required
@require_POST
def follow_user(request, username):
    if not request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'error': 'Invalid request'}, status=400)
    
    try:
        user_to_follow = get_object_or_404(User, username=username)
        profile = user_to_follow.profile
        
        if request.user == user_to_follow:
            return JsonResponse({'error': 'Cannot follow yourself'}, status=400)
        
        if request.user in profile.followers.all():
            profile.followers.remove(request.user)
            action = 'unfollow'
        else:
            profile.followers.add(request.user)
            action = 'follow'
            
        return JsonResponse({
            'action': action,
            'followers_count': profile.followers.count(),
            'following_count': request.user.profile.following_count
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@login_required
def edit_profile(request):
    
    profile = Profile.objects.get(user=request.user)
    
    if request.method == "POST":
        
        new_bio = request.POST.get('bio', '')
        profile.bio = new_bio
        profile.save()

        messages.success(request, 'Profile updated successfully!')
        return redirect('profile_view')  

    
    return render(request, 'edit_profile.html', {'profile': profile})


@login_required
def upload_post(request):
    if request.method == 'POST':
        image = request.FILES.get('image')

        if image:
            try:
                Post.objects.create(user=request.user, image=image)
                messages.success(request, 'Post uploaded successfully!')
                return redirect('main')  # make sure 'main' is a valid URL name
            except Exception as e:
                messages.error(request, f'Error uploading post: {str(e)}')
        else:
            messages.error(request, 'Please select an image to upload.')

    return render(request, 'upload_post.html')



@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id, user=request.user)
    post.delete()
    return redirect('profile')
