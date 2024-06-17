# routing.py

from django.urls import path
from . import person

websocket_urlpatterns = [
    path('ws/<str:room_name>/', person.Omboli_ChatPerson.as_asgi()),
]
