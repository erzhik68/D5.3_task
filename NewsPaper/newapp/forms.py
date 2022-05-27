from django.forms import ModelForm
from .models import Post


# Создаём модельную форму
class PostForm(ModelForm):
    # в класс мета, пишем модель, по которой будет строиться форма и перечисляем нужные нам поля.
    class Meta:
        model = Post
        fields = ['post_type', 'post_author', 'post_category', 'post_title', 'post_text']