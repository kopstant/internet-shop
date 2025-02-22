from django.forms import ModelForm

from catalog.models import Product, Contact
from django.core.exceptions import ValidationError
from django import forms


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'product_name',
            'description',
            'preview',
            'category',
            'price',
            'created_at',
            'updated_at',
            'publications_flag',
        ]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['product_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Введите название продукта'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Опишите ваш продукт'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите цену продукта'})
        self.fields['created_at'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Введите дату создания продукта в формате "year-month-day"'})
        self.fields['updated_at'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Введите дату обновления продукта в формате "year-month-day"'})
        self.fields['publications_flag'].widget.attrs.update({'class': 'form-group'})

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError("Цена не может быть отрицательной либо равняться нулю")
        return price

    def clean(self):
        cleaned_data = super().clean()
        product_name = cleaned_data.get('product_name')
        description = cleaned_data.get('description')
        preview = cleaned_data.get('preview')

        forbidden_words = [
            'казино', 'криптовалюта', 'крипта', 'биржа',
            'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
        ]

        for word in forbidden_words:
            if word in product_name.lower():
                raise ValidationError(f'Название продукта содержит запрещенное слово: {word}')

            if word in description.lower():
                raise ValidationError(f'Описание продукта содержит запрещенное слово: {word}')

        if preview:
            if preview.size > 5 * 1024 * 1024:  # 5MB
                raise ValidationError('Размер файла не должен превышать 5MB')
            if not preview.name.lower().endswith(('.png', '.jpg', '.jpeg')):
                raise ValidationError('Файл должен быть в формате JPEG, PNG, JPG')
        return cleaned_data


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'created_at']
        exclude = ['created_at']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите имя'  # Текст подсказки внутри поля
        })
        # Настройка атрибутов виджета для поля 'email'
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите email'  # Текст подсказки внутри поля
        })
        # Настройка атрибутов виджета для поля 'message'
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите текст вашего сообщения'  # Текст подсказки внутри поля
        })

    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 10 or len(message) > 5000:
            raise ValidationError('Текст вашего поста должен содержать не менее 10 и не более 5000 символов')
        return message

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith(('@mail.ru', '@yandex.ru')):
            raise ValidationError('Email должен оканчиваться на @mail.ru или @yandex.ru')
        return email

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')

        forbidden_words = [
            'казино', 'криптовалюта', 'крипта', 'биржа',
            'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
        ]

        for word in forbidden_words:
            if word in name.lower():
                raise ValidationError(f'Имя содержит запрещенное слово: {word}')
        return cleaned_data


class ModeratorProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'publications_flag',
        )
