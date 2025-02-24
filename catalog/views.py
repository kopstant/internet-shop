from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, get_object_or_404, render
from catalog.forms import ProductForm, ContactForm, ModeratorProductForm
from catalog.models import Product, Contact, Category
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from catalog.services import get_products_from_cache, list_products_in_category


class ProductListView(LoginRequiredMixin, ListView):
    model = Product

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.has_perm('catalog.can_unpublish_product'):
            return Product.objects.all()  # Показывает все продукты
        return Product.objects.filter(publications_flag=True)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    def get_queryset(self):
        return get_products_from_cache()


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_form_class(self):
        user = self.request.user
        product = self.get_object()

        # Если пользователь - владелец, разрешаем полное редактирование
        if user == product.owner:
            return ProductForm

        if user.has_perm('catalog.can_unpublish_product') and user.has_perm('catalog.delete_product'):
            if not user.groups.filter(name='manager_products').exists():
                raise PermissionDenied("Вы не состоите в группе модераторов.")
            return ModeratorProductForm  # Модератор может редактировать только флаг публикации

        # Во всех остальных случаях запрещаем доступ.
        raise PermissionDenied

    def form_valid(self, form):
        user = self.request.user
        product = self.get_object()

        # Проверка прав на отмену публикации
        if 'publications_flag' in form.changed_data and not user.has_perm('catalog.can_unpublish_product'):
            raise PermissionDenied("У вас нет прав на отмену публикации продукта.")

        product.publications_flag = form.cleaned_data['publications_flag']
        product.save()
        return redirect(reverse_lazy('catalog:product_list'))


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

    def dispatch(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=self.kwargs['pk'])
        user = request.user

        # Проверка прав на удаление продукта
        if user != product.owner:
            if user.has_perm('catalog.delete_product') and user.groups.filter(name='manager_products').exists():
                return super().dispatch(request, *args, **kwargs)
            raise PermissionDenied("У вас нет прав на удаление этого продукта.")

        return super().dispatch(request, *args, **kwargs)


class ContactListView(LoginRequiredMixin, ListView):
    model = Contact


class ContactDetailView(LoginRequiredMixin, DetailView):
    model = Contact


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('catalog:contact_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ContactUpdateView(LoginRequiredMixin, UpdateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('catalog:contact_list')


class ContactDeleteView(LoginRequiredMixin, DeleteView):
    model = Contact
    success_url = reverse_lazy('catalog:contact_list')


def category_product_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'catalog/category_product_list.html', {'category': category, 'products': products})
