from django.shortcuts import render
from .models import Message
import pywhatkit

def send_message_view(request):
    if request.method == "POST":
        number = request.POST.get('number')
        data = request.POST.get('data')
        time = request.POST.get('time')

        # Split time to get hour and minute
        try:
            hour, minute = map(int, time.split(':'))
        except ValueError:
            return render(request, 'index.html', {'error_message': 'Invalid time format. Please use HH:MM.'})

        # Create a Message instance but do not save it yet
        message = Message(number=number, data=data, time=f"{hour}:{minute}")

        try:
            # Send the WhatsApp message
            pywhatkit.sendwhatmsg(number, data, hour, minute)
            
            # Save the message after successful sending
            message.save()
            success_message = 'Your message has been sent successfully.'
        except Exception as e:
            success_message = f'Failed to send message: {str(e)}'

        return render(request, 'index.html', {'success_message': success_message})

    return render(request, 'index.html')
