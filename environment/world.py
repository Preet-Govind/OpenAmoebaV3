import numpy as np

class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.nutrients = [np.random.rand(2) * [width, height] for _ in range(10)]

    def get_sensory_input(self, amoeba_position):
        distances = [np.linalg.norm(amoeba_position - nutrient) for nutrient in self.nutrients]
        closest_nutrient = self.nutrients[np.argmin(distances)]
        return closest_nutrient - amoeba_position

    def update_environment(self):
        # Nutrients could randomly move or new ones could appear
        pass
