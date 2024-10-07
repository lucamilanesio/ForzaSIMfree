#!/bin/python3
from sys import platlibdir
from time import sleep

import pygame

def mainLoop(airplaneX, airplaneY):
    plane = pygame.image.load('imagesDirectory/privateJETblue.png').convert_alpha()
    planeFlip = pygame.transform.flip(plane, True, False)
    img = pygame.image.load('imagesDirectory/SpringInYosemite.jpeg').convert()
    imgResize = pygame.transform.scale(img, (1792, 1080))
    crashed = False
    width=700
    height=300
    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            airplaneY = airplaneY - 2
        if keys[pygame.K_DOWN]:
            airplaneY = airplaneY + 2
        if keys[pygame.K_RIGHT]:
            width = width * 0.999
            height = height * 0.999
            airplaneX=airplaneX + 1
        if keys[pygame.K_LEFT]:
            width = width * 1.001
            height = height * 1.001
            airplaneX=airplaneX-1
        if keys[pygame.K_c]:
            img = pygame.image.load('imagesDirectory/ct.jpeg').convert()
            imgResize = pygame.transform.scale(img, (1792, 1080))
        if keys[pygame.K_g]:
            img = pygame.image.load('imagesDirectory/SpringInYosemite.jpeg').convert()
            imgResize = pygame.transform.scale(img, (1792, 1080))
        if keys[pygame.K_y]:
            img = pygame.image.load('imagesDirectory/vf.jpeg').convert()
            imgResize = pygame.transform.scale(img, (1792, 1080))
        if keys[pygame.K_h]:
            img = pygame.image.load('imagesDirectory/hd.jpeg').convert()
            imgResize = pygame.transform.scale(img, (1792, 1080))
        if keys[pygame.K_3]:
            plane = pygame.image.load('imagesDirectory/j2.png').convert_alpha()
            planeFlip = pygame.transform.flip(plane, True, False)
        if keys[pygame.K_2]:
            plane = pygame.image.load('imagesDirectory/privateJETblue.png').convert_alpha()
            planeFlip = pygame.transform.flip(plane, True, False)
        if keys[pygame.K_4]:
            plane = pygame.image.load('imagesDirectory/A380.png').convert_alpha()
            planeFlip = pygame.transform.flip(plane, True, False)
        if keys[pygame.K_a]:
            img = pygame.image.load('imagesDirectory/ap.jpeg').convert()
            imgResize = pygame.transform.scale(img, (1792, 1080))
        if keys[pygame.K_l]:
            img = pygame.image.load('imagesDirectory/a.jpeg').convert()
            imgResize = pygame.transform.scale(img, (1792, 1080))
        if keys[pygame.K_z]:
            img = pygame.image.load('imagesDirectory/a2.jpeg').convert()
            imgResize = pygame.transform.scale(img, (1792, 1080))

        planeScaled = pygame.transform.scale(planeFlip, (width, height))
        scrn.blit(imgResize, (0, 0))
        scrn.blit(planeScaled, (airplaneX,airplaneY))
        pygame.display.flip()

pygame.init()
x=1792
y=1080

scrn=pygame.display.set_mode((x,y))

pygame.display.set_caption( 'panorama' )




mainLoop(500,500)
pygame.quit()
quit()

