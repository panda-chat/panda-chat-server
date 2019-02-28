from django.urls import path

from . import views

urlpatterns = [
    path("testclient/", views.index, name="index"),
    path("messages/", views.messages, name="messages"),
    path("create_account/", views.create_account_page, name="create_account_page"),
    path("create_account/create/", views.create_account, name="create_account"),
]
