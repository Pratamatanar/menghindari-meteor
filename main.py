import pygame
import random
import math
from pygame import mixer


pygame.init()

screen = pygame.display.set_mode((680,590))
pygame.display.set_caption("menghindari meteor")
icon = pygame.image.load("shuttle.png")
pygame.display.set_icon(icon)

pygame.mixer.init()

point_sound = pygame.mixer.Sound("point.mp3")
point_sound.set_volume(0.75)

pygame.mixer.music.load("backsound.mp3")
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.set_volume(0.75)


background = pygame.image.load("background.jpg")


font = pygame.font.Font("score.TTF",28)

score = 0

def show_score(x,y):
    score_number = font.render("score :" + str(score), True,(255,255,255))
    screen.blit(score_number,(x,y))

x_score = 10
y_score = 10

nyawa = 5

def show_nyawa(x,y):
    nyawa_number = font.render("nyawa :" + str(nyawa), True,(255,255,255))
    screen.blit(nyawa_number,(x,y))

x_nyawa = 560
y_nyawa = 10

def player (x,y):
    player = pygame.image.load("spaceship.png")
    screen.blit(player,(x,y))

x_player = 290
y_player = 480

x_player_point = 0
y_player_point = 0

def meteor (x,y):
    meteor = pygame.image.load("meteor.png")
    screen.blit(meteor,(x,y))

x_meteor = random.randint(10,580)
y_meteor = random.randint(0,10)

x_meteor_point = 0
y_meteor_point = 6

def collision (x_player,y_player,x_meteor,y_meteor):
    distance = math.sqrt(math.pow(x_player-x_meteor,2) + (math.pow(y_player-y_meteor,2)))
    if distance < 70:
    	return True
    else:
        return False

clock = pygame.time.Clock()


running = True
while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False              
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord("a"):
                x_player_point -= 5
            if event.key == pygame.K_RIGHT or event.key == ord("d"):
                x_player_point += 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord("a"):
                x_player_point = 0
            if event.key == pygame.K_RIGHT or event.key == ord("d"):
                x_player_point = 0
    

    x_player += x_player_point
    if x_player >= 580:
        x_player = 570
    if x_player <= 10:
        x_player = 20

    y_meteor += y_meteor_point
    if y_meteor >= 600:
       point_sound.play()
       x_meteor = random.randint(10,580)
       y_meteor = random.randint(0,0)
       score += 1

    tabrakan = collision(x_player,y_player,x_meteor,y_meteor)
    if tabrakan:
        x_meteor = random.randint(10,580)
        y_meteor = random.randint(0,0)
        nyawa -= 1
    else:
        nyawa -= 0


    if nyawa <= 0:
        break

    clock.tick(60)

    screen.fill((0,0,0))
    screen.blit(background,(0,0))    
    meteor(x_meteor,y_meteor)
    player(x_player,y_player)
    show_score(x_score,y_score)
    show_nyawa(x_nyawa,y_nyawa)
    
    pygame.display.update()

pygame.quit()

print ("score anda :" + str(score))