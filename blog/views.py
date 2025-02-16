from blog.forms import PostForm
from blog.models import Post
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


# Работает по принципу CRUD (Create(POST)-Read(GET)-Update(PUT/PATCH)-Delete(DELETE))
class PostListView(ListView):  # Отображает список объектов. Основной метод get.
    model = Post

    def get_queryset(self):
        return Post.objects.filter(publications_flag=True)


class PostDetailView(DetailView):  # Отображает детали конкретного объекта. Основной метод - get.
    model = PostForm

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.numbers_of_posts += 1
        obj.save()
        return obj


class PostCreateView(LoginRequiredMixin, CreateView):  # Создает новый объект. Методы - get, post, form_valid.
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:post_list')


class PostUpdateView(LoginRequiredMixin, UpdateView):  # Обновляет существующий объект. Методы - get, post, form_valid.
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:post_list')

    def get_success_url(self):
        return reverse('blog:post_detail', args=[self.kwargs.get('pk')])


class PostDeleteView(LoginRequiredMixin, DeleteView):  # Удаляет объект. Методы - get, post
    model = Post
    success_url = reverse_lazy('blog:post_list')
