import io
from channels.generic.websocket import WebsocketConsumer
from .models import Client
from .json_formatter import to_text_json as format_text, to_image_json as format_image
from .image_random_filename_generator import generate as generate_filename
from .broadcaster import broadcast, register, unregister


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        address = self.scope["client"][0]
        try:
            self.user = Client.objects.get(address=address)
        except Client.DoesNotExist:
            self.user = Client(user_name=None, address=address)

        self.accept()
        if self.user.user_name == None:
            self.send(text_data=format_text("What is your name?"))
        else:
            register(self, format_text(f"{self.user.user_name} connected."))

    def receive(self, *, text_data=None, bytes_data=None):
        if self.user.user_name == None:
            self.receive_first_message(text_data)
        elif text_data != None:
            self.receive_text(text_data)
        else:
            self.receive_image(bytes_data)

    def receive_first_message(self, text_data):
        if text_data != None:
            self.user.user_name = text_data
            self.user.save()
            register(self, format_text(f"{self.user.user_name} joined the chat."))

        else:
            self.send(text_data=format_text("First, what is your name?"))

    def receive_text(self, text_data):
        new_message = self.user.message_set.create(content=text_data)
        broadcast(
            format_text(
                new_message.content,
                id=new_message.id,
                sender=self.user.user_name,
                time=new_message.created,
            )
        )

    def receive_image(self, bytes_data):
        new_message = self.user.message_set.create(content="")
        img_byte_stream = io.BytesIO(bytes_data)
        new_message.image.save(generate_filename(img_byte_stream), img_byte_stream)
        broadcast(
            format_image(
                new_message.image,
                id=new_message.id,
                sender=self.user.user_name,
                time=new_message.created,
            )
        )

    def disconnect(self, close_code):
        unregister(self, format_text(f"{self.user.user_name} disconnected."))
