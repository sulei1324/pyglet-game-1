__author__ = 'Su Lei'

import pyglet
import physicalobject, resources
from pyglet.window import key
import math

class Bullet(physicalobject.PhysicalObject):
    def __init__(self, *args, **kargs):
        super(Bullet, self).__init__(resources.bullet_image, *args, **kargs)
        pyglet.clock.schedule_once(self.die, 0.5)


    def die(self, dt):
        self.dead = True


