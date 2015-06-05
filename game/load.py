__author__ = 'Su Lei'

import pyglet as pg
import random
import math
import physicalobject
from game import resources


def distance(point_1=(0, 0), point_2=(0, 0)):
    return math.sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2)


def asteroids(num_asteroids, player_position, batch=None):
    asteroids_array = []
    for i in xrange(num_asteroids):
        asteroid_x, asteroid_y = player_position
        while distance((asteroid_x, asteroid_y), player_position) < 100:
            asteroid_x = random.randint(0, 800)
            asteroid_y = random.randint(0, 600)
        new_asteroid = physicalobject.PhysicalObject(img=resources.asteroid_image, x=asteroid_x, y=asteroid_y,
                                                     batch=batch)
        new_asteroid.rotation = random.randint(0, 360)
        new_asteroid.velocity_x = random.random() * 40
        new_asteroid.velocity_y = random.random() * 40
        asteroids_array.append(new_asteroid)
    return asteroids_array


def player_lives(num_icons, batch=None):
    player_lives_a = []
    for i in xrange(num_icons):
        new_sprite = pg.sprite.Sprite(img=resources.play_image, x=785 - i * 30, y=585, batch=batch)
        new_sprite.scale = 0.5
        player_lives_a.append(new_sprite)
    return player_lives_a

