from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm #its use to maniputle the table fome

from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class ProfileUpdateForm(UserChangeForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)  # Explicitly define password

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def save(self, commit=True):
        user = super().save(commit=False)

        new_password = self.cleaned_data.get("password")
        if new_password:  # Check if a new password is provided
            user.set_password(new_password)  # Hash the new password

        if commit:
            user.save()
        return user

