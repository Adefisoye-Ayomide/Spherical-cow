import random
import numpy as np

class ParticleMotion:
    def __init__(self, box_length, mass, surface_interaction_probability):
        self.mass = mass
        self.surface_interaction_probability = surface_interaction_probability
        self.box_length = box_length

    def potential_energy(self, x,):
        return 0.5 * (x - self.box_length / 2) ** 2

    def particle_motion(self, y, t):
        position, velocity = y
        force = -1* (position - self.box_length / 2)
        acceleration = force / self.mass

        if random.random() < self.surface_interaction_probability:
            if random.random() < 0.5:
                # Specular reflection (reverse velocity)
                velocity = -velocity
            else:
                # Diffuse reflection (randomize velocity)
                velocity = random.uniform(-1.0, 1.0)

        return [velocity, acceleration]
