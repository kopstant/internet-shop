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
        fields = (
            'email', 'username', 'first_name', 'last_name', 'phone_number', 'avatar', 'country', 'password1',
            'password2')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Введите ваш e-mail'})
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Введите ваш логин'})
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Введите ваше имя'})
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Введите вашу фамилию'})
        self.fields['phone_number'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Введите ваш номер телефона'})
        self.fields['avatar'].widget.attrs.update(
            {'class': 'avatar', 'placeholder': 'Выберите изображение для вашего профиля'})
        self.fields['country'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Введите вашу страну'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Введите пароль'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Подтвердите пароль'})

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Please enter a valid phone number. Only numbers are allowed.')
        return phone_number
