import pygame
from Config import PLATFORM_IMAGE, PLATFORM_SIZE, WIDTH, HEIGHT


class Platform(pygame.sprite.Sprite):

    def __init__(self, pos):
        super(Platform, self).__init__()
        self.position = pos
        self.image = pygame.Surface(PLATFORM_SIZE, flags=pygame.SRCALPHA)  # creating of the platform
        sprite = pygame.image.load(PLATFORM_IMAGE).convert_alpha()
        sprite = pygame.transform.scale(sprite, self.image.get_size())
        self.image.blit(sprite, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2
        self.rect.y = HEIGHT - 100
