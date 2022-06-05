import pygame
import sys
import time
import random

from pygame.constants import FINGERMOTION


# Check eror game
check_errors = pygame.init()
if check_errors[1] > 0:
    print('[!] {check_errors} error game')
else:
    print('[+] Game succes install')

# ============ window game ===========

size_x = 480
size_y = 480

# title game
pygame.display.set_caption('Ulo-Uloan')
screen = pygame.display.set_mode((size_x, size_y))

# ========= game variabel =========
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)

# Panganan
food_pos = [random.randrange(1, size_x // 10) * 10,
            random.randrange(1, size_y // 10) * 10]
food_spawn = True

# skor

score = 0

# Suara

pygame.mixer.init()
eating = pygame.mixer.Sound('eatsong.wav')



# game over funct
def game_over():
    my_font = pygame.font.SysFont('times new roman', 40)
    game_over_surface = my_font.render('Mati Awokwokwokwok', True, white)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (size_x/2, size_y/5)
    screen.fill(black)
    screen.blit(game_over_surface, game_over_rect)
    # show_score(0, red, 'times', 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()

# show score funct


def show_score():
    score_font = pygame.font.SysFont('consolas', 20)
    score_surface = score_font.render('Your poin : ' + str(score), True, black)
    score_rect = score_surface.get_rect()
    score_rect.midtop = (350, 15)

    screen.blit(score_surface, score_rect)
    pygame.display.flip()


# snake
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

change_to = "RIGHT"

direction = "RIGHT"

# change background to white

screen.fill(white)

# running
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"

    # update screen to white again

    screen.fill(white)

    # Create Snake

    for pos in snake_body:
        pygame.draw.ellipse(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))
    snake_body.insert(0, snake_pos[:])

    # fix jalan mundur

    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"

    # ==============================

    if direction == "RIGHT":
        snake_pos[0] += 10
    if direction == "LEFT":
        snake_pos[0] -= 10
    if direction == "UP":
        snake_pos[1] -= 10
    if direction == "DOWN":
        snake_pos[1] += 10
    print(snake_pos)

    # snake over window
    if snake_pos[0] > size_x:
        snake_pos[0] = 0
    if snake_pos[0] < 0:
        snake_pos[0] = size_x
    if snake_pos[1] > size_y:
        snake_pos[1] = 0
    if snake_pos[1] < 0:
        snake_pos[1] = size_y

    # Draw food
    pygame.draw.rect(screen, green, pygame.Rect(
        food_pos[0], food_pos[1], 10, 10))

    # snake eateing food

    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        food_spawn = False
        score += 1
        eating.play()
    else:
        snake_body.pop()

    # logika for spawn

    if not food_spawn:
        food_pos = [random.randrange(
            1, size_x // 10) * 10, random.randrange(1, size_y // 10) * 10]
    food_spawn = True

    # show score

    show_score()

    # game over

    for block in snake_body:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    # level

    pygame.time.Clock().tick(10)

    # Update screen
    pygame.display.update()
