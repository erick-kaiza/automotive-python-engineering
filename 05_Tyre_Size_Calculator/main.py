import math      #accessing the python math module
"""
Project:Tyre size Calculator
Description:This Program takes from the user tyre width(mm),aspect ratio(%) & diameter(inches), to calculate and display:
    -sidewall height
    -overall tyre diameter(mm)
    -rolling radius
    -circumfrence

"""

print('='*25)
print('TYRE SIZE CALCULATOR')
print('='*25)
#USER INPUT
tyre_width=float(input('Enter tyre width (mm): '))
aspect_ratio=float(input('Enter Aspect Ratio(%): '))
wheel_diameter=float(input('Enter Wheel Diameter(inches): '))

#ENGINEERING CALCULATIONS
sidewall_height=(tyre_width * aspect_ratio)/100
wheel_mm=wheel_diameter * 25.4   #Convert inches to millimeters
ovrll_diameter=wheel_mm + (2*sidewall_height)      #Overall diameter
rolling_radius=ovrll_diameter/2
circumfrence=math.pi * ovrll_diameter

#DISPLAYING RESULTS
print('')
print('*'*10)
print('RESULTS')
print('*'*10)
print(f'Sidewall Height: {sidewall_height:.2f}mm')
print(f'Overall Diameter: {ovrll_diameter:.2f}mm')
print(f'Rolling Radius: {rolling_radius:.2f}mm')
print(f'Circumfrence:{circumfrence:.2f}mm')



