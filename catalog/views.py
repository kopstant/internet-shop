from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from catalog.models import Product, Contact
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    # Получаем все товары
    products_list = Product.objects.all().order_by('-created_at')

    # Настройка пагинации
    paginator = Paginator(products_list, 10)  # 10 товаров на страницу
    page_number = request.GET.get('page')  # Получаем номер страницы из запроса

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        # Если page_number не является целым числом, показываем первую страницу
        products = paginator.page(1)
    except EmptyPage:
        # Если page_number выходит за пределы диапазона, показываем последнюю страницу
        products = paginator.page(paginator.num_pages)

    context = {
        'products': products,
    }

    return render(request, 'home.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        if name and email and message:
            Contact.objects.create(name=name, email=email, message=message)
            print(f'Вам сообщение с вашего веб-магазина: {name}, {email}, {message}')
            return redirect('catalog:contact')
        else:
            print('Не все поля заполнены')

    contacts = Contact.objects.all()
    return render(request, 'contact.html', {'contacts': contacts})


def description(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        "product": product,
    }
    return render(request, 'description.html', context)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'price', 'category', 'preview']


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:home')
    else:
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'add_product.html', context)
