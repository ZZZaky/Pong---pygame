import pygame, sys
pygame.init()
clock = pygame.time.Clock()
import random

####################
######SETTINGS######

speed = 20 #game speed

######SETTINGS######
####################


def ball_animation():
    global ball_speed_x, ball_speed_y, start

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x = 0
        ball_speed_y = 0
        start = True
        ball.center = (screen_width/2, screen_height/2)
        

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_animation():
    opponent.y += opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


screen_width, screen_height = (1080, 720)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Super Pong')

ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 50, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(40, screen_height/2 - 70, 10, 140)

bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

start = True
ball_speed_x = 0
ball_speed_y = 0
player_speed = 0
opponent_speed = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += speed
            if event.key == pygame.K_UP:
                player_speed -= speed
            if event.key == pygame.K_s:
                opponent_speed += speed
            if event.key == pygame.K_w:
                opponent_speed -= speed
            if event.key == pygame.K_SPACE and start:
                ball_speed_x = speed * random.choice((1, -1))
                ball_speed_y = speed * random.choice((1, -1))
                start = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed = 0
            if event.key == pygame.K_UP:
                player_speed = 0
            if event.key == pygame.K_w:
                opponent_speed = 0
            if event.key == pygame.K_s:
                opponent_speed = 0

    ball_animation()
    player_animation()
    opponent_animation()

    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))


    pygame.display.flip()
    clock.tick(60)