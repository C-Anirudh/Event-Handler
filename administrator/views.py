from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .models import EventDetails
from django.contrib.auth.mixins import LoginRequiredMixin


class AdminInterface(TemplateView):
    template_name = 'administrator.html'


class AddEventView(CreateView):
    model = EventDetails
    template_name = 'add_event.html'
    fields = '__all__'


class DashboardView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = EventDetails
    template_name = 'dashboard.html'
    context_object_name = 'events_list'


class HomePageView(TemplateView):
    template_name = 'home.html'


class EventDetailView(DetailView):
    model = EventDetails
    template_name = 'event_detail.html'
