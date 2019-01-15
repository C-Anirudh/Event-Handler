from django.urls import path
from .views import SignUpView
from django.contrib.auth.decorators import permission_required

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]
