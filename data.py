import pyganim

class Colors():
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

class Settings():
    WIDTH = 450
    HEIGHT = 700
    PADDING = 10
    FPS = 60
    BALL_STARTING_SPEED = 6
    BALL_MAX_SPEED = 20
    BALL_SPEED = 6
    PLAYER_SPEED = 12
    ENEMY_SPEED = 10


class Globals():
    MOUSE_X = 0
    MOUSE_Y = 0
    BALL_X = 0
    player_char = ''

class Lucca():
    player_animations = {}
    player_animations['idle'] = pyganim.PygAnimation('assets/sprites/lucca/idle.gif', 50)
    player_animations['walk_down'] = pyganim.PygAnimation('assets/sprites/lucca/walk_down.gif', 50)
    player_animations['walk_up'] = pyganim.PygAnimation('assets/sprites/lucca/walk_up.gif', 50)
    player_animations['walk_left'] = pyganim.PygAnimation('assets/sprites/lucca/walk_left.gif', 50)
    player_animations['walk_right'] = player_animations['walk_left'].getCopy()
    player_animations['walk_right'].flip(True, False)
    player_animations['walk_right'].makeTransformsPermanent()
    for key in player_animations.keys():
        player_animations[key].scale((58, 84))
        player_animations[key].makeTransformsPermanent()