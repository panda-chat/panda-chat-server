import uuid
from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True


class Client(BaseModel):
    user_name = models.CharField(max_length=200)
    address = models.GenericIPAddressField()

    def __str__(self):
        return f"{self.user_name} ({self.address})"


class Message(BaseModel):
    sender = models.ForeignKey(Client, on_delete=models.PROTECT)
    content = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="static/user_images/", blank=True)

    def __str__(self):
        return f"{self.sender}: {self.content}"
