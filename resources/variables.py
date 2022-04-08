import pygame
import os.path

pygame.init()

WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Triangle')
ICON_SURFACE = pygame.image.load(os.path.join('resources', 'triangle_icon.png')).convert_alpha()
pygame.display.set_icon(ICON_SURFACE)
FPS = 120
CLOCK = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
