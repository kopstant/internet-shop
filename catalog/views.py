from itertools import product

from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect

from catalog.forms import ProductForm, ContactForm, ModeratorProductForm
from catalog.models import Product, Contact
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductListView(LoginRequiredMixin, ListView):
    model = Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.add_product'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.change_product'

    def get_form_class(self):
        user = self.request.user
        product = self.get_object()

        # Если пользователь - владелец, разрешаем полное редактирование
        if user == product.owner:
            return ProductForm

        # Если пользователь - модератор, разрешаем редактирование только для флага публикации.
        if user.has_perm('catalog.can_unpublish_product') and user.has_perm('catalog.delete_product'):
            return ModeratorProductForm

        # Во всех остальных случаях запрещаем доступ.
        raise PermissionDenied

    def form_valid(self, form):
        user = self.request.user

        # Проверка прав на отмену публикации
        if 'publications_flag' in form.changed_data and not user.has_perm('catalog.can_unpublish_product'):
            raise PermissionDenied("У вас нет прав на отмену публикации продукта.")
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.delete_product'

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()
        user = self.request.user

        # Проверка прав на удаление продукта
        if user != product.owner and not user.has_perm('catalog.delete_product'):
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
