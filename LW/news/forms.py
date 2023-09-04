from .models import Articles
from django.utils import timezone
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, FileInput

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['name', 'title', 'text', 'img']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Содержание'
            }),"img": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Изображение'
            })
        }
