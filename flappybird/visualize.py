import matplotlib.pyplot as plt

def plot_fitness(stats):
    generation = range(len(stats.most_fit_genomes))
    best_fitness = [g.fitness for g in stats.most_fit_genomes]

    plt.plot(generation, best_fitness, label="Best Fitness")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.title("Best Fitness Over Generations")
    plt.legend()
    plt.savefig("fitness_plot.png")