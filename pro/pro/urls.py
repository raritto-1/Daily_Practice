from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from userprofile import views  # Ensure this matches your app's name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.fun, name='fun'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('search_bar/', views.search_bar, name='search_bar'),
    # path('profile/<str:username>/', views.user_profile, name='user_profile'),  # New URL pattern for user profiles
    path("profile_update/",views.profile_update, name = "profile_update"),
    # path('profile/<str:username>/', views.profile_view, name='profile'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
