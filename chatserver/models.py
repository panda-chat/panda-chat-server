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


class User(BaseModel):
    username = models.CharField(max_length=200)

    # Why max_length = 82 for password_hash:
    #
    #   Password hashes are stored in the format "iteration_count$salt$key".
    #
    #   The salt is 20 bytes, converted to a base 64 string, which is 28 characters long.
    #     It's 28 characters long because (20 bytes * 8 bits/byte) / (6 bits/base64 char) = 26.667 base64 chars,
    #     and 26.667 rounded up to the nearest multiple of 4 is 28.
    #
    #   The key is 32 bytes (the hash digest size of SHA-256), which is 44 characters when converted to a base 64 string.
    #     (32 bytes * 8 bits/byte) / (6 bits/base64 char) = 42.667 base64 chars,
    #     and 42.667 rounded up to the nearest multiple of 4 is 44.
    #
    #   The current NIST recommendation for iteration count for "especially critical keys" is 10000000 (8 characters).
    #   We are not using anywhere close to 10000000 iterations, but this gives us a reasonable maximum.
    #
    #   8 + 1 + 28 + 1 + 44 = 82
    password_hash = models.CharField(max_length=82)


class CreationKey(BaseModel):
    pass


class AuthToken(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
