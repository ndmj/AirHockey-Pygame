import pygame, sys, random, math
from pygame.locals import *
import pyganim
from data import Colors, Settings, Lucca, Globals
from classes import *

pygame.init()

SCREEN = pygame.display.set_mode((Settings.WIDTH, Settings.HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Chrono Trigger!")
ball_sound = pygame.mixer.Sound('assets/sounds/ball.wav')
goal_sound = pygame.mixer.Sound('assets/sounds/goal.wav')
enemy_goal_sound = pygame.mixer.Sound('assets/sounds/enemy_goal.wav')
def intro():
    intro = True
    background = pygame.transform.scale(pygame.image.load('assets/sprites/grass.png'), (Settings.WIDTH, Settings.HEIGHT))
    pygame.mixer.music.load('assets/sounds/intro.mp3')
    pygame.mixer.music.play(-1)
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

        large_txt = pygame.font.Font('assets/fonts/ChronoType.ttf', 48)
        txt_surface = large_txt.render('Choose your character!', True, Colors.WHITE)
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

def difficulty_screen():
    intro = True
    background = pygame.transform.scale(pygame.image.load('assets/sprites/grass.png'),
                                        (Settings.WIDTH, Settings.HEIGHT))
    pygame.mixer.music.load('assets/sounds/intro.mp3')
    pygame.mixer.music.play(-1)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    Settings.ENEMY_SPEED = 4
                    intro = False
                if event.key == pygame.K_2:
                    Settings.ENEMY_SPEED = 7
                    intro = False
                if event.key == pygame.K_3:
                    Settings.ENEMY_SPEED = 10
                    Settings.PLAYER_SPEED = 9
                    intro = False

        SCREEN.blit(background, (0, 0))

        large_txt = pygame.font.Font('assets/fonts/ChronoType.ttf', 48)
        txt_surface = large_txt.render('Choose difficulty!', True, Colors.WHITE)
        txt_rect = txt_surface.get_rect()
        txt_rect.center = (Settings.WIDTH/2, Settings.HEIGHT/4)

        txt_surf_1 = large_txt.render('1 - Easy', True, Colors.WHITE)
        txt_rect_1 = txt_surf_1.get_rect()
        txt_rect_1.center = (Settings.WIDTH/2, Settings.HEIGHT / 2 - 50)

        txt_surf_2 = large_txt.render('2 - Normal', True, Colors.WHITE)
        txt_rect_2 = txt_surf_2.get_rect()
        txt_rect_2.center = (Settings.WIDTH/2, Settings.HEIGHT / 2)

        txt_surf_3 = large_txt.render('3 - Hard', True, Colors.WHITE)
        txt_rect_3 = txt_surf_3.get_rect()
        txt_rect_3.center = (Settings.WIDTH/2, Settings.HEIGHT / 2 + 50)

        SCREEN.blit(txt_surface, txt_rect)
        SCREEN.blit(txt_surf_1, txt_rect_1)
        SCREEN.blit(txt_surf_2, txt_rect_2)
        SCREEN.blit(txt_surf_3, txt_rect_3)
        pygame.display.update()

def status_screen(msg):
    win_anim = None
    enememy_animation = None
    screen = True

    if msg == 'win':
        pygame.mixer.music.load('assets/sounds/win.mp3')
        pygame.mixer.music.play(-1)
        SCREEN.fill(Colors.WHITE)
        large_txt = pygame.font.Font('assets/fonts/ChronoType.ttf', 34)
        txt_surface = large_txt.render('You won!', True, Colors.BLACK)
        txt_rect = txt_surface.get_rect()
        txt_rect.center = (Settings.WIDTH / 2, Settings.HEIGHT / 4)
        txt_surface_2 = large_txt.render('Press space to try again!', True, Colors.BLACK)
        txt_rect_2 = txt_surface_2.get_rect()
        txt_rect_2.center = (Settings.WIDTH / 2, Settings.HEIGHT - 100)
        if Globals.player_char == 'lucca':
            win_anim = pyganim.PygAnimation('assets/sprites/lucca/win.gif', 20)
        if Globals.player_char == 'frog':
            win_anim = pyganim.PygAnimation('assets/sprites/frog/win.gif')
        enememy_animation = pyganim.PygAnimation('assets/sprites/magus/lose.gif')

    if msg == 'lost':
        pygame.mixer.music.load('assets/sounds/lose.mp3')
        pygame.mixer.music.play(-1)
        SCREEN.fill(Colors.BLACK)
        large_txt = pygame.font.Font('assets/fonts/ChronoType.ttf', 34)
        txt_surface = large_txt.render('You lost!', True, Colors.RED)
        txt_rect = txt_surface.get_rect()
        txt_rect.center = (Settings.WIDTH / 2, Settings.HEIGHT / 4)
        txt_surface_2 = large_txt.render('Press space to try again!', True, Colors.RED)
        txt_rect_2 = txt_surface_2.get_rect()
        txt_rect_2.center = (Settings.WIDTH / 2, Settings.HEIGHT - 100)
        if Globals.player_char == 'lucca':
            win_anim = pyganim.PygAnimation('assets/sprites/lucca/lose.gif', 20)
        if Globals.player_char == 'frog':
            win_anim = pyganim.PygAnimation('assets/sprites/frog/lose.gif', 20)
        enememy_animation = pyganim.PygAnimation('assets/sprites/magus/win.gif')

    if msg == 'win' and Globals.player_char == 'frog':
        win_anim.scale((68, 94))
    else:
        win_anim.scale((58, 84))

    win_anim.makeTransformsPermanent()
    enememy_animation.scale((58, 84))
    enememy_animation.makeTransformsPermanent()
    win_rect = pygame.Rect((Settings.WIDTH - 125, Settings.HEIGHT / 2), (68, 94))
    lose_rect = pygame.Rect((Settings.WIDTH / 6, Settings.HEIGHT / 2), (58, 84))
    win_anim.play()
    enememy_animation.play()


    while screen:
        if msg == 'win':
            SCREEN.fill(Colors.WHITE)
        if msg == 'lost':
            SCREEN.fill(Colors.BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro()
                    difficulty_screen()
                    game_loop()

        SCREEN.blit(txt_surface_2, txt_rect_2)
        SCREEN.blit(txt_surface, txt_rect)
        win_anim.blit(SCREEN, win_rect)
        enememy_animation.blit(SCREEN, lose_rect)
        pygame.display.update()


def game_loop():
    pygame.mixer.music.load('assets/sounds/game.mp3')
    pygame.mixer.music.play(-1)
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

    background = pygame.transform.scale(pygame.image.load('assets/sprites/grass.png'), (Settings.WIDTH, Settings.HEIGHT))
    sword = pygame.transform.scale(pygame.image.load('assets/sprites/sword.gif'), (25, 60))

    start_ticks = pygame.time.get_ticks()
    started = True

    def score_board(player_score, enemy_score, SCREEN):
        font = pygame.font.Font('assets/fonts/ChronoType.ttf', 36)
        scoreboard = font.render(str(player_score) + ' : ' + str(enemy_score), True, Colors.WHITE)
        rectangle = scoreboard.get_rect()
        rectangle.center = (60, Settings.HEIGHT - 20)

        SCREEN.blit(scoreboard, rectangle)

    while True:  # mainloop
        clock.tick(Settings.FPS)
        SCREEN.blit(background, (0, 0))
        SCREEN.blit(sword, (Settings.WIDTH / 2 - 106, 5))
        SCREEN.blit(sword, (Settings.WIDTH / 2 + 86, 5))
        SCREEN.blit(sword, (Settings.WIDTH / 2 - 106, Settings.HEIGHT - 65))
        SCREEN.blit(sword, (Settings.WIDTH / 2 + 86, Settings.HEIGHT - 65))
        score_board(player_score, enemy_score, SCREEN)

        if pygame.time.get_ticks() > start_ticks + 20000:
            print('Should get another ball..')
            two_balls = True
            ball2.rect.centerx = Settings.WIDTH / 2
            ball2.rect.centery = Settings.HEIGHT / 2
            ball2.speed[0] = 0
            if random.random() < 0.5:
                ball2.speed[1] = Settings.BALL_STARTING_SPEED
            else:
                ball2.speed[1] = -Settings.BALL_STARTING_SPEED
            ball_group.add(ball2)
            all_sprites.add(ball2)
            start_ticks = pygame.time.get_ticks()

        hits = pygame.sprite.groupcollide(ball_group, goal_group, False, False)
        for hit in hits:
            goal_sound.play()
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
                ball_group.remove(ball2)
                all_sprites.remove(ball2)
                two_balls = False


        hits = pygame.sprite.groupcollide(ball_group, enemy_goal_group, False, False)
        for hit in hits:
            enemy_goal_sound.play()
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
            ball_sound.play()
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
            ball_sound.play()
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
difficulty_screen()
game_loop()