"""
PROJECT:Brake Pad Wear & Safety Margin Calculator
Description:Measure brake pad thickness over time,calculate wear rate,and determine a safety margin/warning level

"""
new_pad_thickness=12.0
min_pad_thickness=3.0

#Brake Data
brakes= {
    'front_left':{'thickness_mm':7.5,'mileage_km':22000},
    'front_right':{'thickness_mm':7.2,'mileage_km':22000},
    'rear_left':{'thickness_mm':9.0,'mileage_km':22000},
    'rear_right':{'thickness_mm':8.8,'mileage_km':22000}
}

#1.Calculate brake pad wear rate
def calculate_percent_worn(brake_name):
    brake_data=brakes[brake_name]
    brake_thickness=brake_data['thickness_mm']
    
    percent_worn=(new_pad_thickness-brake_thickness)/new_pad_thickness * 100
    return percent_worn

#Obtain safety margins
def get_safety_margin(percent_worn):
    #safety margins
    if percent_worn > 35:
        return 'PAD REPLACEMENT URGENT'
    elif percent_worn > 20 and percent_worn <= 34:
        return 'OK'
    else:
        return 'GOOD CONDITION'

choice=input('Enter brake position (or \'all\') for all positions: ').strip().lower()
if choice == 'all':
    for name in brakes:
        worn=calculate_percent_worn(name)
        margin=get_safety_margin(worn)
        print(f'{name}:{worn:.1f}%-worn out:{margin}')
elif choice in brakes:
    worn=calculate_percent_worn(choice)
    margin=get_safety_margin(worn)
    print(f'{choice}:{worn:.1f}%-worn out:{margin}')
else:
    print('Brake Position not found.')
    
