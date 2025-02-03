from django.shortcuts import render, redirect
from catalog.models import Product, Contact


def home(request):
    #   Выборка последних 5 созданных продуктов
    latest_products = Product.objects.order_by('-created_at')[:5]

    #   Вывод в консоль
    for product in latest_products:
        print(f'Продукт: {product.product_name}, Цена: {product.price}, Категория: {product.category}')

    return render(request, 'home.html', {'latest_products': latest_products})


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        Contact.objects.create(name=name, email=email, message=message)

        print(f'Вам сообщение с вашего веб-магазина: {name}, {email}, {message}')

        return redirect('catalog:contact')

    contact = Contact.objects.all()

    return render(request, 'contact.html', {'contacts': contact})
