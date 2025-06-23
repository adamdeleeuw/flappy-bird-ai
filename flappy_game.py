import pygame
import neat
pygame.font.init()

from constants import WIN_WIDTH, WIN_HEIGHT
from bird import Bird
from pipe import Pipe
from base import Base
from draw_win import draw_window 

def main(genomes, config, gen):
    nets = [] # keeps track of neural nets
    ge = [] #keeps track of genomes
    birds = []

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        birds.append(Bird(230, 350))
        g.fitness = 0
        ge.append(g)

    base = Base(730)
    pipes = [Pipe(700)]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()

    score = 0

    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

        pipe_ind = 0
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width():
                pipe_ind = 1
        else:
            run = False
            break

        for x, bird in enumerate(birds):
            bird.move()
            ge[x].fitness += 0.1

            output = nets[x].activate((bird.y, abs(bird.y -pipes[pipe_ind].height), abs(bird.y - pipes[pipe_ind].bottom)))

            if output[0] > 0.5:
                bird.jump()


        add_pipe = False
        rem = []
        for pipe in pipes:
            pipe.move()

            for x, bird in enumerate(birds):
                if pipe.collide(bird):
                    ge[x].fitness -= 1 
                    birds.pop(x)
                    nets.pop(x)
                    ge.pop(x)

                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    add_pipe = True

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)

        if add_pipe:
            score += 1 
            for g in ge:
                g.fitness += 5

            pipes.append(Pipe(600))   

        for r in rem:
            pipes.remove(r) 


        for x, bird in enumerate(birds):
            if bird.y + bird.img.get_height() >= 730 or bird.y < 0:
                birds.pop(x)
                nets.pop(x)
                ge.pop(x)   
        
        base.move()
        draw_window(win, birds, pipes, base, score, gen)

# Updates:
# 1. Use pickle to save best bird and be able to use it
# 2. Add more neural net visualization