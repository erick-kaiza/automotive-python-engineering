"""
PROJECT:VEHICLE ACCELERATION SIMULATOR

DESCRIPTION:Calculate a vehicles acceleration using parameters:rolling resistance and Tractive effort

"""

print('='*25)
print('VEHICLE ACCELERATION SIMULATOR')
print('='*25)

#USER INPUTS
mass=float(input('Enter vehicle mass (kg): '))
tractive_force=float(input('Enter tractive force (N): '))
rolling_coefficient=float(input('Enter coefficient of rolling resistance: '))

g=9.81  # acceleration due to garavity

#CALCULATIONS
rolling_resistance=rolling_coefficient * mass * g
net_force=tractive_force-rolling_resistance
acceleration=net_force/mass     #From Newton's second law F=ma

time=0.0
velocity=0.0
time_step=0.1   #Change in time

print('\n-------RESULTS---------')
print(f'Rolling resistance: {rolling_resistance:.1f}N')
print(f'Net Force (on the wheel): {net_force:.1f}N')
print(f'Acceleration:{acceleration:.2f}m/s^2')

#CALCULATE TIME TO REACH 100km/h (27.78 m/s)
while velocity <27.78:
    velocity=velocity+ (acceleration * time_step)  #Acceleration is change in velocity,new velocity will be initial velocity + acceleration * change in time.
    time=time + time_step

print(f'0-100 km/h time: {time:.2f}s')
