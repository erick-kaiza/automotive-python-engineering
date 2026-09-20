"""
PROJECT 27:Bearing L10 life calculator
Description:Estimates bearing fatigue life (L10) in revolutions and operating hours

"""
bearing_types = {
    'ball':{'name':'Ball Bearing','k':3},
    'roller':{'name':'Roller Bearing','k':10/3}
}

def display_bearing_types():
    print('-----BEARING TYPES-----')
    for i,key in enumerate(bearing_types,start=1):
        print(f'{i}. {bearing_types[key]['name']}')

def get_bearing_type():
    keys = list(bearing_types.keys())
    while True:
        try:
            display_bearing_types()
            choice = int(input('Enter bearing type : '))
            if 1 <= choice <=len(keys):
                return keys [choice - 1]
            print('Invalid choice try again')
        except ValueError:
            print('Enter a valid number: ')

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print('Value must be a positive number.')
                continue
            return value
        except ValueError:
            print('Please enter a valid number: ')

def calculate_l10_revolutions(c,p,k):
    return (c/p) ** k

def revolutions_to_hours (l10_million_rev,rpm):
    total_rev = l10_million_rev * 1e6
    minutes = total_rev / rpm
    hours = minutes/60
    return hours

def main ():
    print('===Bearing L10 Life Calculator===')
    running = True
    while running :
        bearing_key = get_bearing_type()
        k=bearing_types[bearing_key]['k']

        c= get_positive_float('Enter dynamic load rating C (N): ')
        p= get_positive_float('Enter applied equivalent load P (N): ')
        rpm= get_positive_float('Enter operating speed (rpm): ')

        l10_rev = calculate_l10_revolutions(c,p,k)
        l10_hours = revolutions_to_hours(l10_rev,rpm)

        print('-----REULTS-----')
        print(f'Bearing Type : {bearing_types[bearing_key]['name']}')
        print(f'L10 Life(revolutions) : {l10_rev:,.2f} million revolutions')
        print(f'L10 Life(hours): {l10_hours:,.0f} operating hours.')

        again = input('Run another estimate (y/n): ')
        running = again == 'y'

    print('Exiting Bearing L10 Life Calculator.')


if __name__ == '__main__':
    main()