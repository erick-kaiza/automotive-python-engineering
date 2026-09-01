"""
OBD-II Fault Code Lookup-tool
---------------------------------
A simple command-line tool that looks up OBD-II diagnostic trouble codes and returns their description using a Python dictionary as the lookup database

Focus areas :
    -Dictioneries as key-value lookupt tables.
    -Safe lookups with dict.get() and a fallback value to avoid a KeyError message
    -Input sanitization with .upper() and .strip()
    -f-string formatting and output

The fault code set is weighted toward diesel/turbo-relevant codes (turbo boost,glow plugs,EGR,injectors) relevant vehicles such as those in Isuzu

Author:Erick Kirobi
Part of:'Python for Automotive Engineering'portfolio

"""

fault_codes= {
    "P0100":"Mass Air Flow (MAF) Circuit Malfunction",
    "P0113":"Intake Air Temperature Circuit High Input",
    "P0171":"System Too Lean (Bank 1)",
    "P0192":"Fuel Rail Pressure Sensor Circuit Low",
    "P0201":"Injector Circuit Malfunction - Cylinder 1",
    "P0217":"Engine Coolant Over Temperature Condition",
    "P0234":"Turbocharger Overboost Condition",
    "P0299":"Turbocharger Underboost Condition",
    "P0335":"Crankshaft Position Sensor Circuit Malfunction",
    "P0401":"Exhaust Gas Recirculation (EGR) Flow Insufficient",
    "P0420":"Catalyst System Efficiency Below Threshhold",
    "P0470":"Exhaust Pressure Sensor Malfunction",
    "P0500":"Vehicle Speed Sensor Malfunction",
    "P0562":"System Voltage Too Low",
    "P0670":"Glow Plug Control Circuit Malfunction",
}

while True:
    code=input('Enter OBD-II Fault Code (q to quit): ').upper().strip()

    if code == 'Q':
        print('Exiting fault code lookup.Drive Safe!')
        break

    description=fault_codes.get(code,'Code Not Found in database.')
    print(f'{code}:{description}')
