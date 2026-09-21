import math
"""
PROJECT 28:Transmission & Gear Composition
Description:Models a Transmission as composed of multiple Gear objects,calculating output RPM and vehicle speed
"""
class Gear:
    def __init__(self,gear_number,ratio):
        self.gear_number = gear_number
        self.ratio = ratio

    def describe (self):
        return f'Gear {self.gear_number} : Ratio {self.ratio}'

class Transmission:
    def __init__(self,final_drive_ratio):
        self.final_drive_ratio = final_drive_ratio
        self.gears = []

    def add_gear (self,gear):
        self.gears.append(gear)

    def list_gears (self):
        print('-----GEARS-----')
        for gear in self.gears:
            print(gear.describe())

    def get_gear(self,gear_number):
        for gear in self.gears:
            if gear.gear_number == gear_number:
                return gear
        return None 

    def output_rpm (self,engine_rpm,gear_number):
        gear = self.get_gear(gear_number)
        if gear is None :
            return None
        return engine_rpm / (gear.ratio * self.final_drive_ratio)

    def vehicle_speed_kph(self,engine_rpm,gear_number,wheel_diameter_m):
        out_rpm = self.output_rpm(engine_rpm,gear_number)
        if out_rpm is None :
            return None
        wheel_circumfrence_m = math.pi * wheel_diameter_m
        speed_m_per_min = out_rpm * wheel_circumfrence_m
        speed_kph = speed_m_per_min * 60 / 1000
        return speed_kph

def build_5peedtransmission ():
    trans = Transmission(final_drive_ratio=3.9)
    ratios = [3.5,2.1,1.4,1.0,0.8]
    for i,ratio in enumerate(ratios,start=1):
        trans.add_gear(Gear(gear_number=i,ratio=ratio))
    return trans

def main ():
    print('=====TRANSMISSION COMPOSITION DEMO=====')
    gearbox = build_5peedtransmission()
    gearbox.list_gears()

    engine_rpm = 4000
    wheel_diameter_m = 0.65

    for gear_num in range(1,6):
        speed = gearbox.vehicle_speed_kph(engine_rpm,gear_num,wheel_diameter_m)
        print (f'Gear {gear_num} at {engine_rpm} RPM Speed : {speed:.2f}km/h ')

if __name__ == '__main__':
    main()