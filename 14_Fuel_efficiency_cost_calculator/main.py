"""
Project:Fuel Efficiency calculator
Description: The user can log in multiple trips and the program calculates fuel efficiency per trip,plus a running average across all trips logged so far.Then,they can choose to view a summary of all trips ,or quit.

"""
trips=[]
menu='1.Log a Trip\n2.View Summary\n3.Quit'
#Display the menu
print('--------------------\nWELCOME TO K-TECH TRAVEL & NAVIGATION\n--------------------')
#Ask the user for input continously until they opt to quit
while True:
    print (menu)
    choice=input('Enter your choice (1,2 or 3)')
    if choice == '1':
        #ask user for trip name,distance travelled during that trip,fuel used in litres
        name=input('Enter trip destinations (eg London to Cardiff): ')
        distance_input=input('Enter total ditance traveled in km: ')
        fuel_input=input('Enter total litres of Fuel used: ')
#Handle user leaving a blank space,entering 0 fuel,not selecting a valid option
        try:
            distance=float(distance_input)
            fuel=float(fuel_input)
            efficiency=distance/fuel
            trips.append({'Name':name,'Distance (km)':distance,'Fuel':fuel,'Efficiency':efficiency})
            print(f'Trip Logged: {efficiency:.2f} km/L')
        except ValueError:
            print('Invalid input - distance and fuel must be numbers')
        except ZeroDivisionError:
            print('Fuel cannot be zero,that would mean you were stationay')

    elif choice == '2':
        #Display the message if the user did not put in any trips
        if not trips:
            print('Trip List is empty')
        else:
            #set for performing a rolling total
            total_distance=0
            total_fuel=0
            for trip in trips:
                print(f'{trip['Name']}:{trip['Distance (km)']} km:{trip['Fuel']}L:{trip['Efficiency']:.2f}km/L')
                total_distance += trip['Distance (km)']
                total_fuel +=trip['Fuel']
                overall_efficiency=total_distance/total_fuel
            print(f'Overall Average Efficiency:{overall_efficiency:.2f}km/L')
    elif choice == '3':
        print('Exiting,Safe Travels 😊')
        break
    else:
        print('Invalid choice-please enter 1,2 or 3')


