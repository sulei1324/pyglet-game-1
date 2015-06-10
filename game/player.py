__author__ = 'Su Lei'

import physicalobject
import resources
from pyglet.window import key
import math
import pyglet as pg

class Player(physicalobject.PhysicalObject):
    def __init__(self, *args, **kargs):
        super(Player, self).__init__(img=resources.play_image, *args, **kargs)
        self.thrust = 300.0
        self.rotate_speed = 200.0
        self.key_handler = key.KeyStateHandler()
        self.engine_sprite = pg.sprite.Sprite(img=resources.engine_image, *args, **kargs)
        self.engine_sprite.visible = False

    def update(self, dt):
        super(Player, self).update(dt)

        if self.key_handler[key.LEFT]:
            self.rotation -= self.rotate_speed * dt
        if self.key_handler[key.RIGHT]:
            self.rotation += self.rotate_speed * dt
        if self.key_handler[key.UP]:
            angle_radians = - math.radians(self.rotation)
            force_x = math.cos(angle_radians) * self.thrust * dt
            force_y = math.sin(angle_radians) * self.thrust * dt
            self.velocity_x += force_x
            self.velocity_y += force_y
            self.engine_sprite.visible = True
            self.engine_sprite.rotation = self.rotation
            self.engine_sprite.x = self.x
            self.engine_sprite.y = self.y
        else:
            self.engine_sprite.visible = False

    def delete(self):
        self.engine_sprite.delete()
        super(Player, self).delete()

    # def on_key_press(self, symbol, modifiers):
    #     if symbol is key.UP:
    #         self.keys['up'] = True
    #     elif symbol is key.LEFT:
    #         self.keys['left'] = True
    #     elif symbol is key.RIGHT:
    #         self.keys['right'] = True
    #
    # def on_key_release(self, symbol, modifiers):
    #     if symbol is key.UP:
    #         self.keys['up'] = False
    #     elif symbol is key.LEFT:
    #         self.keys['right'] = False
    #     elif symbol is key.RIGHT:
    #         self.keys['right'] = False