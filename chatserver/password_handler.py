"""
Passwords are hashed using hashlib.pbkdf2_hmac with SHA-256.
Hashed passwords are stored in the format iteration_count$salt$key.
"""

import os
import hashlib
import base64


hash_algo = "sha256"
split_char = "$"


def is_password_valid(password_hash, password_attempt):
    """Returns True iff the given password_attempt is a match."""

    (str_iteration_count, b64salt, b64key) = password_hash.split(split_char)

    return base64.b64decode(b64key) == hashlib.pbkdf2_hmac(
        hash_algo, password_attempt, base64.b64decode(b64salt), int(str_iteration_count)
    )


def generate_password_hash(password):
    """Generates a new hashed password. Uses 100000 iterations of SHA-256, as recommended here (https://docs.python.org/3/library/hashlib.html) as of 2019."""

    iteration_count = 100_000
    salt = os.urandom(20)
    key = hashlib.pbkdf2_hmac(hash_algo, password, salt, iteration_count)

    return f"{iteration_count}{split_char}{base64.b64encode(salt).decode('utf-8')}{split_char}{base64.b64encode(key).decode('utf-8')}"
