import pygame, sys, random, math
from pygame.locals import *
import pyganim
from data import Colors, Settings, Lucca, Globals
from classes import *

pygame.init()

SCREEN = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Air hockey")

def intro():
    intro = True
    background = pygame.transform.scale(pygame.image.load('assets/grass.png'), (Settings.WIDTH, Settings.HEIGHT))
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    Globals.player_char = 'lucca'
                    intro = False
                if event.key == pygame.K_2:
                    Globals.player_char = 'frog'
                    intro = False

        SCREEN.blit(background, (0, 0))

        large_txt = pygame.font.Font('freesansbold.ttf', 34)
        txt_surface = large_txt.render('Choose your character', True, Colors.WHITE)
        txt_rect = txt_surface.get_rect()
        txt_rect.center = (Settings.WIDTH/2, Settings.HEIGHT/4)

        lucca_img = pygame.image.load('assets/sprites/lucca/icon.gif')
        lucca_rect = lucca_img.get_rect()
        lucca_rect.center = (120, Settings.HEIGHT / 2)
        frog_img = pygame.image.load('assets/sprites/frog/icon.gif')
        frog_rect = frog_img.get_rect()
        frog_rect.center = (Settings.WIDTH - 120, Settings.HEIGHT / 2)

        txt_surf_1 = large_txt.render('1', True, Colors.WHITE)
        txt_rect_1 = txt_surf_1.get_rect()
        txt_rect_1.center = (120, Settings.HEIGHT / 2 + 100)

        txt_surf_2 = large_txt.render('2', True, Colors.WHITE)
        txt_rect_2 = txt_surf_2.get_rect()
        txt_rect_2.center = (Settings.WIDTH - 120, Settings.HEIGHT / 2 + 100)

        SCREEN.blit(lucca_img, lucca_rect)
        SCREEN.blit(frog_img, frog_rect)
        SCREEN.blit(txt_surface, txt_rect)
        SCREEN.blit(txt_surf_1, txt_rect_1)
        SCREEN.blit(txt_surf_2, txt_rect_2)
        pygame.display.update()


def status_screen(msg):
    win_anim = None
    enememy_animation = None

    if msg == 'win':
        SCREEN.fill(Colors.WHITE)
        large_txt = pygame.font.Font('freesansbold.ttf', 34)
        txt_surface = large_txt.render('You won!', True, Colors.BLACK)
        txt_rect = txt_surface.get_rect()
        txt_rect.center = (Settings.WIDTH / 2, Settings.HEIGHT / 4)
        if Globals.player_char == 'lucca':
            win_anim = pyganim.PygAnimation('assets/sprites/lucca/win.gif', 20)
        if Globals.player_char == 'frog':
            win_anim = pyganim.PygAnimation('assets/sprites/frog/win.gif')
        enememy_animation = pyganim.PygAnimation('assets/sprites/magus/lose.gif')

    if msg == 'lost':
        SCREEN.fill(Colors.BLACK)
        large_txt = pygame.font.Font('freesansbold.ttf', 34)
        txt_surface = large_txt.render('You lost!', True, Colors.RED)
        txt_rect = txt_surface.get_rect()
        txt_rect.center = (Settings.WIDTH / 2, Settings.HEIGHT / 4)
        if Globals.player_char == 'lucca':
            win_anim = pyganim.PygAnimation('assets/sprites/lucca/lose.gif', 20)
        if Globals.player_char == 'frog':
            win_anim = pyganim.PygAnimation('assets/sprites/frog/lose.gif', 20)
        enememy_animation = pyganim.PygAnimation('assets/sprites/magus/win.gif')

    win_anim.scale((58, 84))
    win_anim.makeTransformsPermanent()
    enememy_animation.scale((58, 84))
    enememy_animation.makeTransformsPermanent()
    win_rect = pygame.Rect((Settings.WIDTH / 2, Settings.HEIGHT / 2), (58, 84))
    lose_rect = pygame.Rect((Settings.WIDTH / 6, Settings.HEIGHT / 2), (58, 84))
    win_anim.play()
    enememy_animation.play()

    while True:
        if msg == 'win':
            SCREEN.fill(Colors.WHITE)
        if msg == 'lost':
            SCREEN.fill(Colors.BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        SCREEN.blit(txt_surface, txt_rect)
        win_anim.blit(SCREEN, win_rect)
        enememy_animation.blit(SCREEN, lose_rect)
        pygame.display.update()


def game_loop():
    all_sprites = MyGroup()

    player = Player()
    enemy = Enemy()

    ball = Ball()
    ball2 = Ball()
    two_balls = False

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

    background = pygame.transform.scale(pygame.image.load('assets/grass.png'), (Settings.WIDTH, Settings.HEIGHT))
    sword = pygame.transform.scale(pygame.image.load('assets/sprites/sword.gif'), (25, 60))

    start_ticks = 0
    started = True

    while True:  # mainloop
        clock.tick(Settings.FPS)
        SCREEN.blit(background, (0, 0))
        SCREEN.blit(sword, (Settings.WIDTH / 2 - 96, 5))
        SCREEN.blit(sword, (Settings.WIDTH / 2 + 96, 5))
        SCREEN.blit(sword, (Settings.WIDTH / 2 - 96, Settings.HEIGHT - 65))
        SCREEN.blit(sword, (Settings.WIDTH / 2 + 96, Settings.HEIGHT - 65))

        if pygame.time.get_ticks() > start_ticks + 20000:
            print('Should get another ball..')
            two_balls = True
            ball_group.add(ball2)
            all_sprites.add(ball2)
            start_ticks = pygame.time.get_ticks()

        hits = pygame.sprite.groupcollide(ball_group, goal_group, False, False)
        for hit in hits:

            hit_by = 0
            ball.rect.centerx = Settings.WIDTH / 2
            ball.rect.centery = Settings.HEIGHT / 2

            Settings.BALL_SPEED = Settings.BALL_STARTING_SPEED

            ball.speed[0] = 0
            ball.speed[1] = Settings.BALL_SPEED

            player_score += 1
            print('Score: ' + str(player_score) + " - " + str(enemy_score))
            if player_score == 5:
                status_screen('win')

            player.rect.centerx = Settings.WIDTH / 2
            enemy.rect.centerx = Settings.WIDTH / 2

            pygame.time.wait(2000)
            start_ticks = pygame.time.get_ticks()
            if two_balls:
                ball2.rect.centerx = Settings.WIDTH / 2
                ball2.rect.centery = Settings.HEIGHT / 2
                ball2.speed[0] = 0
                if random.random() < 0.5:
                    ball2.speed[1] = Settings.BALL_STARTING_SPEED
                else:
                    ball2.speed[1] = -Settings.BALL_STARTING_SPEED
                ball_group.remove(ball2)
                all_sprites.remove(ball2)
                two_balls = False


        hits = pygame.sprite.groupcollide(ball_group, enemy_goal_group, False, False)
        for hit in hits:
            hit_by = 0
            ball.rect.centerx = Settings.WIDTH / 2
            ball.rect.centery = Settings.HEIGHT / 2

            Settings.BALL_SPEED = Settings.BALL_STARTING_SPEED

            ball.speed[0] = 0
            ball.speed[1] = Settings.BALL_SPEED

            enemy_score += 1
            print('Score: ' + str(player_score) + " - " + str(enemy_score))
            if enemy_score == 5:
                status_screen('lost')

            player.rect.centerx = Settings.WIDTH / 2
            enemy.rect.centerx = Settings.WIDTH / 2

            pygame.time.wait(2000)
            start_ticks = pygame.time.get_ticks()
            if two_balls:
                ball_group.remove(ball2)
                all_sprites.remove(ball2)
                two_balls = False

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

            print('Ball got stuck...')

            pygame.time.wait(1500)
            start_ticks = pygame.time.get_ticks()
            if two_balls:
                ball_group.remove(ball2)
                all_sprites.remove(ball2)
                two_balls = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                Globals.MOUSE_X, Globals.MOUSE_Y = event.pos
                player.image = player.player_animations['idle']

        all_sprites.update()
        all_sprites.draw(SCREEN)
        pygame.display.update()

        if started:
            print('The game is about to start!')
            pygame.time.wait(3000)
            started = False

intro()
game_loop()