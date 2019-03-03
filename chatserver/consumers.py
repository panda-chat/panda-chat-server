import io
from django.core.exceptions import ValidationError
from channels.generic.websocket import WebsocketConsumer
from .models import Message, AuthToken, User
from .json_formatter import (
    to_text_json as format_text,
    to_image_json as format_image,
    to_error_json as format_error,
)
from .image_random_filename_generator import generate as generate_filename
from .broadcaster import broadcast, register, unregister


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        if "user" in self.scope["session"]:
            register(
                self, format_text(f"{self.scope['session']['username']} connected.")
            )

    def receive(self, *, text_data=None, bytes_data=None):
        if "user" not in self.scope["session"]:
            self.receive_first_message(text_data)
        elif text_data != None:
            self.receive_text(text_data)
        else:
            self.receive_image(bytes_data)

    def receive_first_message(self, text_data):
        try:
            auth_token = AuthToken.objects.get(id=text_data)

            self.scope["session"]["user"] = auth_token.user
            self.scope["session"].save()
            register(
                self,
                format_text(
                    f"{self.scope['session']['user'].username} joined the chat."
                ),
            )
        except (AuthToken.DoesNotExist, ValidationError):
            self.send(text_data=format_error("INVALID_AUTH_TOKEN"))

    def receive_text(self, text_data):
        new_message = Message(content=text_data, sender=self.scope["session"]["user"])
        new_message.save()
        broadcast(
            format_text(
                new_message.content,
                id=new_message.id,
                sender=self.scope["session"]["user"].username,
                time=new_message.created,
            )
        )

    def receive_image(self, bytes_data):
        new_message = Message(content="", sender=self.scope["session"]["user"])
        new_message.save()
        img_byte_stream = io.BytesIO(bytes_data)
        new_message.image.save(generate_filename(img_byte_stream), img_byte_stream)
        broadcast(
            format_image(
                new_message.image,
                id=new_message.id,
                sender=self.scope["session"]["user"].username,
                time=new_message.created,
            )
        )

    def disconnect(self, close_code):
        if "user" in self.scope["session"]:
            unregister(
                self,
                format_text(f"{self.scope['session']['user'].username} disconnected."),
            )
