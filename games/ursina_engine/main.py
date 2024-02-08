from ursina import *


app = Ursina()

player = Entity(model='quad', color=color.orange, scale=(1, 2), position=(0, 0))

def update():
    if held_keys['a']:
        player.x -= 1 * time.dt
    if held_keys['d']:
        player.x += 1 * time.dt
    if held_keys['w']:
        player.y += 1 * time.dt
    if held_keys['s']:
        player.y -= 1 * time.dt

app.run()