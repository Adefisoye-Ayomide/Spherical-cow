import numpy as np
import random

class QuantumSimulator:
    def __init__(self, num_bins, box_length):
        self.num_bins = num_bins
        self.box_length = box_length
        
        

    def quantum_energy_levels(self, num_bins, box_length):
        levels = []
        probabilities = []
        hbar = 1.0545718e-34  # Planck's constant divided by 2π
        total_energy = 0.0
        

        for n in range(1, num_bins + 1):
            level_energy = (n**2 * np.pi**2 * hbar**2) / (2 * self.box_length**2)
            levels.append(level_energy)
            total_energy += level_energy

        for energy in levels:
            probability = energy / total_energy
            probabilities.append(probability)

        return levels, probabilities
    
    def non_uniform_probability_distribution(self, x):
        return 2.0 * np.exp(-2.0 * x)

    def initialize_position_with_rejection_sampling(self):
        while True:
            x = random.uniform(0,1)
            proposed_position = random.uniform(0, self.box_length)
            acceptance_probability = 2.0 * np.exp(-2.0 * x)
            if random.random() < acceptance_probability:
                return proposed_position

   
