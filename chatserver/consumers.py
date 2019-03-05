import io
import uuid
from django.core.exceptions import ValidationError
from channels.generic.websocket import WebsocketConsumer
from .models import Message, AuthToken, User
from .json_formatter import (
    to_text_json as format_text,
    to_image_json as format_image,
    to_code_json as format_code,
)
from .image_random_filename_generator import generate as generate_filename
from .broadcaster import broadcast, register, unregister


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        user = self.__get_session_user()
        if user != None:
            register(self)
            self.send(text_data=format_code("AUTH_SUCCESS"))
        else:
            self.send(text_data=format_code("AUTH_REQUEST"))

    def receive(self, *, text_data=None, bytes_data=None):
        user = self.__get_session_user()
        if user == None:
            self.receive_first_message(text_data)
        elif text_data != None:
            self.receive_text(text_data, user)
        else:
            self.receive_image(bytes_data, user)

    def receive_first_message(self, text_data):
        try:
            user = self.__start_user_session(AuthToken.objects.get(id=text_data))
            register(self)
            self.send(text_data=format_code("AUTH_SUCCESS"))
        except (AuthToken.DoesNotExist, ValidationError):
            self.send(text_data=format_code("INVALID_AUTH_TOKEN"))

    def receive_text(self, text_data, user):
        new_message = Message(content=text_data, sender=user)
        new_message.save()
        broadcast(
            format_text(
                new_message.content,
                id=new_message.id,
                sender=user.username,
                time=new_message.created,
            )
        )

    def receive_image(self, bytes_data, user):
        new_message = Message(content="", sender=user)
        new_message.save()
        img_byte_stream = io.BytesIO(bytes_data)
        new_message.image.save(generate_filename(img_byte_stream), img_byte_stream)
        broadcast(
            format_image(
                new_message.image,
                id=new_message.id,
                sender=user.username,
                time=new_message.created,
            )
        )

    def disconnect(self, close_code):
        user = self.__get_session_user()
        if user != None:
            unregister(self)

    def __start_user_session(self, auth_token):
        self.scope["session"]["user_id"] = str(auth_token.user.id)
        self.scope["session"].save()
        return auth_token.user

    def __get_session_user(self):
        return (
            User.objects.get(id=uuid.UUID(self.scope["session"]["user_id"]))
            if "user_id" in self.scope["session"]
            else None
        )
