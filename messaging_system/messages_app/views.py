from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Message, Conversation

# Send Message View
def send_message(request, recipient_username):
    recipient = User.objects.get(username=recipient_username)
    conversation, created = Conversation.objects.get_or_create(participants=request.user)
    if request.method == 'POST':
        content = request.POST['content']
        Message.objects.create(conversation=conversation, sender=request.user, content=content)
        return redirect('inbox')
    return render(request, 'send_message.html', {'recipient': recipient})

# Inbox View
def inbox(request):
    conversations = Conversation.objects.filter(participants=request.user)
    return render(request, 'inbox.html', {'conversations': conversations})

# Conversation Thread View
def conversation_view(request, conversation_id):
    conversation = Conversation.objects.get(id=conversation_id, participants=request.user)
    messages = conversation.message_set.all()
    return render(request, 'conversation.html', {'conversation': conversation, 'messages': messages})
