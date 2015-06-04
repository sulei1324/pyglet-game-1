__author__ = 'Su Lei'

import pyglet as pg

def center_image(image):
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2

pg.resource.path = ['./resources']
pg.resource.reindex()

play_image = pg.resource.image('player.png')
bullet_image = pg.resource.image('bullet.png')
asteroid_image = pg.resource.image('asteroid.png')
center_image(play_image)
center_image(bullet_image)
center_image(asteroid_image)

