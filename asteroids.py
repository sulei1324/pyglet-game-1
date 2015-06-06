__author__ = 'Su Lei'

import pyglet as pg
from game import resources, load, player


game_window = pg.window.Window(800, 600)
main_batch = pg.graphics.Batch()
score_label = pg.text.Label(text='Score: 0', x=10, y=575, batch=main_batch, font_size=32,
                            font_name='Arial', color=(255, 0, 0, 255))
level_label = pg.text.Label(text='Game 1', x=400, y=575, anchor_x='center', batch=main_batch)
player_ship = player.Player(x=400, y=300, batch=main_batch)
asteroids = load.asteroids(3, player_ship.position, main_batch)
game_objects = asteroids + [player_ship]
game_window.push_handlers(player_ship.key_handler)

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
