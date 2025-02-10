from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Post


# Работает по принципу CRUD (Create(POST)-Read(GET)-Update(PUT/PATCH)-Delete(DELETE))
class PostListView(ListView):  # Отображает список объектов. Основной метод get.
    model = Post


class PostDetailView(DetailView):  # Отображает детали конкретного объекта. Основной метод - get.
    model = Post


class PostCreateView(CreateView):  # Создает новый объект. Методы - get, post, form_valid.
    model = Post
    fields = ("title", "content", "preview", "publications_flag")
    success_url = reverse_lazy('blog:post_list')


class PostUpdateView(UpdateView):  # Обновляет существующий объект. Методы - get, post, form_valid.
    model = Post
    fields = ("title", "content", "preview", "publications_flag")
    success_url = reverse_lazy('blog:post_list')


class PostDeleteView(DeleteView):  # Удаляет объект. Методы - get, post
    model = Post
    success_url = reverse_lazy('blog:post_list')
