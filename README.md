# 🐦 Flappy Bird AI with NEAT

An intelligent Flappy Bird implementation using neuroevolution through the NEAT (NeuroEvolution of Augmenting Topologies) algorithm. Watch as AI agents learn to navigate through pipes with increasing skill over generations.

## 🎥 Demo
https://github.com/user-attachments/assets/3492d1dd-1c55-49f2-8348-700f29451c41

## 🧠 How It Works

This project demonstrates machine learning through evolutionary algorithms, where multiple AI agents (birds) learn to play Flappy Bird simultaneously. Each generation builds upon the previous one's successes, gradually improving performance through natural selection and neural network evolution.

### Game Logic

The core game mechanics follow the classic Flappy Bird formula:
- **Bird Physics**: Gravity-based movement with jump mechanics
- **Pipe Navigation**: Randomly generated pipe gaps that birds must navigate
- **Collision Detection**: Pixel-perfect collision using pygame masks
- **Scoring System**: Points awarded for successfully passing through pipes

### Neural Network & NEAT Framework

Each bird is controlled by a feed-forward neural network that receives three inputs:
1. **Bird's Y position** - Current vertical location
2. **Distance to top pipe** - Vertical distance to upper obstacle
3. **Distance to bottom pipe** - Vertical distance to lower obstacle

The network outputs a single decision: whether to jump or not (threshold > 0.5).

**NEAT Algorithm Features:**
- **Topology Evolution**: Networks start simple and grow in complexity
- **Species Formation**: Similar networks are grouped and compete
- **Fitness-Based Selection**: Better-performing birds have higher reproduction chances
- **Mutation & Crossover**: Genetic operators introduce variation

Configuration highlights:
- Population size: 20 birds per generation
- Fitness threshold: 100 points (auto-stop)
- Maximum stagnation: 20 generations
- Input nodes: 3, Output nodes: 1, Hidden nodes: Variable

### Performance Tracking & Visualization

The system includes comprehensive real-time and post-training visualization:

**In-Game Display:**
- **Generation Counter**: Shows current generation number in top-left corner
- **Live Score**: Real-time score display in top-right corner  
- **Multi-Bird Visualization**: Watch up to 20 AI birds learning simultaneously
- **Real-time Physics**: Observe bird animations, pipe movements, and collision detection

**Analytics & Plotting:**
- **Fitness Evolution Charts**: Automatically generated matplotlib plots showing best fitness scores across generations
- **Performance Graphs**: Saved as `fitness_plot.png` after training completion
- **Console Statistics**: Detailed NEAT algorithm statistics including species formation, mutation rates, and population health
- **Progress Tracking**: Visual feedback on learning progress and algorithm convergence

## 🚀 Getting Started

### Prerequisites

- Python 3.12+
- Poetry (for dependency management)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/flappy-bird-ai.git
   cd flappy-bird-ai
   ```

2. **Install dependencies**
   ```bash
   poetry install
   ```

3. **Add game assets**
   Create an `imgs` folder in the parent directory and add the following image files:
   - `bird1.png`, `bird2.png`, `bird3.png` (bird animation frames)
   - `pipe.png` (pipe obstacle)
   - `base.png` (ground texture)
   - `bg.png` (background)

### Running the AI

Start the NEAT evolution process:
```bash
poetry run python flappybird/neat_runner.py
```

The AI will begin training, displaying:
- Real-time gameplay with multiple birds
- Generation and score counters
- Console output showing population statistics
- Fitness plots saved as `fitness_plot.png`

### Configuration

Modify [`NEAT_CONFIG.txt`](flappybird/NEAT_CONFIG.txt) to experiment with:
- Population size and mutation rates
- Network topology constraints
- Fitness criteria and thresholds
- Species and stagnation parameters

## 🎯 Key Features

- **Evolutionary Learning**: No pre-training required - AI learns from scratch
- **Real-time Visualization**: Watch the learning process unfold
- **Configurable Parameters**: Easily adjust NEAT algorithm settings
- **Performance Analytics**: Track fitness evolution across generations
- **Clean Architecture**: Modular design with separation of concerns

## 🛠️ Technologies Used

- **Python**: Core programming language
- **Pygame**: Game engine and graphics
- **NEAT-Python**: Neuroevolution algorithm implementation
- **Matplotlib**: Fitness visualization and plotting
- **Poetry**: Dependency management and virtual environments

---

*This project demonstrates the power of evolutionary algorithms in game AI, showcasing how simple fitness functions can lead to complex emergent behaviors.*
