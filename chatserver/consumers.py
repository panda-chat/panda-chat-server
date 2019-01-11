import io
from channels.generic.websocket import WebsocketConsumer
from .models import Message
from .json_formatter import to_text_json as format_text, to_image_json as format_image
from .image_random_filename_generator import generate as generate_filename
from .broadcaster import broadcast, register, unregister


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        if "username" not in self.scope["session"]:
            self.send(text_data=format_text("What is your name?"))
        else:
            register(
                self, format_text(f"{self.scope['session']['username']} connected.")
            )

    def receive(self, *, text_data=None, bytes_data=None):
        if "username" not in self.scope["session"]:
            self.receive_first_message(text_data)
        elif text_data != None:
            self.receive_text(text_data)
        else:
            self.receive_image(bytes_data)

    def receive_first_message(self, text_data):
        if text_data != None:
            self.scope["session"]["username"] = text_data
            self.scope["session"].save()
            register(
                self,
                format_text(f"{self.scope['session']['username']} joined the chat."),
            )

        else:
            self.send(text_data=format_text("First, what is your name?"))

    def receive_text(self, text_data):
        new_message = Message(
            content=text_data, sender_name=self.scope["session"]["username"]
        )
        new_message.save()
        broadcast(
            format_text(
                new_message.content,
                id=new_message.id,
                sender=self.scope["session"]["username"],
                time=new_message.created,
            )
        )

    def receive_image(self, bytes_data):
        new_message = Message(content="", sender_name=self.scope["session"]["username"])
        new_message.save()
        img_byte_stream = io.BytesIO(bytes_data)
        new_message.image.save(generate_filename(img_byte_stream), img_byte_stream)
        broadcast(
            format_image(
                new_message.image,
                id=new_message.id,
                sender=self.scope["session"]["username"],
                time=new_message.created,
            )
        )

    def disconnect(self, close_code):
        if "username" in self.scope["session"]:
            unregister(
                self, format_text(f"{self.scope['session']['username']} disconnected.")
            )
