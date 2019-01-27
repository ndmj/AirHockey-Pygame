import pygame

from data import Settings, Globals

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__ (self)
        self.image = pygame.transform.scale(pygame.image.load('assets/player.png'), (75, 75))
        self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-15, -15)
        # self.rect.size = (50, 50)
        self.rect.centerx = Settings.WIDTH / 2
        self.rect.bottom = Settings.HEIGHT - 10
        self.max_speed = Settings.PLAYER_SPEED

    def update(self):
        self.hidden = False

        self.target = Globals.MOUSE_X, Globals.MOUSE_Y

        if self.rect.centerx > self.target[0]:
            if self.rect.centerx - self.max_speed >= 30:
                if self.rect.centerx - self.target[0] < self.max_speed:
                    self.rect.centerx -= self.rect.centerx - self.target[0]
                else:
                    self.rect.centerx -= self.max_speed
        elif self.rect.centerx < self.target[0]:
            if self.rect.centerx + self.max_speed <= Settings.WIDTH - 30:
                if self.target[0] - self.rect.centerx < self.max_speed:
                    self.rect.centerx += self.target[0] - self.rect.centerx
                else:
                    self.rect.centerx += self.max_speed

        if self.rect.centery > self.target[1]:
            if self.rect.centery - self.max_speed >= Settings.HEIGHT - 250:
                if self.rect.centery - self.target[1] < self.max_speed:
                    self.rect.centery -= self.rect.centery - self.target[1]
                else:
                    self.rect.centery -= self.max_speed
        elif self.rect.centery < self.target[1]:
            if self.rect.centery + self.max_speed <= Settings.HEIGHT - 30:
                if self.target[1] - self.rect.centery < self.max_speed:
                    self.rect.centery += self.target[1] - self.rect.centery
                else:
                    self.rect.centery += self.max_speed

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
        self.image = pygame.transform.scale(pygame.image.load('assets/enemy.png'), (75, 75))
        self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-15, -15)
        self.rect.centerx = Settings.WIDTH / 2
        self.rect.top = 45
        self.max_speed = 4

    def update(self):
        self.hidden = False
        self.target = Globals.BALL_X

        if self.rect.centerx > self.target:
            if self.rect.centerx - self.max_speed >= 30:
                self.rect.centerx -= self.max_speed
        elif self.rect.centerx < self.target:
            if self.rect.centerx + self.max_speed <= Settings.WIDTH - 30:
                self.rect.centerx += self.max_speed


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('assets/ball.png'), (25, 25))
        self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-6, -6)
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
        if self.rect.y >= Settings.HEIGHT + 5 - self.rect.height or self.rect.y <= -5:
            self.speed[1] *= -1
            self.rect.y = self.rect.y + self.speed[1] * 2

        Globals.BALL_X = self.rect.centerx

class Goal(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('assets/goal.png'), (192, 18))
        self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-30, -8)
        self.rect.centerx = Settings.WIDTH / 2
        self.rect.top = 0

    def update(self):
        self.hidden = False

class Enemy_Goal(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load('assets/goal2.png'), (192, 18))
        self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-30, -8)
        self.rect.centerx = Settings.WIDTH / 2
        self.rect.bottom = Settings.HEIGHT - 8

    def update(self):
        self.hidden = False