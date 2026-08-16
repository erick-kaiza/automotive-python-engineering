import math
"""
PROJECT:VEHICLE ACCELERATION & TRACTION CALCULATOR
DESCRIPTION:The program calculates maximum acceleration available from tyre-road traction,downforce included

"""

print('='*25,'\nTRACTION AND ACCELERATION CALCULATOR\n','='*25)

#USER INPUT
mass=float(input('Enter vehicle mass (kg): '))
friction_coefficient=float(input('Enter tyre-road friction coefficient: '))
air_density=float(input('Enter air density(kg/m^3): '))
downforce_coefficient=float(input('Enter downforce coefficient(Cl): '))
frontal_area=float(input('Enter frontal area (m^2): '))
initial_speed_kmh=float(input('Enter initial speed(km/h): '))
target_speed_kmh=float(input('Enter target speed(km/h): '))

g=9.81

#CONVERSION OF KM/H-m/s
initial_speed_ms=initial_speed_kmh *(10/36)
target_speed_ms=target_speed_kmh *(10/36)
time=0.0
velocity=initial_speed_ms
time_step=0.01
#CALCULATIONS
while velocity < target_speed_ms:
    downforce=0.5*air_density*downforce_coefficient*frontal_area*(velocity**2)
    normal_force=(mass *g) + downforce
    traction_force=friction_coefficient * normal_force
    acceleration=traction_force/mass
    velocity=velocity + acceleration * time_step
    time=time + time_step
    acceleration_g=acceleration/g

print('\n-----RESULTS-----')
print(f'Normal force:{normal_force:.1f}N')
print(f'Final Downforce:{downforce:.2f}N')
print(f'Maximum Traction Force:{traction_force:.1f}N')
print(f'Maximum acceleration:{acceleration:.1f}m/s^2')
print(f'Acceleration:{acceleration_g:.2f}g')
print(f'Estimated time to target speed:{time:.2f}s')

