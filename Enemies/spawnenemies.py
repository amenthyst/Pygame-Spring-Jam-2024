import pygame
from enum import Enum
import random
from Enemies.basher import Basher
from Enemies.shooter import Shooter
import images
from Objects.player import Player
class EnemyChance(Enum):
    BASHER = [1,2,3,4,5,6,7,8,9,10,11,12]
    SHOOTER = [13,14,15]
    #SUPPORT = [11,12]
    #THROWER = [13,14,15]


def patterns(nums: int):
    pattern = []
    for i in range(nums):
        data = []
        chance = random.randint(1,15)
        for obj in EnemyChance:
            if chance in obj.value:
                data.append(obj.name)

        pos = (random.randint(-300,1300), random.randint(-300, 900))

        data.append(pos)
        pattern.append(data)
    return pattern

def spawnenemies(enemygrp: pygame.sprite.Group, nums: int, bulletgrp):
    # dont like this but the pos is needed from pattern
    pattern = patterns(nums)
    for item in pattern:
        enemydict = {"BASHER": Basher(item[1], 3, 3, 10, (30,30), Player.Instance.state, bulletgrp),
                     "SHOOTER": Shooter(item[1], 6, 2, 10, (75,50),  Player.Instance.state, bulletgrp)}
        enemygrp.add(enemydict[item[0]])




