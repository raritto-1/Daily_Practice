from django.db import models
from datetime import datetime
from django.utils import timezone
from whatsapp.views import send_message


# import pywhatkit

# print('use the country code before number ')
# number = input('mobile number :- ')  # Keep the number as a string
# data = input("message: ")
# hour = int(input('hour: '))
# min = int(input('min: '))

# # Send a WhatsApp Message to a Contact at the specified time
# pywhatkit.sendwhatmsg(number, data, hour, min)




class Message(models.Model):
    number = models.CharField(max_length=15)  # Use CharField for phone numbers
    data = models.TextField()
    day = models.CharField(max_length=10, blank=True)
    time = models.TimeField()

    def save(self, *args, **kwargs):
        if not self.day: 
            self.day = timezone.now().strftime('%A')  # Set to today's day
        super().save(*args, **kwargs)  # Call the original save method

    def __str__(self):
        return f"{self.day} - {self.number} - {self.data} at {self.time}"




