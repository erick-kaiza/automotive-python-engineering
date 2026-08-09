"""
PROJECT:Wheel Torque Calculator

DESCRIPTION:Calculates torque available at the whee,neglecting losses eg friction,gear losses,from engine torque,driveline efficiency,transmission ratio,final drive ratio.

"""

print('='*25)
print('WHEEL TORQUE CALCULATOR')
print('='*25)

#USER INPUT
engine_torque=float(input('Enter Engine torque (Nm): '))
gear_ratio=float(input('Enter gear ratio: '))
final_drive_ratio=float(input('Enter Final Drive Ratio: '))
efficiency=float(input('Enter Driveline Efficiency: '))

print('TRACTIVE FORCE CALCULATOR')
rolling_radius=float(input('Enter rolling radius (m): '))

#CALCULATIONS
efficiency_decimal=efficiency/100
wheel_torque=(engine_torque
              *gear_ratio
              *final_drive_ratio
              *efficiency_decimal)
tractive_force=wheel_torque/rolling_radius

#OUTPUT
print('\nRESULTS')
print('-'*25)
print(f'Wheel torque : {wheel_torque:.2f}Nm')
print(f'Tractive Force :{tractive_force:.2f}N')