"""
Project:Engine Coolant Temperature Monitor
Description:To simulate a coolant temperature sensor reading and classify it into statutus zones,normal,high,danger,critical

"""

def check_coolant_temp(temp_celsius):

    if temp_celsius >=90 and temp_celsius <=105:
        print('Normal')
    elif  temp_celsius >105 and temp_celsius <=150:
        print('High ⚠️')
    elif temp_celsius > 150:
        print('Critical 💀')
    elif temp_celsius <90:
        print('Engine too cold!')

while True:
    reading=input('Enter Coolant Temperature (celsius) or (q) to exit: ')
    if reading.lower() == 'q':
        print('Thank you,Drive Safe!')
        break
    try:
        temp=float(reading)
        check_coolant_temp(temp)
    except ValueError:
        print('Invalid Input-Please enter a number or q to quit.')
