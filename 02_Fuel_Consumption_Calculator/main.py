"""
Project:Fuel Consumption Calculator
Author:Erick Kirobi

Description:Calculates fuel economy and fuel consumption
"""
print('='*25)
print('FUEL CONSUMPTION CALCULATOR')
print('='*25)
distance=float(input('Enter distance travelled (km): '))
fuel=float(input('Enter fuel used (L): '))
price_per_litre=float(input('Enter Price per litre:'))
total_fuel_price=fuel*price_per_litre
km_per_litre=distance/fuel
litres_per_100km=(fuel/distance) * 100
print(f'\nDistance:{distance:.1f} km')
print(f'Fuel Used :{fuel:.2f} L')
print(f'Fuel Economy:{km_per_litre:.2f}km/L')
print(f'Fuel Consumption :{litres_per_100km:.2f} L/km')
print(f'Total Fuel Cost:ksh {total_fuel_price:.2f}')