"""
Project:Braking Distance Calculator
Description:Calculates braking distance,reaction distance & stopping distance

"""

print('='*25)
print('BRAKING DISTANCE CALCULATOR')
print('='*25)
speed=float(input('Enter Vehicle speed (km/h): '))
mu=float(input('Enter Coefficient of Friction (u): '))
reaction_time=float(input('Enter reaction time(s):'))

g=9.81
speed_ms=speed/3.6
reaction_distance=speed_ms * reaction_time
braking_distance=(speed_ms**2)/(2*mu*g)
total_distance=reaction_distance + braking_distance

print('='*25)
print('\nRESULTS')
print('='*25)
print(f'Reaction Distance:{reaction_distance:.2f}m')
print(f'Braking Distance:{braking_distance:.2f}m')
print(f'Stopping Distance:{total_distance:.2f}m')

#Basic Race Engineering commentary
if total_distance <40:
    print('Excellent braking performance')

elif total_distance >40 and total_distance <70:
    print('Average braking performance')

elif total_distance > 70:
    print('Long stopping distance-Drive with caution')
##