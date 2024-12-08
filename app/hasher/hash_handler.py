import hashlib


def encode_data(data: str):
    sha1 = hashlib.sha1()
    sha1.update(data.encode("utf-8"))
    return sha1.hexdigest()

