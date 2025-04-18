from django.urls import path
from .views import upload_post

from . import views

urlpatterns = [
    path('upload_post/', upload_post, name='upload_post'),
]
