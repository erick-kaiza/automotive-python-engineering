import math

print('='*25)
print('GEAR & VEHICLE SPEED SIMULATOR')
print('='*25)

#VEHICLE INPUTS
engine_rpm=float(input('Enter engine speed (rpm): '))
max_rpm=float(input('Enter maximum engine RPM: '))
final_drive=float(input('Enter Final Dreive ratio: '))
tyre_diameter=float(input('Enter tyre diameter (m): '))

#GEAR RATIOS
gear_ratios=[3.50,2.20,1.50,1.00,0.80]

#CALCULATIONS
tyre_circumfrence=math.pi * tyre_diameter

print('----------VEHICLE SPEED BY GEAR----------')

for gear_number,gear_ratio in enumerate(gear_ratios,start=1):
    wheel_rpm=engine_rpm/(gear_ratio * final_drive)
    speed_ms=wheel_rpm*tyre_circumfrence/60
    speed_kmh=speed_ms * 3.6

    print(f'Gear {gear_number}:{speed_kmh:.1f}km/h.')

print('----------MAXIMUM SPEED IN EACH GEAR----------')

for gear_number,gear_ratio in enumerate(gear_ratios,start=1):
    wheel_rpm=max_rpm/(gear_ratio * final_drive)
    speed_ms=wheel_rpm*tyre_circumfrence/60
    speed_kmh=speed_ms * 3.6

    print(f'Gear {gear_number}:{speed_kmh:.1f}km/h.')



print('----------RPM AFTER UPSHIFT----------')
for i in range(len(gear_ratios)-1):
    current_ratio=gear_ratios[i]
    next_ratio=gear_ratios[i+1]
    rpm_after_shift=max_rpm * (next_ratio/current_ratio)
    print(f'Gear {i+1} -> Gear {i+2}:{rpm_after_shift:.0f}RPM')