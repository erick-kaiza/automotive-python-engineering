"""
Project :Engine Performance Calculator
Author:Erick Kirobi
Description:Calculates engine horsepower from torque and rpm.
"""
print('ENGINE PERFORMANCE CALCULATOR')
print('-'*20)

torque=float(input('Enter engine torque (Nm): '))
rpm=float(input('Enter engine speed (rpm): '))
horsepower=(torque * rpm)/7127
kilowatt=horsepower * 0.7457
print(f'\nEngine Speed:{rpm:.0f}')
print(f'Engine torque:{torque} Nm')
print(f'Horsepower :{horsepower:.1f} HP')
print(f'Engine Power:{kilowatt:.1f} kW')