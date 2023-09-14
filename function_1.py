import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.8  # Gravitational acceleration (m/s^2)

# Initial conditions
m = 1000.0  # Mass of the cow (kg)
r = 1.0  # Radius of the cow (m)
x = 0.0  # Initial x position (m)
y = 1000.0  # Initial y position (m)
vx = 1.0  # Initial x velocity (m/s)
vy = 100.0  # Initial y velocity (m/s)
constant_wind_resistance = 0.0  # Selectable constant for wind resistance

# Time settings
dt = 0.001  # Time step size (s)

# Functions
def total_force(x, y, vx, vy, constant):
    # Calculate gravitational force
    fx = 0.0
    fy = -m * g
    
    # Calculate wind resistance force
    v = (vx**2 + vy**2)**0.5
    wind_resistance = -constant * v**2 
    fx += wind_resistance 
    fy += wind_resistance
    
    return fx, fy

def update_position_velocity(x, y, vx, vy, fx, fy, dt):
    # Calculate acceleration
    ax = fx / m
    ay = fy / m
    
    # Update velocity using the acceleration
    new_vx = vx + ax * dt
    new_vy = vy + ay * dt
    
    # Update position using the new velocity
    new_x = x + new_vx * dt
    new_y = y + new_vy * dt
    
    return new_x, new_y, new_vx, new_vy

def calculate_energy(x, y, vx, vy):
    # Calculate potential energy
    potential_energy = m * g * y
    
    # Calculate kinetic energy
    kinetic_energy = 0.5 * m * (vx**2 + vy**2)
    
    # Total energy is the sum of potential and kinetic energy
    total_energy = potential_energy + kinetic_energy
    
    return potential_energy, kinetic_energy, total_energy

# Simulation
time = 0.0
list = []
#list[0] = (0,0,1000)
while y > 0.0:
    fx, fy = total_force(x, y, vx, vy, constant_wind_resistance)
    x, y, vx, vy = update_position_velocity(x, y, vx, vy, fx, fy, dt)
    list.append((dt, x, y))
    potential_energy, kinetic_energy, total_energy = calculate_energy(x, y, vx, vy)
    time += dt

#print(list)
headers = ['Time', 'position_x', 'position_y']
np.savetxt("lst.txt", list, delimiter='\t', fmt='%0.3f', header = '\t'.join(headers))
print("Simulation ended at time:", time)
print("Final x position:", x)
print("Final y position:", y)
print("Final x velocity:", vx)
print("Final y velocity:", vy)
print("Final potential energy:", potential_energy)
print("Final kinetic energy:", kinetic_energy)
print("Final total energy:", total_energy)
