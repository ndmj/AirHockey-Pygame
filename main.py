import pygame, sys, random, math
from pygame.locals import *

from data import Colors, Settings
from classes import *

pygame.init()

SCREEN = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Air hockey")

all_sprites = MyGroup()

player = Player()
enemy = Enemy()

ball = Ball()

goal = Goal()
enemy_goal = Enemy_Goal()

player_group = MyGroup()
player_group.add(player)

enemy_group = MyGroup()
enemy_group.add(enemy)

ball_group = MyGroup()
ball_group.add(ball)

goal_group = MyGroup()
goal_group.add(goal)

enemy_goal_group = MyGroup()
enemy_goal_group.add(enemy_goal)

all_sprites.add(player)
all_sprites.add(enemy)
all_sprites.add(ball)
all_sprites.add(goal)
all_sprites.add(enemy_goal)

player_score = 0
enemy_score = 0
hit_by = 0

while True:  # mainloop
    clock.tick(Settings.FPS)
    SCREEN.fill(Colors.WHITE)

    hits = pygame.sprite.groupcollide(ball_group, goal_group, False, False)
    for hit in hits:

        hit_by = 0
        hit.rect.centerx = Settings.WIDTH / 2
        hit.rect.centery = Settings.HEIGHT / 2

        Settings.BALL_SPEED = Settings.BALL_STARTING_SPEED

        hit.speed[0] = 0
        hit.speed[1] = Settings.BALL_SPEED

        player_score += 1
        print('Score: ' + str(player_score) + " - " + str(enemy_score))

        player.rect.centerx = Settings.WIDTH / 2
        enemy.rect.centerx = Settings.WIDTH / 2

        pygame.time.wait(2000)

    hits = pygame.sprite.groupcollide(ball_group, enemy_goal_group, False, False)
    for hit in hits:
        hit_by = 0
        hit.rect.centerx = Settings.WIDTH / 2
        hit.rect.centery = Settings.HEIGHT / 2

        Settings.BALL_SPEED = Settings.BALL_STARTING_SPEED

        hit.speed[0] = 0
        hit.speed[1] = Settings.BALL_SPEED

        enemy_score += 1
        print('Score: ' + str(player_score) + " - " + str(enemy_score))

        player.rect.centerx = Settings.WIDTH / 2
        enemy.rect.centerx = Settings.WIDTH / 2

        pygame.time.wait(2000)


    hits = pygame.sprite.groupcollide(ball_group, player_group, False, False)
    for hit in hits:
        if hit_by < 0:
            hit_by = 0

        hit_by += 1
        player_rect = player.rect.centerx, player.rect.centery

        angle = math.degrees(math.atan2(abs(hit.rect.centery - player_rect[1]), abs(hit.rect.centerx - player_rect[0])))

        angle_var = angle/90

        if Settings.BALL_SPEED < Settings.BALL_MAX_SPEED:
            Settings.BALL_SPEED += 1

        hit.speed[0] = (Settings.BALL_SPEED * (1-angle_var)) if hit.speed[0] > 0 else -(Settings.BALL_SPEED * (1-angle_var))
        hit.speed[1] = (Settings.BALL_SPEED * angle_var) if hit.speed[1] > 0 else -(Settings.BALL_SPEED * angle_var)

        if random.random() > 0.75:
            if random.random() > 0.5: # x
                if random.random() > 0.5: # +
                    hit.speed[0] += random.random() * Settings.BALL_SPEED / 4
                else: # -
                    hit.speed[0] -= random.random() * Settings.BALL_SPEED / 4
            else: # y
                if random.random() > 0.5: # +
                    hit.speed[1] += random.random() * Settings.BALL_SPEED / 4
                else:  # -
                    hit.speed[1] -= random.random() * Settings.BALL_SPEED / 4

        if player_rect[0] < hit.rect.centerx:
            hit.speed[0] = -hit.speed[0] if hit.speed[0] < 0 else hit.speed[0]
        elif player_rect[0] > hit.rect.centerx:
            hit.speed[0] = -hit.speed[0] if hit.speed[0] > 0 else hit.speed[0]

        if player_rect[1] < hit.rect.centery:
            hit.speed[1] = hit.speed[1] if hit.speed[1] > 0 else -hit.speed[1]
        elif player_rect[1] > hit.rect.centery:
            hit.speed[1] = hit.speed[1] if hit.speed[1] < 0 else -hit.speed[1]

    hits = pygame.sprite.groupcollide(ball_group, enemy_group, False, False)

    for hit in hits:
        if hit_by > 0:
            hit_by = 0

        hit_by -= 1

        player_rect = enemy.rect.centerx, enemy.rect.centery

        angle = math.degrees(math.atan2(abs(hit.rect.centery - player_rect[1]), abs(hit.rect.centerx - player_rect[0])))

        angle_var = angle / 90

        if Settings.BALL_SPEED < Settings.BALL_MAX_SPEED:
            Settings.BALL_SPEED += 1

        hit.speed[0] = (Settings.BALL_SPEED * (1 - angle_var)) if hit.speed[0] > 0 else -(Settings.BALL_SPEED * (1 - angle_var))
        hit.speed[1] = (Settings.BALL_SPEED * angle_var) if hit.speed[1] > 0 else -(Settings.BALL_SPEED * angle_var)

        if random.random() > 0.75:
            if random.random() > 0.5: # x
                if random.random() > 0.5: # +
                    hit.speed[0] += random.random() * Settings.BALL_SPEED / 4
                else: # -
                    hit.speed[0] -= random.random() * Settings.BALL_SPEED / 4
            else: # y
                if random.random() > 0.5: # +
                    hit.speed[1] += random.random() * Settings.BALL_SPEED / 4
                else:  # -
                    hit.speed[1] -= random.random() * Settings.BALL_SPEED / 4

        if player_rect[0] < hit.rect.centerx:
            hit.speed[0] = -hit.speed[0] if hit.speed[0] < 0 else hit.speed[0]
        elif player_rect[0] > hit.rect.centerx:
            hit.speed[0] = -hit.speed[0] if hit.speed[0] > 0 else hit.speed[0]

        if player_rect[1] < hit.rect.centery:
            hit.speed[1] = hit.speed[1] if hit.speed[1] > 0 else -hit.speed[1]
        elif player_rect[1] > hit.rect.centery:
            hit.speed[1] = hit.speed[1] if hit.speed[1] < 0 else -hit.speed[1]

    if abs(hit_by) == 50:
        hit_by = 0
        ball.rect.centerx = Settings.WIDTH / 2
        ball.rect.centery = Settings.HEIGHT / 2

        Settings.BALL_SPEED = Settings.BALL_STARTING_SPEED

        ball.speed[0] = 0
        ball.speed[1] = Settings.BALL_SPEED

        player.rect.centerx = Settings.WIDTH / 2
        enemy.rect.centerx = Settings.WIDTH / 2

        print('Ball got stuck')

        pygame.time.wait(1500)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            Globals.MOUSE_X, Globals.MOUSE_Y = event.pos

    all_sprites.update()
    all_sprites.draw(SCREEN)
    pygame.display.update()
