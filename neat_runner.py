import neat
import os
from flappy_game import main

def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    # population
    p = neat.Population(config)

    # stats in console when running
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    gen_counter = [0] # using a mutable list to keep track of generations (inside int would be immutable)

    def eval_genomes(genomes, config):
        gen_counter[0] += 1
        main(genomes, config, gen_counter[0])

    winner = p.run(eval_genomes, 50)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "NEAT_CONFIG.txt")
    run(config_path)