import pygame
import time

from Interface import Interface
from Menu import Menu
from Rocket import Rocket
from Platform import Platform
from Config import *

SCORE = 100

pygame.init()
pygame.display.set_caption(WINDOW_TITLE)
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode(SCREEN_SIZE)
run = True

all_sprites = pygame.sprite.Group()
rocket = Rocket(SPEED, GRAVITY_VECTOR, (WIDTH / 2, HEIGHT / 8))  # creating of the rocket
platform = Platform((WIDTH/2, HEIGHT-100))
all_sprites.add(rocket)
all_sprites.add(platform)

playersprite = pygame.sprite.RenderClear(rocket)
platfomrsprite = pygame.sprite.RenderClear(platform)

background = pygame.image.load(BACKGROUND_IMAGE_LEVEL_1)
background = pygame.transform.scale(background, SCREEN_SIZE)

level = 1
interface = Interface(SCREEN_SIZE, screen)


def draw():
    playersprite.update()
    rocket.update()

    screen.blit(background, (0, 0))

    playersprite.draw(screen)
    platfomrsprite.draw(screen)

    """ interface """
    Interface.render(interface, SCORE, 0, 0, "SCORE: ")
    Interface.render(interface, abs(round(rocket.move_direction[0], 2)), 0, 50, "HORIZONTAL SPEED: ")
    Interface.render(interface, abs(round(rocket.move_direction[1], 2)), 0, 100, "VERTICAL SPEED: ")
    Interface.render(interface, rocket.fuel, 0, 150, "FUEL: ")
    Interface.render(interface, level, WIDTH - 100, 0, "LEVEL: ")


    pygame.display.update()


items = [(WIDTH / 2 - 200, HEIGHT / 2, u"Game", GREEN, YELLOW, 0),
         (WIDTH / 2 + 100, HEIGHT / 2, u"Quit", GREEN, YELLOW, 1)]
game = Menu(screen, items)
game.menu()


def game_over():
    if (rocket.position[0] - rocket.rect.width / 2) < 0 \
            or (rocket.position[0] + rocket.rect.width / 2) > WIDTH \
            or (rocket.position[1] - rocket.rect.height / 2) < 0 \
            or (rocket.position[1] + rocket.rect.height / 2) > (HEIGHT - 100):
        screen.fill(BLACK)
        font = pygame.font.SysFont(FONT, 40)
        for i in range(180):
            CLOCK.tick(GAME_FPS)
            screen.blit(font.render("You lose", False, RED), (WIDTH / 2, HEIGHT / 2))
            pygame.display.update()
        game.menu()
        return False
    else:
        return True

# def game_win():
#     if rocket.position[0] + rocket.rect.height == platform.


while run:

    CLOCK.tick(GAME_FPS)

    time1 = time.time()

    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                rocket.angle_speed = -ANGLE

            if event.key == pygame.K_RIGHT:
                rocket.angle_speed = +ANGLE

            if event.key == pygame.K_UP:
                rocket.gas = True

            if event.key == pygame.K_ESCAPE:
                game.menu()
                pygame.key.set_repeat(1, 1)
                pygame.mouse.set_visible(False)

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_UP:
                rocket.gas = False

            if event.key == pygame.K_RIGHT:
                rocket.angle_speed = 0

            if event.key == pygame.K_LEFT:
                rocket.angle_speed = 0

    game_over()
    draw()

pygame.quit()
