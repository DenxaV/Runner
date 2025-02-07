import os
import random
import math
import pygame
from sys import exit
from os import listdir
from os.path import isfile, join

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)




# IMAGES
background_surface = pygame.image.load('sprites/woods.png')
foreground_surface = pygame.image.load('sprites/ground.png')
text_surface = test_font.render('Run', False, 'White')

en_x_pos = 600

# RESIZE
enemy_surface = [
    pygame.transform.scale(pygame.image.load('sprites/enemy1.png'), (50, 50)),
    pygame.transform.scale(pygame.image.load('sprites/enemy2.png'), (50, 50)),
    pygame.transform.scale(pygame.image.load('sprites/enemy3.png'), (50, 50))
]
protagonist_surface = [
    pygame.transform.scale(pygame.image.load('sprites/ghost1.png'), (60, 80)),
    pygame.transform.scale(pygame.image.load('sprites/ghost2.png'), (60, 80)),
    pygame.transform.scale(pygame.image.load('sprites/ghost3.png'), (60, 80)),
    pygame.transform.scale(pygame.image.load('sprites/ghost4.png'), (60, 80)),
    pygame.transform.scale(pygame.image.load('sprites/ghost5.png'), (60, 80)),
    pygame.transform.scale(pygame.image.load('sprites/ghost6.png'), (60, 80))
]
protagonist_idle = pygame.transform.scale(pygame.image.load('sprites/ghost1.png'), (60, 80))


# INITIALISATIONS
WIDTH, HEIGHT = 800, 600 
enemy_pos = [400, 189]
protagonist_pos = [0,0]  
protagonist_velocity = 0
gravity = 0.5
is_jumping = False
speed= 5
enemy_frame = 0
protagonist_frame = 0
animation_speed = 60  
ground_level = 160
facing_right = True
is_moving = False
protagonist_index = 0

# MOVEMENT
            # PROTAGONIST 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        protagonist_pos[0] -= speed
        if not facing_right:
            facing_right = True 
            is_moving = True

    if keys[pygame.K_RIGHT]:
        protagonist_pos[0] += speed    
        if facing_right:
            facing_right = False
            is_moving = True


    if is_moving:
        protagonist_index += 1   
        if protagonist_index >= len(protagonist_surface):
            protagonist_index = 0
    else:
        protagonist_index = 0
        protagonist_frame  = protagonist_idle


    if not is_jumping and keys[pygame.K_SPACE]:
        protagonist_velocity = -10
        is_jumping = True

    protagonist_velocity += gravity
    protagonist_pos[1] += protagonist_velocity

    if protagonist_pos[1] >= ground_level:
        protagonist_pos[1] = ground_level
        protagonist_velocity = 0
        is_jumping = False

    if protagonist_pos[1] >= 240:
        protagonist_pos[1] = 240
        is_jumping = False

            # ENEMY
    enemy_pos[0] -= speed
    if enemy_pos[0] < -50:
        enemy_pos[0] = 800


    enemy_rect = pygame.Rect(enemy_pos[0], enemy_pos[1], 40, 60)
    protagonist_rect = pygame.Rect(protagonist_pos[0], protagonist_pos[1], 40, 60)
    if enemy_rect.colliderect(protagonist_rect):
        break


    current_time = pygame.time.get_ticks()
      
# ENEMY
    enemy_frame = (current_time // animation_speed) % len(enemy_surface)
    enemy_image = enemy_surface[enemy_frame]



# PROTAGONIST
    if is_moving:
        protagonist_image = protagonist_surface[int(protagonist_index)]
    else:
        protagonist_image = protagonist_idle
             
    protagonist_frame = (current_time // animation_speed) % len(protagonist_surface)
    protagonist_image = protagonist_surface[protagonist_frame]
    if not facing_right:
        protagonist_image = pygame.transform.flip(protagonist_image, True,False)

    # screen
    screen.blit(background_surface, (0, 0))
    screen.blit(foreground_surface, (0, 240))
    screen.blit(text_surface, (200, 20))
    screen.blit(enemy_image, enemy_pos)
    en_x_pos += 1
    screen.blit(protagonist_image, protagonist_pos)

    pygame.display.update()
    clock.tick(animation_speed)
 
