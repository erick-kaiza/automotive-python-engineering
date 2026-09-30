import math
"""
PROJECT : TYRE SIZE DECORDER & SPEEDOMETER ERROR CALCULATOR
Description:The project takes in a tyre's dimensions and calculates how wrong the speedometer becomes when someone fits in a new tyre

"""

def read_tyre(prompt):
    while True :
        text = input(prompt).strip().upper().replace(' ','')
        try:
            width,rest = text.split('/')
            ratio,rim = rest.split('R')
            width,ratio,rim = int(width),int(ratio) ,int(rim)
            if width <=0 or ratio <= 0 or rim <=0:
                 raise ValueError
            return width,ratio,rim
        except ValueError:
            print('Invalid,enter with format eg (195/65R15)')

width,ratio,inches = read_tyre('Enter original tyre size: ')
width1,ratio1,inches1 = read_tyre('Enter new tyre size:')
            
def calculate_overall_diameter(width,ratio,inches):
#Calculate Tyre diameters
    sidewall_mm = width * ratio/100
    rim_diameter_mm = inches * 25.4
    overall_diameter_mm = rim_diameter_mm + (2*sidewall_mm)
    return overall_diameter_mm

original_diameter = calculate_overall_diameter(width,ratio,inches)
new_diameter = calculate_overall_diameter(width1,ratio1,inches1)
#Calculate speedometer error
speeds = [60,100,120]
real_speeds = []
print('Actual Speeds')
for speed in speeds:
    real_speed = speed * (new_diameter/original_diameter)
    real_speeds.append(real_speed)

for speed in real_speeds:
    print(f'{speed:.2f}km/h')

difference =((real_speeds[0]-speeds[0])/speeds[0]) * 100 #since the increase in speedometer is equal across all speeds,just one sample of the two values can be taken.
print(f'Original tyre diameter: {original_diameter:.2f}mm')
print(f'New tyre diameter: {new_diameter:.2f}mm')
print(f'{difference:.2f}% change in real speed.')

diameter_difference = ((new_diameter - original_diameter)/original_diameter)*100 #this matches the percantage change in real speed since real speed is just the original speed multiplied by the diameter ratio.
if diameter_difference > 3:
    print('Limits Exceeded.Speedometer reading affected!')
else:
    print(f'{diameter_difference:.2f}% change in diameter.')




    

        




