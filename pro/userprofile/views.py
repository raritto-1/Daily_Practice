from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .models import Profile, PostData
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from .form import ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash  
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


@login_required
def fun(request):
    profiles = Profile.objects.all() 
    return render(request, "base.html", {"profiles": profiles})

@login_required
def search_bar(request): 
    if request.method == "POST":
        search_query = request.POST.get("search")
        if search_query:
            users = User.objects.filter(username__icontains=search_query)  
            return render(request, "base.html", {"users": users})
    return render(request, "base.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(f"Username: {username}, Password: {password}")  # Debugging
        
        user = authenticate(request, username=username, password=password)

        if user is None:
            print("Authentication failed!")  # Debugging
        else:
            print(f"Authenticated User ID: {user.id}")  # Debugging

        if user is not None:
            auth_login(request, user)
            
            print(f"After login: {request.user.id}")  # Debugging
                       
            return redirect("fun")
        else:
            messages.error(request, "Invalid username or password")
    
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
            

            Profile.objects.create(user=user)  # Create a profile for the user
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
    return render(request, 'register.html')

def user_logout(request):
    auth_logout(request)
    return redirect('login')

@login_required
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    posts = PostData.objects.filter(user=user)  # Get all posts by the user
    return render(request, "profile.html", {"profile": profile, "posts": posts})



# def profile_update():
# def profile_update(request):
#     user = get_object_or_404(User, username=request.user.username)  # Fetch logged-in user
    
#     if request.method == "POST":
#         username = request.POST.get("username")  # Get username from form
#         email = request.POST.get("email")  # Get email from form

#         # Update user data
#         user.username = username
#         user.email = email
#         user.save()

#     return render(request, "profile_update.html", {"postdata": user})
# #     pass



# def profile_update(request):
#     user = request.user
#     username = user.username #initialize with default value
#     email = user.email #initialize with default value

#     if request.method == "POST":
#         username = request.POST.get("username", user.username) #use request.POST
#         email = request.POST.get("email", user.email)

#         user.username = username
#         user.email = email
#         user.save()

#     return render(request, "profile_update.html", {"postdata": user}) #Pass the user object
# @login_required  # Ensure that the user is logged in
# def profile_update(request):
#     if request.method == 'POST':
#         form = ProfileUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')  # Redirect to the profile page after successful update
#     else:
#         form = ProfileUpdateForm(instance=request.user)

#     return render(request, 'profile_update.html', {'form': form})
# @login_required
# def profile_update(request):
#     if request.method == "POST":
#         user = request.user
#         form = ProfileUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Profile updated successfully!")
#             return redirect("profile_update")  # Redirect to prevent form resubmission
#     else:
#         form = ProfileUpdateForm(instance=request.user)

#     return render(request, "profile_update.html", {"form": form})

from django.contrib.auth import update_session_auth_hash

def profile_update(request):
    user = request.user  # Get the logged-in user
    form = ProfileUpdateForm(instance=user)  # Load form with user data

    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=user)
        if form.is_valid():  # Ensures data integrity before saving
            updated_user = form.save(commit=False)  # Do not save yet

            # Check if a new password was provided
            new_password = form.cleaned_data.get("password")
            if new_password:
                updated_user.set_password(new_password)  # Hash password properly

            updated_user.save()  # Save the updated user
            update_session_auth_hash(request, updated_user)  # Prevent logout after password change
            return redirect("profile_update")

    return render(request, "profile_update.html", {"form": form})

'''
@login_required
def profile_update(request):
    print("view funcitons called')

    user = request.user #becaues of user reqeust to the django authenticiton to access the data form theere data base
    form  = profileupdateform(reqeust.post, instance = user)
    if form.is_valid():
    udpate_user = form.save(commit = false)
    why we wrote the commit = false ?
    because its didnot directly udpated to the data base its wait ulti the hasa password is not provided to the sytem or unitle they got commit = true
    or default also commit = true

    if form.cleaned_data.get("password")
    #clean password or other simples uman understandable password
        update_user.set_password(form.cleaned_data["password"])
        update_use.sava(commit = true)
        update_session_auth)_has(request, update_user)
        print("form save succefully")
        return redirect(reqest, "proifle_update,html',{form: form})

'''





# def get_all_users():
#     users = User.objects.all()
#     user_list = []
#     for user in users:
#         user_list.append({
#             "id": user.id,
#             "username": user.username,
#             "email": user.email,
#             "password" : user.password,
#             "is_staff": user.is_staff,
#             "is_active": user.is_active
#         })
#     return user_list

# print(get_all_users())


def print_password_functionailty(erqeust):
    user= User.objects.all()
    li = []
    for i in user:
        list.append({
            "username": user.username,
            "password" : user.password}
        )
    return li
print(print_password_functionailty)