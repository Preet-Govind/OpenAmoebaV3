import numpy as np
import pygame

class Environment:
    def __init__(self, width, height, num_nutrients=10, diffusion_rate=0.01):
        self.width = width
        self.height = height
        self.num_nutrients = num_nutrients
        self.diffusion_rate = diffusion_rate
        self.chemical_map = np.zeros((width, height))
        self._generate_nutrients()
        self._apply_chemicals()

    def _generate_nutrients(self):
        self.nutrients = np.random.rand(self.num_nutrients, 2) * [self.width, self.height]

    def _apply_chemicals(self):
        for nutrient in self.nutrients:
            x, y = int(nutrient[0]), int(nutrient[1])
            self.chemical_map[x, y] = 1.0  # High concentration at the nutrient location

    def update_chemicals(self):
        # Simulate diffusion
        self.chemical_map = self.chemical_map * (1 - self.diffusion_rate)
        # Ensure the chemical_map stays within [0, 1] range
        self.chemical_map = np.clip(self.chemical_map, 0, 1)

    def get_sensory_inputs(self, amoeba_positions):
        sensory_inputs = []
        for pos in amoeba_positions:
            x, y = int(pos[0]), int(pos[1])
            # Extract a small region around the amoeba position to simulate sensing
            region = self.chemical_map[x-5:x+5, y-5:y+5]
            avg_concentration = np.mean(region)
            sensory_inputs.append(avg_concentration)

        # Ensure inputs have a consistent shape, e.g., (100,)
        if len(sensory_inputs) < 100:
            sensory_inputs = np.pad(sensory_inputs, (0, 100 - len(sensory_inputs)), 'constant')
        elif len(sensory_inputs) > 100:
            sensory_inputs = sensory_inputs[:100]
        return np.array(sensory_inputs)

    def draw(self, screen):
        # Draw nutrients and chemical gradients on the screen
        for nutrient in self.nutrients:
            pygame.draw.circle(screen, (0, 255, 0), (int(nutrient[0]), int(nutrient[1])), 5)

        # Optional: visualize chemical concentration as a gradient (for debugging)
        for x in range(self.width):
            for y in range(self.height):
                color = int(self.chemical_map[x, y] * 255)
                pygame.draw.rect(screen, (color, color, color), pygame.Rect(x, y, 1, 1))
