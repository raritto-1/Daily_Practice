from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import FileExtensionValidator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(default="default.jpg", upload_to="profile_pics/")
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    joined_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        # Ensure that the default image path is relative to MEDIA_ROOT
        if self.image == "default.jpg":
            self.image = "profile_pics/default.jpg" #Correct default image path

        super().save(*args, **kwargs)


class PostData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    image_field = models.ImageField(
        upload_to="static/default-profile.jpg",
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif'])]
    )
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"



class ler(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email_ler = models.EmailField()
    password = models.CharField(max_length=128)

# from django.db import models
# from django.contrib.auth.models import User
# from django.core.validators import FileExtensionValidator
# import os

# def user_post_directory_path(instance, filename):
#     """Generates the upload path for the post image."""
#     return f'user_{instance.user.id}/posts/{filename}'

# class Post(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
#     image = models.ImageField(
#         upload_to=user_post_directory_path,
#         validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif'])],
#         null=True,
#         blank=True
#     )
#     description = models.TextField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

#     class Meta:
#         ordering = ['-created_at'] # Optional: Order posts by creation date (newest first)