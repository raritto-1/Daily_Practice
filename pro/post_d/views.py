from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post  # Import your Post model
from django.contrib.auth.decorators import login_required #restrict to logged in users
from django.contrib.auth.models import User

@login_required # Apply the login required decorator
def upload_post(request):

    if request.method == 'POST':
        # Process the form submission
        image_post = request.FILES.get('image_post')  # Use .get() to avoid KeyError
        description = request.POST.get('description')  # Use .get()

        if image_post: #check if image_post is not None
            # Create a new Post object
            
            post = Post(
                image_post=image_post,
                description=description,
                user=request.user  # Associate the post with the logged-in user
            )
            try:
                post.save()  # Save the post to the database
                messages.success(request, 'Post uploaded successfully!')
                return redirect('home')  # Redirect to the home page or a success page
            except Exception as e:
                messages.error(request, f'Error uploading post: {e}')
                # Optionally, log the error for debugging
                return render(request, 'upload_post.html') # Render the form again
        else:
             messages.error(request, 'Please select an image to upload.')
             return render(request, 'upload_post.html')

    else:
        # If the request method is not POST, render the upload form
        return render(request, 'upload_post.html')

