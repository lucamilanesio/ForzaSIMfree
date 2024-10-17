#!/bin/python3
from sys import platlibdir
from time import sleep

import pygame


def blitRotate(surf, image, pos, originPos, angle):
    # offset from pivot to center
    image_rect = image.get_rect(
        topleft=(
            pos[0] -
            originPos[0],
            pos[1] -
            originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    # roatated offset from pivot to center
    rotated_offset = offset_center_to_pivot.rotate(-angle)

    # roatetd image center
    rotated_image_center = (
        pos[0] - rotated_offset.x,
        pos[1] - rotated_offset.y)

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)

    # rotate and blit the image
    surf.blit(rotated_image, rotated_image_rect)


def blitRotate2(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(
        center=image.get_rect(
            topleft=topleft).center)

    surf.blit(rotated_image, new_rect.topleft)
    pygame.draw.rect(surf, (255, 0, 0), new_rect, 2)


def mainLoop(airplaneX, airplaneY):
    sw, sh = scrn.get_size()
    iw, ih = (sw * 1.9, sh * 1.9)
    plane = pygame.image.load(
        'imagesDirectory/privateJETblue.png').convert_alpha()
    planeFlip = pygame.transform.flip(plane, True, False)
    img = pygame.image.load('imagesDirectory/SpringInYosemite.jpeg').convert()
    backgroundImage = pygame.transform.scale(img, (iw, ih))
    crashed = False
    width = 700
    height = 300
    rotationAngle = 0
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
            airplaneX = airplaneX + 1
        if keys[pygame.K_LEFT]:
            width = width * 1.001
            height = height * 1.001
            airplaneX = airplaneX - 1
        if keys[pygame.K_c]:
            img = pygame.image.load('imagesDirectory/ct.jpeg').convert()
            backgroundImage = pygame.transform.scale(img, (iw, ih))
        if keys[pygame.K_g]:
            img = pygame.image.load(
                'imagesDirectory/SpringInYosemite.jpeg').convert()
            backgroundImage = pygame.transform.scale(img, (iw, ih))
        if keys[pygame.K_y]:
            img = pygame.image.load('imagesDirectory/vf.jpeg').convert()
            backgroundImage = pygame.transform.scale(img, (iw, ih))
        if keys[pygame.K_h]:
            img = pygame.image.load('imagesDirectory/hd.jpeg').convert()
            backgroundImage = pygame.transform.scale(img, (iw, ih))
        if keys[pygame.K_3]:
            plane = pygame.image.load('imagesDirectory/j2.png').convert_alpha()
            planeFlip = pygame.transform.flip(plane, True, False)
        if keys[pygame.K_2]:
            plane = pygame.image.load(
                'imagesDirectory/privateJETblue.png').convert_alpha()
            planeFlip = pygame.transform.flip(plane, True, False)
        if keys[pygame.K_4]:
            plane = pygame.image.load(
                'imagesDirectory/A380.png').convert_alpha()
            planeFlip = pygame.transform.flip(plane, True, False)
        if keys[pygame.K_a]:
            img = pygame.image.load('imagesDirectory/ap.jpeg').convert()
            backgroundImage = pygame.transform.scale(img, (iw, ih))
        if keys[pygame.K_l]:
            img = pygame.image.load('imagesDirectory/a.jpeg').convert()
            backgroundImage = pygame.transform.scale(img, (iw, ih))
        if keys[pygame.K_z]:
            img = pygame.image.load('imagesDirectory/a2.jpeg').convert()
            backgroundImage = pygame.transform.scale(img, (iw, ih))
        if keys[pygame.K_r]:
            rotationAngle = rotationAngle + 1
            backgroundImage = pygame.transform.scale(img, (iw, ih))
        blitRotate(scrn, backgroundImage, (sw / 2, sh / 2),
                   (iw / 2, ih / 2), rotationAngle)
        planeScaled = pygame.transform.scale(planeFlip, (width, height))
        scrn.blit(planeScaled, (airplaneX, airplaneY))
        pygame.display.flip()


pygame.init()
x = 1792
y = 1080

scrn = pygame.display.set_mode((x, y))

pygame.display.set_caption('panorama')


mainLoop(500, 500)
pygame.quit()
quit()
