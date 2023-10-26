import random
import numpy as np
from scipy.integrate import odeint
from QuantumSimulator import QuantumSimulator
from ParticleMotion import ParticleMotion

class Metropolis:
    
    def __init__(self, quantum_simulator, particle_motion, num_bins, box_length):
        self.quantum_simulator = quantum_simulator
        self.particle_motion = particle_motion
        self.num_bins = num_bins
        self.box_length = box_length

    def potential_energy(self, x):
        return 0.5 * (x - self.box_length / 2) ** 2
    
    def simulate(self, num_steps, time_step, quantum_probabilities, surface_interaction_probability, potential_energy = False):
        positions = []

        initial_velocity = random.uniform (0, 1.0)
        quantum_simulator_instance = QuantumSimulator(self.num_bins, self.box_length)
        current_position = quantum_simulator_instance.initialize_position_with_rejection_sampling()
        current_velocity = initial_velocity
        
        particle_simulator = ParticleMotion(self.box_length, mass = 1, surface_interaction_probability = 0.1)
        quantum_levels, quantum_probabilities = quantum_simulator_instance.quantum_energy_levels(self.num_bins, self.box_length)

        for step in range(num_steps):
            # Sample a quantum state
            n = random.choices(range(1, self.num_bins + 1), quantum_probabilities)[0]

            # Update position and velocity based on the ODE integration
            time_points = np.linspace(0, time_step, 2)
            ode_solution = odeint(particle_simulator.particle_motion, [current_position, current_velocity], time_points)
            current_position, current_velocity = ode_solution[-1]

            # Probabilistic surface interaction
            if random.random() < surface_interaction_probability:
                if random.random() < 0.5:
                    # Specular reflection (reverse velocity)
                    current_velocity = -current_velocity
                else:
                    # Diffuse reflection (randomize velocity)
                    current_velocity = random.uniform(-1.0, 1.0)
            

            # Calculate the energy based on the quantum state
            current_energy = quantum_levels[n - 1]

            # Calculate the energy difference
            if potential_energy:
                proposed_energy = current_energy + self.particle_motion.potential_energy(current_position)
            else:
                proposed_energy = current_energy

            energy_difference = proposed_energy - current_energy

            # Metropolis acceptance/rejection step
            if energy_difference <= 0 or random.random() < np.exp(-energy_difference / 1):
                # Accept the move
                current_position = current_position

            # Store the accepted position
            positions.append(current_position)

        return positions
