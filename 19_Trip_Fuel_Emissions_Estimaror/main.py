"""
PROJECT:VEHICLE TRIP FUEL & EMISSIONS REPORT
Description:This project takes trip distance,fuel type,fuel consumption rate to calculate fuel used,cost and emissions.Then to display everything as a well formatted result.
"""
fuel_price_per_litre= {'petrol':194.50,'diesel':178.20}
co2_per_litre_kg= {'petrol':2.31,'diesel':2.68}
#Function to calculate fuel used in litres
def calculate_fuel_used(distance_km,consumpion_per_l_100):
    return distance_km * (consumpion_per_l_100/100)

#Function to calculate cost of fuel
def calculate_fuel_cost(litres_used,fuel_type):
    price_per_l=fuel_price_per_litre[fuel_type]
    return litres_used * price_per_l

#Function to calculate emissions
def calculate_emissions(litres_used,fuel_type):
    co2_per_litre=co2_per_litre_kg[fuel_type]
    return litres_used * co2_per_litre

def generate_report(distance_km,litres_used,cost,emissions_kg):
    print('---------TRIP REPORT---------')
    print(f'Distance : {distance_km:.2f}km')
    print(f'Fuel Used : {litres_used:.2f}L')
    print(f'Fuel Cost :KES {cost:.2f}')
    print(f'CO2 Emissions : {emissions_kg:.2f}kg')


ask_distance=float(input('Enter distance in km: '))
ask_consumption=float(input('Enter fuel consumption rate (L/100km): '))
ask_type=input('Enter Fuel Type: ').strip().lower()
while ask_type not in fuel_price_per_litre:
    print('Invalid fuel type.Please enter petrol or diesel')
    ask_type=input('Enter Fuel Type: ').strip().lower()


litres=calculate_fuel_used(ask_distance,ask_consumption)
cost=calculate_fuel_cost(litres,ask_type)
emissions=calculate_emissions(litres,ask_type)
generate_report(ask_distance,litres,cost,emissions)

