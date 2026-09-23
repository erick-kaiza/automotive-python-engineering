"""
PROJECT : DRIVETRAIN POWER LOSS
Description:Power gets lost between the engine and the wheels-through the transmission,driveshaft and differential.Each stage has its own efficiency loss.

"""
class Driveline:
    def __init__(self,input_power_kW):
        self.input_power_kW = input_power_kW

    def output_power_kW(self):
        power_out = self.input_power_kW * 1
        return power_out

class Transmission(Driveline):
    def __init__(self, input_power_kW,transmission_efficiency):
        super().__init__(input_power_kW)
        self.transmission_efficiency = transmission_efficiency

    def output_power_kW(self):
        return super().output_power_kW() * self.transmission_efficiency

class Differential:
    def __init__(self,transmission,differential_efficiency):
        self.transmission = transmission
        self.differential_efficiency = differential_efficiency

    def output_power_kW(self):
        return self.transmission.output_power_kW() * self.differential_efficiency

def main():
    driveline = Driveline(input_power_kW=150)
    transmission = Transmission(input_power_kW=driveline.output_power_kW(),transmission_efficiency=0.90)
    differential = Differential(transmission=transmission,differential_efficiency=0.96)
    power_at_wheels = driveline.output_power_kW() * transmission.transmission_efficiency * differential.differential_efficiency
    drivetrain_loss = ((driveline.output_power_kW()-power_at_wheels)/driveline.output_power_kW()) * 100

    print('---TESTING DRIVETRAIN POWER LOSS CALCULATOR---')
    print(f'Driveline output power : {driveline.output_power_kW()}kW')
    print(f'Transmission output power : {transmission.output_power_kW():.1f}kW')
    print(f'Differential output power : {differential.output_power_kW():.1f}kW')
    print(f'Drivetrain Power Loss : {drivetrain_loss:.2f}%')
    print(f'Power at Wheels : {power_at_wheels}kW')

if __name__ == '__main__':
    main()
