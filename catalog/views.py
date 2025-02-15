from catalog.forms import ProductForm, ContactForm
from catalog.models import Product, Contact
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ContactListView(ListView):
    model = Contact


class ContactDetailView(DetailView):
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
