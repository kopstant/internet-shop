from blog.models import Post
from django.core.exceptions import ValidationError
from django.forms import ModelForm


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "preview", "created_at", "publications_flag", "numbers_of_posts"]
        exclude = ["created_at", "numbers_of_posts"]

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Введите название заголовка'})
        self.fields['content'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Опишите ваш пост. Допустимое количество символов: 10 - 5000'})
        self.fields['preview'].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Загрузите изображение в формате JPEG, PNG, JPG. Размер не должен превышать 5MB'})
        self.fields['publications_flag'].widget.attrs.update(
            {'class': 'form-group'})

    def clean_content(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')
        if len(content) > 5000:
            raise ValidationError('Текст вашего поста должен содержать не менее 10 и не более 5000 символов')
        if len(content) < 5000:
            raise ValidationError('Текст вашего поста должен содержать не менее 10 и не более 5000 символов')

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        preview = cleaned_data.get('preview')

        forbidden_words = [
            'казино', 'криптовалюта', 'крипта', 'биржа',
            'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
        ]

        for word in forbidden_words:
            if word in title.lower():
                raise ValidationError(f'Название поста не может содержать запрещенное слово: {word}')

        if preview:
            if preview.size > 5 * 1024 * 1024:  # MB
                raise ValidationError('Размер файла не должен превышать 5MB')
            if not preview.name.lower().endswith(('.png', '.jpg', '.jpeg')):
                raise ValidationError('Размер файла не должен превышать 5MB')

        return cleaned_data
