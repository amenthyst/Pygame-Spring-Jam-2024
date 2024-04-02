import pygame

_last_keys: pygame.key.ScancodeWrapper


def update():
    global _last_keys
    _last_keys = get_pressed()


def get_pressed() -> pygame.key.ScancodeWrapper:
    return pygame.key.get_pressed()


def is_key_down(key: int) -> bool:
    keys = pygame.key.get_pressed()
    return keys[key]


def is_key_just_pressed(key: int) -> bool:
    return (not _last_keys[key]) and is_key_down(key)


def is_key_just_released(key: int) -> bool:
    return _last_keys[key] and (not is_key_down(key))


def is_key_held(key: int) -> bool:
    return _last_keys[key] and is_key_down(key)