__author__ = 'Su Lei'

import pyglet as pg
from game import resources, load


game_window = pg.window.Window(800, 600)
main_batch = pg.graphics.Batch()
score_label = pg.text.Label(text='Score: 0', x=10, y=575, batch=main_batch)
level_label = pg.text.Label(text='Game 1', x=400, y=575, anchor_x='center', batch=main_batch)
player_ship = pg.sprite.Sprite(img=resources.play_image, x=400, y=300)
asteroids = load.asteroids(3, player_ship.position, main_batch)
game_objects = asteroids


def update(dt):
    for obj in game_objects:
        obj.update(dt)


@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()
    # level_label.draw()
    # score_label.draw()


pg.clock.schedule_interval(update, 1 / 1000.0)
pg.app.run()
