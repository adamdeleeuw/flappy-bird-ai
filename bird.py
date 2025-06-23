import pygame
from constants import BIRD_IMGS


class Bird:
    IMGS = BIRD_IMGS 
    MAX_ROTATION = 25 #how much the bird titls
    ROT_VEL = 20 # how much we rotate each frame
    ANIMATION_TIME = 5 # how long we show each animation

    # A constructor method that runs automatically when a Bird object is created. It sets the bird’s starting position and initializes its properties (like tilt, velocity, and image for animation).
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0 #keeps track of last jump
        self.height = self.y #keeps track of where the bird jumped from

    def move(self):
        self.tick_count += 1

        # total distance the bird moves in a frame - defines the arcing "physics"
        d = self.vel*self.tick_count + 1.5*self.tick_count**2 

        if d >= 16: # moving down 16 pixels
            d = 16

        if d < 0:
            d -= 2

        self.y = self.y + d

        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL

    def draw(self, win):
        self.img_count += 1

        #logic can be made more efficient - defines the bird "flapping" animation by switching bird imgs

        if self.img_count < self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count < self.ANIMATION_TIME*2:
            self.img = self.IMGS[1]
        elif self.img_count < self.ANIMATION_TIME*3:
            self.img = self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME*4:
            self.img = self.IMGS[1]
        elif self.img_count == self.ANIMATION_TIME*4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME*2

        # function that defines the tilting of the bird 
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft = (self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)