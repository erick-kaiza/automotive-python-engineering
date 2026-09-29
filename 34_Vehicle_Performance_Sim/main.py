import matplotlib.pyplot as plt
import numpy as np
import math
"""
PROJECT 34:VEHICLE PERFORMANCE SIMULATOR - WHEEL TORQUE & SPEED BY GEAR
Description:This project combines an Engine class and Transmission class,to calculate actual wheel torque and vehicle speed

"""

class Engine:
    def __init__(self,displacement_l,max_torque_Nm,peak_torque_rpm,redline_rpm,idle_rpm=800):
        self.displacement_l = displacement_l
        self.max_torque_Nm = max_torque_Nm
        self.peak_torque_rpm = peak_torque_rpm
        self.redline_rpm = redline_rpm
        self.idle_rpm = idle_rpm
        self.k = max_torque_Nm / max((redline_rpm - peak_torque_rpm,peak_torque_rpm-idle_rpm)) **2

    def torque_at_rpm(self,rpm):
        torque = self.max_torque_Nm - self.k * (rpm - self.peak_torque_rpm)**2
        return np.clip(torque,0,None)

class Transmission:
    def __init__(self,engine,final_drive_ratio,wheel_radius):
        self.engine = engine
        self.final_drive_ratio = final_drive_ratio
        self.wheel_radius = wheel_radius

    def calculate_wheel_torque(self,rpm_array,gear_ratio):
        engine_torque = self.engine.torque_at_rpm(rpm_array)
        wheel_torque = engine_torque * gear_ratio * self.final_drive_ratio
        return wheel_torque 

    def calculate_vehicle_speed(self,rpm_array,gear_ratio):
        wheel_rpm = rpm_array / (gear_ratio * self.final_drive_ratio)
        wheel_circumfrence = self.wheel_radius * math.pi * 2
        vehicle_speed = ((wheel_rpm/60) * wheel_circumfrence) * 3.6       #convert to km/h
        return vehicle_speed

def main():
    engine = Engine(max_torque_Nm=196,peak_torque_rpm=6100,redline_rpm=8000,idle_rpm=850,displacement_l=2.5)
    transmission = Transmission(engine=engine,final_drive_ratio=4.1,wheel_radius=0.3)

    gear_list = [3.5,2.1,1.4,1.0,0.8]
    rpm_array = np.linspace(engine.idle_rpm,engine.redline_rpm,100)

    plt.figure()

    for gear_ratio in gear_list:
        torque_array = transmission.calculate_wheel_torque(rpm_array=rpm_array,gear_ratio=gear_ratio)
        speed_array = transmission.calculate_vehicle_speed(rpm_array=rpm_array,gear_ratio=gear_ratio)
        plt.plot(speed_array,torque_array,label=f'{gear_ratio}')

    plt.xlabel('Vehicle Speed (km/h)')
    plt.ylabel('Wheel Torque (Nm)')
    plt.title('Wheel Torque vs Vehicle Speed')
    plt.legend()
    plt.savefig('wheel_torque_vs_vehicle_speed.png')
    plt.show()

if __name__ == '__main__':
    main()

