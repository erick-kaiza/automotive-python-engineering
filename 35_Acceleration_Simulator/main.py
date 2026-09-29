import math
import numpy as np
import matplotlib.pyplot as plt
"""
PROJECT:0-100 KM/H ACCELERATION SIMULATOR
Description:Models how long it takes a car to reach 100km/h,including the gearshifts

"""
rpm_data = np.array([1000,2000,3000,4000,5000,6000,7000])
torque_data = np.array([150,210,260,280,270,240,200])
# print(np.interp(4325,rpm_data,torque_data))

def wheel_rpm(speed,radius):
    circumference = 2 * math.pi * radius
    revs_per_second = speed/ circumference
    return revs_per_second * 60

def engine_rpm(speed,radius,gear_ratio,final_drive_ratio):
    return wheel_rpm(speed,radius) * gear_ratio * final_drive_ratio

def tractive_force(engine_torque,gear_ratio,final_drive_ratio,radius,efficiency=0.9):
    wheel_torque = engine_torque * gear_ratio * final_drive_ratio * efficiency
    traction_force = wheel_torque / radius
    return traction_force

def resistive_forces(speed,mass,cd,area,crr,p=1.225):
    drag = 0.5 * p *cd * area * (speed**2)
    rolling = crr * mass * 9.81
    return drag + rolling

gears = [3.6,2.2,1.5,1.1,0.85]
final_drive = 3.9
radius = 0.31
mass = 1300
cd = 0.32
area = 2.1
crr = 0.012

shift_rpm = 6500
target = 27.8
dt = 0.05

speed = 0
elapsed = 0
gear_index = 0
time_list = []
speed_list = []

shift_timer = 0
shift_times = []

while speed < target:
    if shift_timer > 0:
        traction = 0
        shift_timer = shift_timer - dt
    else:
        rpm = engine_rpm(speed,radius,gears[gear_index],final_drive)
        rpm = max(rpm,1000)

        if rpm >= shift_rpm and gear_index < len(gears) - 1:
            gear_index +=1
            sfift_timer = 0.3
            shift_times.append(elapsed)
            traction = 0
        else:
            torque = np.interp(rpm,rpm_data,torque_data)
            traction = tractive_force(torque,gears[gear_index],final_drive,radius)

    
    resistance = resistive_forces(speed,mass,cd,area,crr)
    acceleration = (traction - resistance)/mass
    speed = speed + acceleration *dt
    elapsed = elapsed + dt 

    time_list.append(elapsed)
    speed_list.append(speed)

def main():
    for t in shift_times:
        plt.axvline(x=t,color='gray',linestyle='--')

    plt.plot(time_list,speed_list,color='red')
    plt.xlabel('Time (s)')
    plt.ylabel('Speed (m/s)')
    plt.title('Speed vs Time (0-100km/h)')
    plt.grid()
    plt.savefig('speed_vs_time.png')
    plt.show()

if __name__ == '__main__':
    main()







