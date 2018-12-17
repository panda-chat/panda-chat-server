from django.db import models


class Client(models.Model):
    user_name = models.CharField(max_length=200)
    address = models.GenericIPAddressField()

    def __str__(self):
        return f"{self.user_name} ({self.address})"


class Message(models.Model):
    sender = models.ForeignKey(Client, on_delete=models.PROTECT)
    content = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}: {self.content}"
