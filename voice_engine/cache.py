import hashlib
import os

CACHE_DIR = "cache/audio"


def get_cache_path(text, profile):

    key = text + str(profile)

    filename = hashlib.md5(key.encode()).hexdigest() + ".mp3"

    return os.path.join(CACHE_DIR, filename)


def exists(text, profile):

    return os.path.exists(get_cache_path(text, profile))


def get(text, profile):

    return get_cache_path(text, profile)


def save(text, profile):

    return get_cache_path(text, profile)