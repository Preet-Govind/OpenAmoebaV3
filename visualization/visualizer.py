import pygame
import numpy as np

def visualize(amoeba, environment, screen):
    screen.fill((0, 0, 0))  # Black background

    # Draw nutrients
    environment.draw(screen)

    # Draw amoeba with smooth connecting lines between particles
    positions = amoeba.get_shape()
    for i in range(len(positions)):
        pygame.draw.line(screen, (255, 0, 0), positions[i], positions[(i + 1) % len(positions)], 3)
        pygame.draw.circle(screen, (255, 0, 0), (int(positions[i][0]), int(positions[i][1])), 5)

    pygame.display.flip()
