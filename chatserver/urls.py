from django.urls import path

from . import views

urlpatterns = [
    path(
        "testclient/", views.index, name="index"
    ),
    path("messages/", views.messages, name="messages"),
]
