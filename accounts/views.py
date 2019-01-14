from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from .models import EventDetails


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class AddEventView(CreateView):
    model = EventDetails
    template_name = 'add_event.html'
    fields = '__all__'
