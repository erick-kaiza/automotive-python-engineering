"""
PROJECT:PLANETARY GEARSET CALCULATOR
Description:Planetary gearsets are the heart of automatic transmissions,this project checks the arrangement of the planet gears and the number of teeth,and decides if the build is possible.If possible it displays the ratios and rpm,torque.

"""

class PlanetaryGearset:
    def __init__(self,sun_teeth,ring_teeth,planets_number):
        if (ring_teeth-sun_teeth)%2 != 0 or (sun_teeth+ring_teeth)%planets_number !=0:
            raise ValueError('Invalid gearset:Check teeth and Planet teeth')

        self.sun_teeth = sun_teeth
        self.ring_teeth = ring_teeth
        self.planets_number = planets_number

    def calculate_planet_teeth(self):
        planet_teeth = (self.ring_teeth - self.sun_teeth)//2
        return planet_teeth

    def calculate_ratios(self,mode):
        
        if mode == 'First_gear':
            first_gear = 1 + (self.ring_teeth/self.sun_teeth)
            return first_gear
        elif mode == 'Second_gear':
            second_gear = 1 + (self.sun_teeth/self.ring_teeth)
            return second_gear
        elif mode == 'Reverse_gear':
            reverse = -self.ring_teeth/self.sun_teeth
            return reverse
        elif mode == 'Direct_drive':
            return 1
        else:
            raise ValueError('Invalid mode')

    def calculate_output(self,input_rpm,input_torque,mode):
        ratio = self.calculate_ratios(mode=mode)
        output_rpm = input_rpm/ratio
        output_torque = input_torque * ratio
        return output_rpm,output_torque

    def describe(self,input_rpm,input_torque):
        modes = ['First_gear','Second_gear','Reverse_gear','Direct_drive']
        print(f'{'Mode':<12}{'Ratio':>8}{'RPM':>10}{'Torque':>10}')
        for mode in modes:
            ratio = self.calculate_ratios(mode=mode)
            rpm,torque = self.calculate_output(input_rpm,input_torque,mode=mode)
            print(f'{mode:<12}{ratio:>8.3f}{rpm:>10.1f}{torque:>10.1f}')

def main():
    planetary_gearset = PlanetaryGearset(30,70,4)
    planetary_gearset.describe(1000,100)

if __name__ == '__main__':
    main()

        







        

#Validation in __init__ that raises a ValueError with a clear message
#method for planet teeth,
# method that returns the ratio for a chosen mode
# method that takes input RPM and torque and returns output RPM and torque,
# a printed table of all four modes for an input RPM and torque.
