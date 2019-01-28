import pygame
import pyganim
from data import Settings, Globals

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__ (self)
        # self.image = pygame.transform.scale(pygame.image.load('assets/player.png'), (75, 75))
        # self.rect = self.image.get_rect()
        # self.rect = self.rect.inflate(-15, -15)
        # self.rect.size = (50, 50)
        self.player_animations = {}
        if Globals.player_char == 'lucca':
            self.player_animations['idle'] = pyganim.PygAnimation('assets/sprites/lucca/idle.gif', 50)
            self.player_animations['walk_down'] = pyganim.PygAnimation('assets/sprites/lucca/walk_down.gif', 50)
            self.player_animations['walk_up'] = pyganim.PygAnimation('assets/sprites/lucca/walk_up.gif', 50)
            self.player_animations['walk_left'] = pyganim.PygAnimation('assets/sprites/lucca/walk_left.gif', 50)
            self.player_animations['walk_right'] = self.player_animations['walk_left'].getCopy()
            self.player_animations['walk_right'].flip(True, False)
            self.player_animations['walk_right'].makeTransformsPermanent()
        if Globals.player_char == 'frog':
            self.player_animations['idle'] = pyganim.PygAnimation('assets/sprites/frog/idle.gif', 50)
            self.player_animations['walk_down'] = pyganim.PygAnimation('assets/sprites/frog/walk_down.gif', 50)
            self.player_animations['walk_up'] = pyganim.PygAnimation('assets/sprites/frog/walk_up.gif', 50)
            self.player_animations['walk_left'] = pyganim.PygAnimation('assets/sprites/frog/walk_left.gif', 50)
            self.player_animations['walk_right'] = self.player_animations['walk_left'].getCopy()
            self.player_animations['walk_right'].flip(True, False)
            self.player_animations['walk_right'].makeTransformsPermanent()

        for key in self.player_animations.keys():
            self.player_animations[key].scale((58, 84))
            self.player_animations[key].makeTransformsPermanent()
        self.move_conductor = pyganim.PygConductor(self.player_animations)

        self.image = self.player_animations['idle']
        self.rect = pygame.Rect((0, 0), (58, 84))
        self.rect.centerx = Settings.WIDTH / 2
        self.rect.bottom = Settings.HEIGHT - 10
        self.max_speed = Settings.PLAYER_SPEED

    def update(self):
        self.hidden = False
        self.move_conductor.play()

        self.target = Globals.MOUSE_X, Globals.MOUSE_Y

        if self.rect.centerx > self.target[0]:
            self.image = self.player_animations['walk_left']
            if self.rect.centerx - self.max_speed >= 30:
                if self.rect.centerx - self.target[0] < self.max_speed:
                    self.rect.centerx -= self.rect.centerx - self.target[0]
                else:
                    self.rect.centerx -= self.max_speed
        elif self.rect.centerx < self.target[0]:
            self.image = self.player_animations['walk_right']
            if self.rect.centerx + self.max_speed <= Settings.WIDTH - 30:
                if self.target[0] - self.rect.centerx < self.max_speed:
                    self.rect.centerx += self.target[0] - self.rect.centerx
                else:
                    self.rect.centerx += self.max_speed

        if self.rect.centery > self.target[1]:
            self.image = self.player_animations['walk_up']
            if self.rect.centery - self.max_speed >= Settings.HEIGHT - 250:
                if self.rect.centery - self.target[1] < self.max_speed:
                    self.rect.centery -= self.rect.centery - self.target[1]
                else:
                    self.rect.centery -= self.max_speed
        elif self.rect.centery < self.target[1]:
            self.image = self.player_animations['walk_down']
            if self.rect.centery + self.max_speed <= Settings.HEIGHT - 30:
                if self.target[1] - self.rect.centery < self.max_speed:
                    self.rect.centery += self.target[1] - self.rect.centery
                else:
                    self.rect.centery += self.max_speed

        # IDLE IS FUCKING WITH ME
        # if self.rect.centery == self.target[1] and self.rect.centerx == self.target[0]:
        #     self.image = self.player_animations['idle']

        # if Globals.MOUSE_X > Settings.WIDTH - (self.rect.width / 2):
        #     self.rect.right = Settings.WIDTH
        # elif Globals.MOUSE_X < (self.rect.width / 2):
        #     self.rect.left = 0
        # else:
        #     self.rect.centerx = Globals.MOUSE_X
        #
        # if Globals.MOUSE_Y < Settings.HEIGHT - 250 + (self.rect.height / 2):
        #     self.rect.top = Settings.HEIGHT - 250
        # elif Settings.HEIGHT - (self.rect.width / 2) < Globals.MOUSE_Y:
        #     self.rect.bottom = Settings.HEIGHT
        # else:
        #     self.rect.centery = Globals.MOUSE_Y

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.transform.scale(pygame.image.load('assets/enemy.png'), (75, 75))
        # self.rect = self.image.get_rect()
        # self.rect = self.rect.inflate(-15, -15)

        self.enemy_animations = {}
        self.enemy_animations['idle'] = pyganim.PygAnimation('assets/sprites/magus/idle.gif', 50)
        self.enemy_animations['walk_down'] = pyganim.PygAnimation('assets/sprites/magus/walk_down.gif', 50)
        self.enemy_animations['walk_up'] = pyganim.PygAnimation('assets/sprites/magus/walk_up.gif', 50)
        self.enemy_animations['walk_left'] = pyganim.PygAnimation('assets/sprites/magus/walk_left.gif', 50)
        self.enemy_animations['walk_right'] = self.enemy_animations['walk_left'].getCopy()
        self.enemy_animations['walk_right'].flip(True, False)
        self.enemy_animations['walk_right'].makeTransformsPermanent()
        self.move_conductor = pyganim.PygConductor(self.enemy_animations)

        for key in self.enemy_animations.keys():
            self.enemy_animations[key].scale((58, 84))
            self.enemy_animations[key].makeTransformsPermanent()

        self.image = self.enemy_animations['idle']
        self.rect = pygame.Rect((0, 0), (58, 84))

        self.rect.centerx = Settings.WIDTH / 2
        self.rect.top = 45
        self.max_speed = Settings.ENEMY_SPEED

    def update(self):
        self.hidden = False
        self.target = Globals.BALL_X
        self.move_conductor.play()

        if self.rect.centerx > self.target + self.max_speed:
            self.image = self.enemy_animations['walk_left']
            if self.rect.centerx - self.max_speed >= 30:
                self.rect.centerx -= self.max_speed
        elif self.rect.centerx < self.target - self.max_speed:
            self.image = self.enemy_animations['walk_right']
            if self.rect.centerx + self.max_speed <= Settings.WIDTH - 30:
                self.rect.centerx += self.max_speed
        if self.target - 0.5 < self.rect.centerx < self.target + 0.5:
            self.image = self.enemy_animations['idle']


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        anim_ball = pyganim.PygAnimation('assets/sprites/ball.gif', 50)
        move_conductor = pyganim.PygConductor(anim_ball)
        move_conductor.play()
        self.image = anim_ball
        self.rect = pygame.Rect((0, 0), (36, 40))
        self.rect.centerx = Settings.WIDTH / 2
        self.rect.bottom = Settings.HEIGHT / 2
        self.speed = [0, Settings.BALL_SPEED]


    def update(self):
        self.hidden = False

        self.rect.x = self.rect.x + self.speed[0]
        self.rect.y = self.rect.y + self.speed[1]

        if self.rect.x >= Settings.WIDTH - Settings.PADDING - self.rect.width or self.rect.x <= 0 + Settings.PADDING:
            self.speed[0] *= -1
            self.rect.x = self.rect.x + self.speed[0] * 2
        if self.rect.y >= Settings.HEIGHT - self.rect.height + 15 or self.rect.y <= -15:
            self.speed[1] *= -1
            self.rect.y = self.rect.y + self.speed[1] * 2

        Globals.BALL_X = self.rect.centerx

class Goal(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('assets/sprites/goal_t.png'), (192, 32))
        self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-40, -8)
        self.rect.centerx = Settings.WIDTH / 2 - 5
        self.rect.top = -10

    def update(self):
        self.hidden = False

class Enemy_Goal(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('assets/sprites/goal2_t.png'), (192, 32))
        self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-40, -8)
        self.rect.centerx = Settings.WIDTH / 2 - 5
        self.rect.bottom = Settings.HEIGHT + 10

    def update(self):
        self.hidden = False


class MyGroup(pygame.sprite.Group):
    def __init__(self):
        pygame.sprite.Group.__init__(self)

    def draw(self, surface):
        sprites = self.sprites()
        surface_blit = surface.blit
        for spr in sprites:
            if isinstance(spr.image, pyganim.PygAnimation):
                self.spritedict[spr] = spr.image.blit(surface, spr.rect)
            else:
                self.spritedict[spr] = surface_blit(spr.image, spr.rect)
        self.lostsprites = []