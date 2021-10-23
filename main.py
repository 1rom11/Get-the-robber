def on_button_pressed_a():
    game.resume()
    player.turn(Direction.RIGHT, 90)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    game.pause()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    game.resume()
    player.turn(Direction.LEFT, 90)
input.on_button_pressed(Button.B, on_button_pressed_b)

player: game.LedSprite = None
player = game.create_sprite(2, 2)
food = game.create_sprite(randint(1, 5), randint(1, 5))
game.set_score(0)
game.set_life(3)

def on_forever():
    pass
basic.forever(on_forever)

def on_forever2():
    global food
    if player.is_touching(food):
        food.delete()
        food = game.create_sprite(randint(1, 5), randint(1, 5))
        game.add_score(1)
    player.move(1)
    basic.pause(500)
basic.forever(on_forever2)
