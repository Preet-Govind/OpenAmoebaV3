import numpy as np

class PhysicsEngine:
    def __init__(self, num_particles, stiffness=0.2, damping=0.85, mass=1.0):
        self.num_particles = num_particles
        self.stiffness = stiffness
        self.damping = damping
        self.mass = mass
        self.positions = np.random.rand(num_particles, 2) * 100  # Random initial positions
        self.velocities = np.zeros_like(self.positions)
        self.forces = np.zeros_like(self.positions)
        self.rest_lengths = np.linalg.norm(self.positions - np.roll(self.positions, 1, axis=0), axis=1)  # Rest lengths of the springs

    def apply_forces(self, movement_vector):
        # Apply neural controller output as a directional force to all particles
        for i in range(self.num_particles):
            self.forces[i] += movement_vector * 0.1  # Apply the movement vector as a force (scaled)

        # Calculate internal forces and spring forces
        for i in range(self.num_particles):
            next_index = (i + 1) % self.num_particles
            prev_index = (i - 1) % self.num_particles

            # Spring forces from neighboring points
            force_next = self.spring_force(i, next_index)
            force_prev = self.spring_force(i, prev_index)

            self.forces[i] += force_next + force_prev

        # Apply damping (friction)
        self.velocities *= self.damping

    def spring_force(self, i, j):
        displacement = self.positions[j] - self.positions[i]
        distance = np.linalg.norm(displacement)
        direction = displacement / (distance + 1e-6)  # Normalize, prevent division by zero
        stretch = distance - self.rest_lengths[i]
        force = self.stiffness * stretch * direction
        return force

    def update_positions(self, dt):
        # Integrate forces to update velocity and positions (Euler integration)
        accelerations = self.forces / self.mass
        self.velocities += accelerations * dt
        self.positions += self.velocities * dt
        self.forces.fill(0)  # Reset forces for the next step

    def get_shape(self):
        return self.positions

    def simulate_step(self, movement_vector, dt):
        self.apply_forces(movement_vector)
        self.update_positions(dt)
