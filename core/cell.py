import numpy as np

class AmoebaCell:
    def __init__(self, initial_position):
        self.position = np.array(initial_position, dtype=float)
        self.pseudopods = [np.array(initial_position, dtype=float) for _ in range(5)]  # 5 pseudopods
        self.velocity = np.zeros_like(self.position)
    
    def update_position(self, forces):
        # Apply forces to move the cell
        self.velocity += forces
        self.position += self.velocity
        
        # Update pseudopods movement (simple model)
        for i, pod in enumerate(self.pseudopods):
            self.pseudopods[i] = self.position + 0.1 * (np.random.rand(2) - 0.5)

    def get_shape(self):
        return [self.position] + self.pseudopods
