import math
"""
Project:Gear Ratio Analyzer
Author:Erick Kirobi

Description:Calculates wheel RPM and vehicle speed

"""

print('='*20)
print('GEAR RATIO ANALYZER')
print('='*20)

engine_rpm=float(input('Enter Engine RPM: '))
gear_ratio=float(input('Enter Gear Ratio: '))
final_drive=float(input('Enter Final Drive Ratio: '))
tire_diameter=float(input('Enter Tire Diameter(m): '))

overall_ratio=gear_ratio * final_drive
wheel_rpm=engine_rpm/(gear_ratio*final_drive)
wheel_circumfrence=math.pi * tire_diameter
speed=wheel_rpm * wheel_circumfrence * (60/1000)

print('\nRESULTS🏁🏁')
print('-'*20)
print(f'Overall Gear Ratio:{overall_ratio:.2f}')
print(f'Wheel speed : {wheel_rpm:.1f} RPM')
print(f'Vehicle Speed : {speed:.1f} km/h')
