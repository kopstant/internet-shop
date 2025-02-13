from django.forms import ModelForm
from catalog.models import Product
from django.core.exceptions import ValidationError


class ProductForm(ModelForm):
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

    def clean_price(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('price')
        if price <= 0:
            raise ValidationError("Цена не может быть отрицательной либо равняться нулю")

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
                raise ValidationError(f'Название продукта содержит запрещенное слово: {word}')

        if preview:
            if preview.size > 5 * 1024 * 1024:  # 5MB
                raise ValidationError('Размер файла не должен превышать 5MB')
            if not preview.name.lower().endswith(('.png', '.jpg', '.jpeg')):
                raise ValidationError('Файл должен быть в формате JPEG, PNG, JPG')
        return cleaned_data
