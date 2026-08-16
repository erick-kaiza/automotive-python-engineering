"""
PROJECT:AERODYNAMIC DRAG CALCULATOR
DESCRIPTION:CLACULATES AERODYNAMIC DRAG USING THE BASIC FORMULA

"""

print('='*25)
print('AEROFYNAMIC DRAG CALCULATOR')
print('='*25)

#USER INPUT
speed_kmh=float(input('Enter vehicle speed (km/h): '))
air_density=float(input('Enter air density (kg/m^3): '))
drag_coefficient=float(input('Enter Drag Coefficient(Cd): '))
frontal_area=float(input('Enter frontal area (m^2): '))
engine_power=float(input('Enter engine power (W): '))
engine_power_kw=engine_power * 1000

#convert km/h - m/s
speed_ms=speed_kmh*(10/36)
drag_force=0.5 *air_density*drag_coefficient*frontal_area*speed_ms**2
top_speed=(2*(engine_power_kw/air_density)*drag_coefficient*frontal_area)**(1/3)
top_speed_km=top_speed *3.6
#Power Required to overcome aerodynamic drag
drag_power=drag_force * speed_ms
drag_power_kW=drag_power/1000

print('--------RESULTS---------')
print(f'Vehicle Speed(m/s):{speed_ms:.1f}m/s')
print(f'Aerodynamic Drag Force:{drag_force:.2f}N')
print(f'Power required to overcome drag:{drag_power_kW:.2f}kW')
print(f'Theoretical Top Speed:{top_speed_km:.2f}km/h')
