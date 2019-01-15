from django.views.generic import TemplateView, CreateView, ListView, DetailView, DeleteView
from .models import EventDetails, SuggestedEvents, Registrants
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


class EventDetailView(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = EventDetails
    template_name = 'event_detail.html'


class SuggestEventView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = SuggestedEvents
    template_name = 'suggest_event.html'
    fields = '__all__'


class SuggestedEventListView(ListView):
    model = SuggestedEvents
    template_name = 'suggested_event_list.html'
    context_object_name = 'suggested_events_list'


class SuggestedEventDetailView(DetailView):
    model = SuggestedEvents
    template_name = 'suggested_event_detail.html'


class EventRegistrationView(CreateView):
    model = Registrants
    fields = '__all__'
    template_name = 'event_register.html'


class EventParticipantsView(ListView):
    model = Registrants
    template_name = 'show_participants.html'
    context_object_name = 'members'


class EventDeleteView(DeleteView):
    model = EventDetails
    template_name = 'event_delete.html'
    success_url = reverse_lazy('dashboard')
