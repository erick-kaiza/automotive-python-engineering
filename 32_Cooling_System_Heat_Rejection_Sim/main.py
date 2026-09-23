import numpy as np
"""
PROJECT 32:COOLING SYSTEM HEAT REJECTION SIMULATOR
Description:An engine's cooling system has to reject a certain amount of heat energy depending on engine load,or the engine overheats.This project models a CoolingSystem that has a Radiator and WaterPump.

"""

class Radiator:
    def __init__(self,surface_area_m2,coolant_flow_lpm):
        self.surface_area_m2 = surface_area_m2
        self.coolant_flow_lpm = coolant_flow_lpm

    def heat_rejected_kW (self):
        heat_rejected = self.surface_area_m2 * self.coolant_flow_lpm * 2.5  #efficiency,this is not how a modern radiator does heat transfer rather this is a simple mathematical formula to keep things constant
        return heat_rejected

class WaterPump:
    def __init__(self,flow_rate_lpm,efficiency):
        self.flow_rate_lpm = flow_rate_lpm
        self.efficiency = efficiency

    def calculate_effective_flow(self):
        effective_flow_lpm = self.flow_rate_lpm * self.efficiency
        return effective_flow_lpm


class CoolingSystem:
    def __init__(self,radiator,waterpump,engine_heat_load_kw):
        self.engine_heat_load_kw = engine_heat_load_kw
        self.radiator = radiator
        self.waterpump = waterpump

    def is_overheating(self):
        return self.engine_heat_load_kw > self.radiator.heat_rejected_kW()

    def stress_test(self):
        loads = np.linspace(20,120,10)
        for power in loads:
            result = power > self.radiator.heat_rejected_kW()
            print(f'{power:.2f}kW Overheating : {result}')
           

def main():
    waterpump = WaterPump(flow_rate_lpm=45,efficiency=0.92)
    radiator = Radiator(surface_area_m2=0.35,coolant_flow_lpm=waterpump.calculate_effective_flow())#the radiator's coolant flow is dependent on the water pump's effective flow rate.
    coolingsystem = CoolingSystem(radiator=radiator,waterpump=waterpump,engine_heat_load_kw=90)
    print('-----TESTING COOLING SYSTEM HEAT REJECTION SIMULATOR-----')
    print(f'Present Status\nOverheating :{coolingsystem.is_overheating()}\n')
    coolingsystem.stress_test()

if __name__ == '__main__':
    main()

