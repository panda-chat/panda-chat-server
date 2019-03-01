from django.core.exceptions import ValidationError
from django.http import JsonResponse, HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from .models import Message, User, CreationKey, AuthToken
from .json_formatter import to_text_json_object, to_image_json_object
from .password_handler import is_password_valid, generate_password_hash


def messages(request):
    quantity = int(request.GET.get("quantity") or 100)
    before_id = request.GET.get("before_id")

    messages = Message.objects.order_by("-created")
    if before_id != None:
        before_time = Message.objects.get(id=before_id).created
        messages = messages.filter(created__lte=before_time).exclude(id=before_id)

    return JsonResponse(
        [
            to_text_json_object(
                msg.content, id=msg.id, sender=msg.sender_name, time=msg.created
            )
            if not msg.image
            else to_image_json_object(
                msg.image, id=msg.id, sender=msg.sender_name, time=msg.created
            )
            for msg in messages[:quantity]
        ],
        safe=False,
    )


def login(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = User.objects.get(username=username)
    assert is_password_valid(user.password_hash, password)

    auth_token = AuthToken(user=user)
    auth_token.save()

    return JsonResponse({"auth_token": auth_token.id})


def create_account_page(request):
    return render(request, "create_account/index.html")


def create_account(request):
    creation_key_id = request.POST.get("creation_key")
    username = request.POST.get("username")
    password = request.POST.get("password")

    try:
        creation_key = CreationKey.objects.get(id=creation_key_id)
    except (CreationKey.DoesNotExist, ValidationError):
        return HttpResponseForbidden("Invalid creation key.")  # 403 Forbidden

    new_user = User(username=username, password_hash=generate_password_hash(password))
    new_user.save()
    creation_key.delete()

    return HttpResponse("Success.")  # 200 OK
