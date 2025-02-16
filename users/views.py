from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import CustomUserCreationForm
from .models import CustomUser


class RegisterView(FormView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('catalog:product_list')
    template_name = 'users/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис!'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        from_email = 'testdmitrynadelyaev@yandex.ru'
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)
