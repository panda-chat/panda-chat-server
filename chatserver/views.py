from django.http import JsonResponse
from django.shortcuts import render
from .models import Message
from .json_formatter import to_json_object


def index(request):
    return render(request, "test_client/index.html")


def messages(request):
    quantity = int(request.GET.get("quantity") or 100)
    before_id = request.GET.get("before_id")

    messages = Message.objects.order_by("-created")
    if before_id != None:
        before_time = Message.objects.get(id=before_id).created
        messages = messages.filter(created__lte=before_time).exclude(id=before_id)

    return JsonResponse(
        [
            to_json_object(
                msg.content, id=msg.id, sender_id=msg.sender_id, time=msg.created
            )
            for msg in messages[:quantity]
        ],
        safe=False,
    )
