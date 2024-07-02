from django.urls import path
from .views import visitor_greeting

urlpatterns = [
   path('api/hello/', visitor_greeting, name='hello'),
]
