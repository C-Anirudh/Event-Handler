from django.urls import path
from .views import SignUpView, AddEventView
from django.contrib.auth.decorators import permission_required

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('event/new/', permission_required('is_staff')
         (AddEventView.as_view()), name='addevent'),
]
