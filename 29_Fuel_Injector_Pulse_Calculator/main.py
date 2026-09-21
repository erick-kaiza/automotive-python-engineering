class Injector:
    fuel_density = 0.745
    def __init__(self,fuel_flow_rate,dead_time):
        self.fuel_flow_rate = fuel_flow_rate
        self.dead_time = dead_time

    def convert_to_mg_s(self):
        flow_rate_cc = self.fuel_flow_rate
        flow_rate_mg_s = (self.fuel_density * flow_rate_cc * 1000)/60
        return flow_rate_mg_s

    def describe(self):
        return f'Fuel flow rate (cc/min):{self.fuel_flow_rate:.2f}\nFuel flow rate (mg/s):{self.convert_to_mg_s():.2f}'

class EngineDemand:
    def __init__(self,fuel_mass,injector):
        self.fuel_mass = fuel_mass
        self.injector = injector

    def ecu_pulse_width(self):
        #Calculated pulse width (dead time excluded)
        pulse_width_calc = (self.fuel_mass / self.injector.convert_to_mg_s()) * 1000
        #Actual pulse width (dead time included)
        pulse_width_actual = self.injector.dead_time + pulse_width_calc 
        return pulse_width_actual

    def describe (self):
        return f'ECU Pulse Width : {self.ecu_pulse_width():.2f}ms'

def main ():
    injector1=Injector(fuel_flow_rate=550,dead_time=1.5)
    turbo_engine = EngineDemand(fuel_mass=4.65,injector=injector1)
    print(injector1.describe())  
    print(turbo_engine.describe())

if __name__ == '__main__':
    main()