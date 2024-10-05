
from django.contrib import admin
from .models import Conversation, Message

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')  
    search_fields = ('participants__username',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'conversation', 'timestamp', 'read')
    search_fields = ('content',)
    list_filter = ('conversation', 'read')
