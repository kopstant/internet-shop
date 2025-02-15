from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=11, required=False)
    username = forms.CharField(max_length=50, required=True)
    avatar = forms.ImageField(required=False)
    usable_password = None

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'first_name', 'last_name', 'phone_number', 'avatar', 'country', 'password1', 'password2')

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Please enter a valid phone number. Only numbers are allowed.')
        return phone_number
