import pygame
from core.neural_controller import NeuralController
from core.physics import PhysicsEngine
from core.environment import Environment
from visualization.visualizer import visualize

def main():
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    num_particles = 10
    physics_engine = PhysicsEngine(num_particles)
    neural_controller = NeuralController()
    environment = Environment(width, height)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        environment.update_chemicals()  # Update the chemical map over time
        sensory_inputs = environment.get_sensory_inputs(physics_engine.get_shape())
        movement_vector = neural_controller.decide_movement(sensory_inputs)

        physics_engine.simulate_step(movement_vector, dt=0.1)

        visualize(physics_engine, environment, screen)
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
