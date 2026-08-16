"""
PROJECT:VEHICLE BRAKING SIMULATOR
DESCRIPTION:Simulates vehicle braking distance and decceleration time 

"""

print('='*25)
print('VEHICLE BRAKING SIMULATOR')
print('='*25)

#VEHICLE INPUTS
mass=float(input('Enter vehicle mass (kg): '))
friction_coefficient=float(input('Enter tyre-road friction coefficient: '))
air_density=float(input('Enter air density (kg/m^3): '))
downforce_coefficient=float(input('Enter downforce coefficient(Cl): '))
aero_area=float(input('Enter aerodynamic area (frontal area m^2): '))
initial_speed_kmh=float(input('Enter initial speed (km/h): '))

g=9.81

#UNIT CONVERSION
initial_speed_ms=initial_speed_kmh * (10/36)

velocity=initial_speed_ms
distance=0.0
time=0.0
time_step=0.01

while velocity >0:
    #calculate downforce
    downforce=0.5*air_density*downforce_coefficient*aero_area*(velocity**2)
    #normal force
    normal_force=(mass*g) + downforce
    #braking force
    braking_force=friction_coefficient * normal_force
    #decceleration
    decceleration=braking_force/mass
    #distance travelled during braking
    distance=distance + velocity*time_step #####
    #update velocity
    velocity=velocity-decceleration*time_step
    decceleration_g=decceleration/g
    if velocity<0:
        velocity=0   #prevent negative velocity

    #update time
    time=time +time_step

print('-----RESULTS-----')
print(f'Initial speed: {initial_speed_kmh:.2f}km/h')
print(f'Braking Distance: {distance:.2f}m')
print(f'Braking Time: {time:.2f}s')
print(f'Final Downforce:{downforce:.2f}')
print(f'Final Decceleration:{decceleration_g:.1f}g')
