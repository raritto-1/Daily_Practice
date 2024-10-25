from django.contrib import admin
from .models import ChatRoom, Message

class MessageInline(admin.TabularInline):
    model = Message
    extra = 1
    fields = ('sender', 'receiver', 'content', 'timestamp', 'is_read')
    readonly_fields = ('timestamp',)

class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    inlines = [MessageInline]

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'chat_room', 'timestamp', 'is_read')
    list_filter = ('is_read', 'timestamp')
    search_fields = ('content',)
    readonly_fields = ('timestamp',)

# Register your models here
admin.site.register(ChatRoom, ChatRoomAdmin)
admin.site.register(Message, MessageAdmin)
