from django.urls import path
from .views import upload_post, post_list



urlpatterns = [
    path('upload_post/', upload_post, name='upload_post'),
    path('post_list/', post_list, name = "post_list")
]
