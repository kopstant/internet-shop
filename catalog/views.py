from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        print(f'Вам сообщение с вашего веб-магазина: {name}, {email}, {message}')
    return render(request, 'contact.html')
