from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse

from blog.models import Post


# Работает по принципу CRUD (Create(POST)-Read(GET)-Update(PUT/PATCH)-Delete(DELETE))
class PostListView(ListView):  # Отображает список объектов. Основной метод get.
    model = Post

    def get_queryset(self):
        return Post.objects.filter(publications_flag=True)


class PostDetailView(DetailView):  # Отображает детали конкретного объекта. Основной метод - get.
    model = Post

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.numbers_of_posts += 1
        obj.save()
        return obj


class PostCreateView(CreateView):  # Создает новый объект. Методы - get, post, form_valid.
    model = Post
    fields = ("title", "content", "preview", "publications_flag")
    success_url = reverse_lazy('blog:post_list')


class PostUpdateView(UpdateView):  # Обновляет существующий объект. Методы - get, post, form_valid.
    model = Post
    fields = ("title", "content", "preview", "publications_flag")
    success_url = reverse_lazy('blog:post_list')

    def get_success_url(self):
        return reverse('blog:post_detail', args=[self.kwargs.get('pk')])


class PostDeleteView(DeleteView):  # Удаляет объект. Методы - get, post
    model = Post
    success_url = reverse_lazy('blog:post_list')
