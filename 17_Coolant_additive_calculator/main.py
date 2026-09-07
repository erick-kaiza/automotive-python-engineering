"""
PROJECT:COOLANT/OIL ADDITIVE RATIO RATIO CALCULATOR
Description :Calculate how much concentrate vs water to mix for a target coolant ratio .

"""
#Function for calculation
def calculate_mix(total_litres,concentrate_ratio=0.5):
    concentrate_litre=total_litres * concentrate_ratio
    water_litres=total_litres-concentrate_litre
    return concentrate_litre,water_litres

ask_litres= float(input('Enter total litres of coolant mixture(L): '))
concentrate,water=calculate_mix(ask_litres)
print(f'Concentrate:{concentrate:.2f}L\nWater:{water:.2f}L')
#Trying to overrun the default parameter(play around with the concentrate ratio)
concentrate2,water2=calculate_mix(ask_litres,0.6)
print(f'Concentrate 2:{concentrate2:.2f}L\nWater 2:{water2:.2f}L')


