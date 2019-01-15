from django.urls import path
from .views import AddEventView, AdminInterface, HomePageView, DashboardView, EventDetailView, SuggestEventView, SuggestedEventListView, SuggestedEventDetailView, EventRegistrationView
from django.contrib.auth.decorators import permission_required

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('event_register/', EventRegistrationView.as_view(), name='event_register'),
    path('suggested_event/<int:pk>/', permission_required('is_staff')(SuggestedEventDetailView.as_view()),
         name='suggested_event_detail'),
    path('event/suggest/', SuggestEventView.as_view(), name='suggestevent'),
    path('event/suggested/', permission_required('is_staff')(SuggestedEventListView.as_view()),
         name='suggestedEventList'),
    path('event/new/', permission_required('is_staff')
         (AddEventView.as_view()), name='addevent'),
    path('admin_interface/', permission_required('is_staff')
         (AdminInterface.as_view()), name='admin_interface'),
]
