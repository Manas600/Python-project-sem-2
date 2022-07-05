import pygame
import random


pygame.init()


# Creating screen
screen = pygame.display.set_mode((800,600))

# Background
background = pygame.image.load('background.png')



# Title and icon
pygame.display.set_caption("Galaxy rush")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load("arcade-game.png")
playerX=370
playerY=480
playerX_change=0

#Enemy
EnemyImg = []
EnemyX = []
EnemyY = []
EnemyX_change = []
EnemyY_change = []
num_of_enemies = 4
for i in range(num_of_enemies) :
    EnemyImg.append(pygame.image.load('Enemy.png'))
    EnemyX.append(random.randint(0,735))
    EnemyY.append(random.randint(50,150))
    EnemyX_change.append(1)
    EnemyY_change.append(40)

def player(x,y):
    screen.blit(playerImg,(x,y))

def Enemy(x,y,i):
    screen.blit(EnemyImg[i],(x,y))



# Game loop
running = True
while running:
    #RGB colors 
    screen.fill((10 ,51, 102))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False