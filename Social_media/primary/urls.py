from django.contrib import admin
from django.urls import path
from primary.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', main , name= 'main'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile_view, name='profile_view'),
    path('follow/<str:username>/', follow_user, name='follow_user'),   
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('upload_post/', upload_post, name='upload_post'),
    path('delete-post/<int:id>/', delete_post, name='delete_post')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
