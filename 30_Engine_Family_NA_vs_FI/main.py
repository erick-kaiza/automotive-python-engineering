import math
class Engine:
    def __init__(self,displacement_l,no_of_cylinders,torque,rpm):
        self.displacement_l = displacement_l
        self.no_of_cylinders = no_of_cylinders
        self.torque = torque
        self.rpm = rpm
        self.is_running = False
        #Start running our engine
    def start_engine(self):
        self.is_running = True
        print('---ENGINE STARTED---')
        print(f'Displacement(L): {self.displacement_l}\nNumber of cylinders:{self.no_of_cylinders}\nTorque : {self.torque}Nm\nRPM :{self.rpm}')

    #Stopping our engine
    def stop_engine(self):
        self.is_running = False
        print('Engine has stopped!')

    def calculate_power(self):
        power = (self.torque  * self.rpm)/9550
        return power

    def calculate_hp_per_l(self):
        hp = self.calculate_power() * 1.341
        hp_per_l = (hp) / self.displacement_l
        return hp_per_l

    def describe(self):
        print(f'Engine Power : {self.calculate_power():.1f}kW')

class TurboEngine(Engine):
    def __init__(self, displacement_l, no_of_cylinders, torque, rpm,boost_psi):
        super().__init__(displacement_l, no_of_cylinders, torque, rpm)
        self.boost_psi = boost_psi

    def specs(self):
        print('---TURBOCHARGED ENGINE---')
        print(f'BOOST PRESSURE :{self.boost_psi}PSI')

    def pressure_ratio(self):
        absolute_pressure = self.boost_psi + 14.7    #14.7 is atmospheric pressure
        pr = (absolute_pressure)/ 14.7
        return pr

    def turbo_power(self):
        t_power = self.pressure_ratio() * self.calculate_power() * 0.75    #0.75 is the turbo efficiency
        return t_power

    def turbo_horsepower_per_l(self):
        hp_per_l = (self.turbo_power() * 1.341)/self.displacement_l
        return hp_per_l

    def calculate_power_perc_increase(self):
        base_power = self.calculate_hp_per_l()
        new_power = self.turbo_horsepower_per_l()
        percantage_increase = ((new_power-base_power)/base_power) * 100
        return f'Percantage increase in power : {percantage_increase:.1f}%'
        
def main():
    print('-----TESTING ENGINE FAMILY COMPARISON-----')
    engine1 = Engine(displacement_l=3.0,no_of_cylinders=4,torque=400,rpm=8500)
    turbo_engine = TurboEngine(displacement_l=3.0,no_of_cylinders=4,torque=400,rpm=8500,boost_psi=15)
    engine1.start_engine()
    print(f'Horsepower per Litre: {engine1.calculate_hp_per_l():.1f}HP/L')
    engine1.describe()
    engine1.stop_engine()

    print('TURBOCHARGED ENGINE STARTED')
    turbo_engine.specs()
    print(f'Pressure Ratio: {turbo_engine.pressure_ratio():.1f}')
    print(f'Power: {turbo_engine.turbo_power():.1f}kW')
    print(f'Horsepower per Litre: {turbo_engine.turbo_horsepower_per_l():.2f}HP/L')
    print(turbo_engine.calculate_power_perc_increase())
    turbo_engine.stop_engine()

if __name__ == '__main__':
    main()


    
