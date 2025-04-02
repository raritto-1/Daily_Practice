from django.test import TestCase

# Create your tests here.

# @login_required
# def profile_update(request):
#     print("View Function Called")
    
#     user = request.user  # Get the logged-in user
#     form = ProfileUpdateForm(instance=user)  # Load form with user data

#     if request.method == "POST":
#         form = ProfileUpdateForm(request.POST, instance=user)
#         if form.is_valid():
#             updated_user = form.save(commit=False)  # Save data without committing
#             if form.cleaned_data.get("password"):  # If password is provided
#                 updated_user.set_password(form.cleaned_data["password"])  # Hash the password
#             updated_user.save()
#             update_session_auth_hash(request, updated_user)  # Prevent logout after password change
#             print("Form Saved Successfully")
#             return redirect("profile_update")

#     return render(request, "profile_update.html", {"form": form})
