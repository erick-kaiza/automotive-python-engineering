"""
Project: Tire Wear & Replacement predictor
Tracks tread depth and mileage for all four tires on a vehicle,calculates wear rate per 1000km,and predicts remaining mileage before each tire hits the legal minimum tread depth (1.6mm)

"""

#legal minimum tread depth
min_tread_depth= 1.6
#original tread depth
og_tread_depth=8.0

#Tire data
tires={
    'front_left':{'tread mm':5.2,'mileage_km':18000},
    'front_right':{'tread mm':5.0,'mileage_km':18000},
    'rear_left':{'tread mm':6.1,'mileage_km':18000},
    'rear_right':{'tread mm':6.3,'mileage_km':18000}
}

#function to calculate tire tread depth wear rate
def calculate_wear_rate(wheel_name):
    tire_data=tires[wheel_name]
    current_tread_mm=tire_data['tread mm']
    mileage_km=tire_data['mileage_km']
    wear_rate=(og_tread_depth-current_tread_mm)/mileage_km *1000
    return wear_rate
#function to display wear rate
def display_result(wheel_name):
    rate=calculate_wear_rate(wheel_name)
    print(f'{wheel_name}:{rate:.2f}mm/1000km')
    remaining_km=predict_remaining_km(wheel_name)
    tire_status=classify_status(wheel_name)

    print(f'Remaining Tire kilometers: {remaining_km:.2f}km')
    print(f'Tire Status:{tire_status}.')

#function to predict remaining km
def predict_remaining_km(wheel_name):
    tire_data=tires[wheel_name]
    Current_tread_mm=tire_data['tread mm']
    wear_rate=calculate_wear_rate(wheel_name)

    tread_remaining=Current_tread_mm - min_tread_depth
    remaining_km=(tread_remaining/wear_rate) * 1000
    return remaining_km

#function to classify status of tire
def classify_status(wheel_name):
    remaining_km=predict_remaining_km(wheel_name)

    if remaining_km < 2000:
        return 'URGENT REPLACEMENT'
    elif remaining_km < 8000:
        return 'REPLACE SOON'
    else:
        return 'OK'

choice=input('Enter wheel name (or \'all\' for all tires): ').strip().lower()
if choice == 'all':
    for name in tires:
        display_result(name)
elif choice in tires:
    display_result(choice)
else:
    print('Wheel not found:Try front_left,front_right,rear_left,rear_right')




    