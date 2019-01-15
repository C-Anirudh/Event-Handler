from django.contrib import admin
from .models import EventDetails, SuggestedEvents, Registrants

admin.site.register(EventDetails)
admin.site.register(SuggestedEvents)
admin.site.register(Registrants)
