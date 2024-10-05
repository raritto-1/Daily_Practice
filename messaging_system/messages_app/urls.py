from django.urls import path
from . import views

urlpatterns = [
    path('send/<str:recipient_username>/', views.send_message, name='send_message'),
    path('inbox/', views.inbox, name='inbox'),
    path('conversation/<int:conversation_id>/', views.conversation_view, name='conversation_view'),
]
