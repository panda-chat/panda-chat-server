from django.urls import path

from . import views

urlpatterns = [
    path("messages/", views.messages, name="messages"),
    path("login/", views.login, name="login"),
    path("create_account/", views.create_account_page, name="create_account_page"),
    path("create_account/create/", views.create_account, name="create_account"),
]
