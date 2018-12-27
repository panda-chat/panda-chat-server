import uuid
import imghdr


def generate(byte_stream):
    file_extension = imghdr.what(byte_stream)
    return f"{uuid.uuid4()}.{file_extension}"
