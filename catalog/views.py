from django.shortcuts import render, redirect, get_object_or_404
from catalog.models import Product, Contact


def home(request):
    #   Выборка последних 5 созданных продуктов
    latest_products = Product.objects.order_by('-created_at')[:5]
    products = Product.objects.all()

    context = {
        'products': products,
        'latest_products': latest_products,
        'pk': latest_products[0].pk if latest_products else None,
                    }

    #   Вывод в консоль
    for product in latest_products:
        print(f'Продукт: {product.product_name}, Цена: {product.price}, Категория: {product.category}')

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
