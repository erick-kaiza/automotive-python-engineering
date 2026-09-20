import math
"""
PROJECT 26: Fatigue life estimator
Description: Estimates the number of cycles to failure for a material under cyclic stress loading,using the Basquin Fatigue equation

"""

materials = {
    'steel_1045':{'name':'Steel_1045','sigma_f_prime':948,'b':-0.09},
    'aluminium_6061': {'name':'Aluminium_6061-T6','sigma_f_prime':620,'b':-0.11},
    'steel_4340': {'name':'Steel_4030 (alloy)','sigma_f_prime':1655,'b':-0.076}
    }

def display_materials():
    #Print available materials from the MATERIALS Dictionary
    print('-----AVAILABLE MATERIALS-----')
    for i,key in enumerate(materials,start=1):
        print(f'{i}. {materials[key]['name']}')

def get_material_choice():
    #Get the choice of material from the user
    keys = list(materials.keys())
    while True :
        display_materials()
        try:
            choice = int(input('Select Material number: '))
            if 1 <= choice <= 3 :
                return keys [choice-1]
            print('Invalid choice,try again.')
        except ValueError:
            print('Please enter a valid number.')

def calculate_cycles_to_failure (stress_amplitude,sigma_f_prime,b):
    #Solve Basquin's equation for cycles to failure N:
         #sigma_a = sigma_f_prime * (2n)^b
         #rearranged : n = 0.5 * (sigma_a/sigma_f_prime)^(1/b)
    ratio = stress_amplitude / sigma_f_prime
    exponent = 1/b
    n = 0.5 * (ratio ** exponent)
    return n

def classify_fatigue_life(cycles):
    #Classify fatigue regim based on cycle count
    if cycles < 1e3:
        return 'Low-Cycle Fatigue (LCF) - Very short life,plastic deformation dominant'
    elif cycles  < 1e6:
        return 'High-Cycle Fatigue (HCF) - Typical operational range'
    else:
        return 'Near-infinite Life - stress below practical fatigue limit'

def get_stress_input():
    #Ask the user for stress input
    while True:
        try:
            stress=float(input('Enter applied stress amplitude (MPa): '))
            if stress <= 0:
                print('Stress must be positive.')
                continue
            return stress
        except ValueError :
            print('Please enter a valid number: ')

def main ():
    print('===Fatigue Life Estimator===')
    running = True
    while running :
        material_key = get_material_choice()
        material = materials[material_key]
        stress = get_stress_input()
        cycles = calculate_cycles_to_failure(stress,material['sigma_f_prime'],material['b'])
        regime = classify_fatigue_life (cycles)

        print('-----RESULTS-----')
        print(f'Material : {material['name']}')
        print(f'Applied Stress : {stress}MPa')
        print(f'Estimated Cycles to Failure : {cycles:,.0f}')
        print(f'Fatigue Regime : {regime}')

        again = input('Run another estimate (y/n): ').strip().lower()
        running=again=='y'

    print('Existing Fatigue Life Estimator.')

if __name__ == '__main__' :
    main ()

    