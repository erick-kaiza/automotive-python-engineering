"""
PROJECT:TIRE CONTACT PATCH & LOAD ESTIMATOR
Description:A simplified way to estimate a tire's contact patch area and the load it can supprt,given tire width,aspect ratio and inflation pressure

"""

#Fuction to determine sidewall height & overall tire diameter
def calculate_tire_dimension(width_mm,aspect_ratio,rim_diameter_in):
    sidewall_height_mm= width_mm * (aspect_ratio/100)
    overall_diameter= (sidewall_height_mm * 2) + (rim_diameter_in * 25.4)
    return sidewall_height_mm,overall_diameter

#Function to estimate contact patch area
def estimate_contact_patch(width_mm,pressure_kpa,load_kg):
    load_n= load_kg * 9.81
    pressure_pa= pressure_kpa * 1000
    contact_area_m2= load_n/pressure_pa
    contact_area_cm2= contact_area_m2 * 10000
    width_m= width_mm/1000
    return width_m,contact_area_cm2
#Ask User for physics parameters
ask_width=float(input('Enter Tire width (mm): '))
ask_ratio=float(input('Enter aspect ratio: '))
ask_diameter=float(input('Enter rim diameter (in): '))
ask_inflation_pressure=float(input('Enter inflation pressure (kPa): '))
ask_tire_load=float(input('Enter tire load (kg): '))

#Unpacking function return values
height,diameter=calculate_tire_dimension(ask_width,ask_ratio,ask_diameter)
height_m,contact_patch_area=estimate_contact_patch(height,ask_inflation_pressure,ask_tire_load)

#Display results
print('-'*25)
print('RESULTS')
print('-'*25)
print(f'Sidewall height:{height:.2f}mm\nSidewall Height:{height_m:.2f}m\nOverall Tire Diameter:{diameter:.2f}mm\nEstimated contact patch area:{contact_patch_area:.2f}cm^2')