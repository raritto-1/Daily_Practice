from django.contrib import admin
from django.urls import path, include  # fixed typo here
from django.conf import settings
from django.conf.urls.static import static
from userprofile import views  # app views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.fun, name='fun'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('search_bar/', views.search_bar, name='search_bar'),
    path('profile_update/', views.profile_update, name='profile_update'),

    path('upload_post/', include('post_d.urls')),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
