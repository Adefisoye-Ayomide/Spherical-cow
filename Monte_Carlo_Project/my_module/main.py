import numpy as np
import random
import matplotlib.pyplot as plt
from QuantumSimulator import QuantumSimulator
from ParticleMotion import ParticleMotion
from MonteCarlo import Metropolis

# Defining parameters
box_length = 10  # Length of the 1D box
temperature = 1.0  # Temperature for the simulation
num_steps = 100000  # Number of Metropolis steps
num_bins = 50  # Number of bins
mass = 1.0  # Mass of the particle
surface_interaction_probability = 0

# Sample initial velocity randomly
initial_velocity = random.uniform(0, 1.0)

# Define a non-uniform probability distribution function
def non_uniform_probability_distribution(x):
    return 2.0 * np.exp(-2.0 * x)

# Sample initial position using rejection sampling
while True:
    proposed_position = random.uniform(0, box_length)
    acceptance_probability = non_uniform_probability_distribution(proposed_position)
    if random.random() < acceptance_probability:
        initial_position = proposed_position
        break

def potential_energy(x):
        return 0.5 * (x - box_length / 2) ** 2


quantum_simulator = QuantumSimulator(num_bins, box_length)
particle_motion = ParticleMotion(mass, surface_interaction_probability, box_length)
metropolis_simulator = Metropolis(quantum_simulator, particle_motion, num_bins, box_length)


current_position = initial_position

# Call the potential_energy method from the ParticleMotion class
potential_energy_value = particle_motion.potential_energy(current_position)

# Define the quantum energy levels and associated probabilities
quantum_levels, quantum_probabilities = quantum_simulator.quantum_energy_levels(num_bins, box_length)

# Call the simulate method for different scenarios
positions_potential_and_surface = metropolis_simulator.simulate(num_steps, 0.01, quantum_probabilities, 0.1, potential_energy_value)
positions_surface_interaction = metropolis_simulator.simulate(num_steps, 0.01, quantum_probabilities, 0.1)
positions_harmonic_potential = metropolis_simulator.simulate(num_steps, 0.01, quantum_probabilities, 0, potential_energy_value)

# Create histograms for each scenario
hist_potential_and_surface, bins_potential_and_surface = np.histogram(positions_potential_and_surface, bins=num_bins, range=(0, box_length), density=True)
hist_surface_interaction, bins_surface_interaction = np.histogram(positions_surface_interaction, bins=num_bins, range=(0, box_length), density=True)
hist_harmonic_potential, bins_harmonic_potential = np.histogram(positions_harmonic_potential, bins=num_bins, range=(0, box_length), density=True)

# Calculate bin centers for plotting
bin_centers_potential_and_surface = 0.5 * (bins_potential_and_surface[1:] + bins_potential_and_surface[:-1])
bin_centers_surface_interaction = 0.5 * (bins_surface_interaction[1:] + bins_surface_interaction[:-1])
bin_centers_harmonic_potential = 0.5 * (bins_harmonic_potential[1:] + bins_harmonic_potential[:-1])

# Create plots in separate figures
plt.figure(figsize=(8, 6))
plt.hist(positions_potential_and_surface, bins=num_bins, range=(0, box_length), density=True, alpha=0.7, color='g')
plt.plot(bin_centers_potential_and_surface, hist_potential_and_surface, 'ro-')
plt.xlabel('Position (m)')
plt.ylabel('Probability')
plt.title('Harmonic Potential and Surface Interaction')

# Create plots
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.hist(positions_potential_and_surface, bins=num_bins, range=(0, box_length), density=True, alpha=0.7, color='g')
plt.plot(bin_centers_potential_and_surface, hist_potential_and_surface, 'ro-')
plt.xlabel('Position (m)')
plt.ylabel('Probability')
plt.title('Harmonic Potential and Surface Interaction')

plt.subplot(2, 2, 2)
plt.hist(positions_surface_interaction, bins=num_bins, range=(0, box_length), density=True, alpha=0.7, color='m')
plt.plot(bin_centers_surface_interaction, hist_surface_interaction, 'ro-')
plt.xlabel('Position (m)')
plt.ylabel('Probability')
plt.title('Surface Interaction Only')

plt.subplot(2, 2, 3)
plt.hist(positions_harmonic_potential, bins=num_bins, range=(0, box_length), density=True, alpha=0.7, color='c')
plt.plot(bin_centers_harmonic_potential, hist_harmonic_potential, 'ro-')
plt.xlabel('Position (m)')
plt.ylabel('Probability')
plt.title('Harmonic Potential Only')

plt.tight_layout()
plt.show()
