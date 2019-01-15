from django.urls import path
from .views import AddEventView, AdminInterface, HomePageView, DashboardView
from django.contrib.auth.decorators import permission_required

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('event/new/', permission_required('is_staff')
         (AddEventView.as_view()), name='addevent'),
    path('admin_interface/', permission_required('is_staff')
         (AdminInterface.as_view()), name='admin_interface'),
]
