# only defined imports that are shared across all modules
import pygame
import os
pygame.font.init()

# constants hence the all caps var names
WIN_WIDTH = 500
WIN_HEIGHT = 800

IMG_DIR = "imgs"
MAX_SCORE = 100

# list of bird images
# .scale2x doubles the size of the images
# .load loads the images
BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join(IMG_DIR, "bird1.png"))),pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]

PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join(IMG_DIR, "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join(IMG_DIR, "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join(IMG_DIR, "bg.png")))
STAT_FONT = pygame.font.SysFont("comicsans", 50)