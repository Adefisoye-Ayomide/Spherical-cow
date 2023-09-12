#We first set up the initial conditions and constants
g = 9.8  
m = 1000.0  #Mass of the cow (kg) 
x = 0.0  #Initial x position (m)
y = h = 100.0  #Initial y position we chose (m)
vx = 10.0  #Initial x velocity (m/s)
vy = 0.0  #Initial y velocity (m/s)
constant_wind_resistance = 0.1  #we assumed this value for wind resistance constant
dt = 0.01  #Time step size (s)

#Function 1 which returns the total forces on the cow
def total_force(x, y, vx, vy, constant):
    #Gravitational force
    fx = 0.0
    fy = -m * g
    
    #Wind resistance force
    v = (vx**2 + vy**2)**0.5
    wind_resistance = -constant * v**2
    fx += wind_resistance 
    fy += wind_resistance 
    
    return fx, fy

#Function 2 which returns the updated position and velocity of cow at time t
def update_position_velocity(x, y, vx, vy, fx, fy, dt):
    #Calculate acceleration
    ax = fx / m
    ay = fy / m
    
    #Update velocity using the acceleration
    new_vx = vx + ax * dt
    new_vy = vy + ay * dt
    
    #Update position using the new velocity
    new_x = x + new_vx * dt
    new_y = y + new_vy * dt
    
    return new_x, new_y, new_vx, new_vy

#Function 3 which returns potential energy and kinetic energy of the cow
def calculate_energy(x, y, vx, vy):
    #Calculate potential energy
    potential_energy = m * g * y
    
    #Calculate kinetic energy
    kinetic_energy = 0.5 * m * (vx**2 + vy**2)
    
    #Total energy is the sum of potential and kinetic energy
    total_energy = potential_energy + kinetic_energy
    
    return potential_energy, kinetic_energy, total_energy

time = 0.0

while y > 0.0: #This condition is to stop the simulation when the cow hits the ground. i.e. when y <=0
    fx, fy = total_force(x, y, vx, vy, constant_wind_resistance)
    x, y, vx, vy = update_position_velocity(x, y, vx, vy, fx, fy, dt)
    potential_energy, kinetic_energy, total_energy = calculate_energy(x, y, vx, vy)
    time += dt

print("The simulation ended at time:", time)
print("Final x position:", x)
print("Final y position:", y)
print("Final x velocity:", vx)
print("Final y velocity:", vy)
print("Final potential energy:", potential_energy)
print("Final kinetic energy:", kinetic_energy)
print("Final total energy:", total_energy)
