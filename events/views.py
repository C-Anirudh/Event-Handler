from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import EventDetails


class DashboardView(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = EventDetails
    template_name = 'dashboard.html'
    context_object_name = 'events_list'


class HomePageView(TemplateView):
    template_name = 'home.html'
