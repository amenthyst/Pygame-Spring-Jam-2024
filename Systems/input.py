from typing import overload

import pygame

_last_keys: pygame.key.ScancodeWrapper


def update():
    global _last_keys
    _last_keys = get_pressed()


def get_pressed() -> pygame.key.ScancodeWrapper:
    return pygame.key.get_pressed()


def is_key_down(key: int) -> bool:
    return get_pressed()[key]


def is_key_just_pressed(key: int) -> bool:
    return (not _last_keys[key]) and is_key_down(key)


def is_key_just_released(key: int) -> bool:
    return _last_keys[key] and (not is_key_down(key))


def is_key_held(key: int) -> bool:
    return _last_keys[key] and is_key_down(key)


def get_vector(neg_x, pos_x, neg_y, pos_y) -> pygame.math.Vector2:
    vector = pygame.math.Vector2(0, 0)
    keys = get_pressed()
    if keys[neg_x]:
        vector.x -= 1
    if keys[pos_x]:
        vector.x += 1
    if keys[neg_y]:
        vector.y -= 1
    if keys[pos_y]:
        vector.y += 1
    return vector


def get_pos() -> pygame.math.Vector2:
    return pygame.math.Vector2(pygame.mouse.get_pos())


def get_pressed_mouse() -> tuple[bool, bool, bool]:
    return pygame.mouse.get_pressed()


def l_pressed() -> bool:
    return get_pressed_mouse()[0]


def r_pressed() -> bool:
    return get_pressed_mouse()[1]
