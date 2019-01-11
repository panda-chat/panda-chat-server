import uuid
from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True


class Message(BaseModel):
    sender_name = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    image = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.sender_name}: {self.content}"
