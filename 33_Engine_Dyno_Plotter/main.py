import numpy as np
import matplotlib.pyplot as plt

"""
PROJECT 33:ENGINE DYNO - TORQUE & POWER CURVE PLOTTER
Description : A model of an engine's torque curve across an rpm range

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
        torque = self.max_torque_Nm - self.k * (rpm - self.peak_torque_rpm) **2
        torque = np.clip(torque,0,None)
        return torque

    def power_at_rpm(self,rpm):
        torque = self.torque_at_rpm(rpm)
        power = (torque * rpm)/9550
        return power

def main():
    #Honda K 20 Civic Type R 
    engine1 = Engine(displacement_l=2.0,max_torque_Nm=196,peak_torque_rpm=6100,redline_rpm=8000,idle_rpm=850)
    rpm_array = np.linspace(engine1.idle_rpm,engine1.redline_rpm,100)
    torque_array = engine1.torque_at_rpm(rpm_array)
    power_array = engine1.power_at_rpm(rpm_array)
#CREATING THE PLOT CURVES
#PLOT 1
    fig,ax1 = plt.subplots()
    ax1.plot(rpm_array,torque_array,color='blue',label='Torque (Nm)')
    ax1.set_xlabel('RPM')
    ax1.set_ylabel('Torque (Nm)',color='blue')
#PLOT 2
    ax2 = ax1.twinx()
    ax2.plot(rpm_array,power_array,color='red',label='Power(kW)')
    ax2.set_ylabel('Power(kW)',color='red')

    plt.title('Engine Dyno Curve (Honda K20) Civic Type R')
    plt.show()

if __name__ == '__main__':
    main()  