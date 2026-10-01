import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
"""
PROJECT:DYNO SHEET ANALYZER
Description:It takes raw dyno readings ,builds the power curve,finds the peaks,and plots the results

"""
rpm = np.array([2000,2500,3000,3500,4000,4500,5000,5500,6000,6500])
torque = np.array([210,245,280,295,300,292,285,250,225,195])

def build_dyno_table():
    df = pd.DataFrame({'RPM':rpm,'Torque':torque})
    df['Power_kW'] =(df['Torque'] * df['RPM'])/9549
    df['Power_hp'] = df['Power_kW'] * 1.341
    return df

def find_peaks(df):
    max_torque = df['Torque'].max()
    rpm_max_torque = df.loc[df['Torque'].idxmax(),'RPM']

    max_power = df['Power_hp'].max()
    rpm_max_power = df.loc[df['Power_hp'].idxmax(),'RPM']

    return max_torque,rpm_max_torque,max_power,rpm_max_power

def usable_band(peak_torque,df):
    band_rpm = []
    threshold = 0.9 * peak_torque
    for rpm,torque in zip(df['RPM'],df['Torque']):
        if torque >= threshold:
            band_rpm.append(rpm)
    highest_band_rpm = max(band_rpm)
    lowest_band_rpm = min(band_rpm)
    return lowest_band_rpm,highest_band_rpm

def main():
    df = build_dyno_table()
    max_torque,rpm_max_torque,max_power,rpm_max_power = find_peaks(df=df)
    lowest_band_rpm,highest_band_rpm = usable_band(peak_torque=max_torque,df=df)

    print('DYNO SHEET RESULTS')
    print(round(df,2))
    print(f'\nMax Torque : {max_torque:.1f}Nm')
    print(f'RPM at Max Torque : {rpm_max_torque:.1f}RPM')
    print(f'Max Power : {max_power:.1f}HP')
    print(f'RPM at Max Power : {rpm_max_power:.1f}RPM')
    print(f'USABLE BAND : {lowest_band_rpm}RPM - {highest_band_rpm}RPM')

    fig,ax1 = plt.subplots()
    ax1.plot(rpm,torque,color='blue',label='Torque (Nm)',marker='o')
    
    ax1.set_xlabel('RPM')
    ax1.set_ylabel('Torque (Nm)',color='blue')
    ax1.annotate(f'{max_torque}Nm@{rpm_max_torque:.0f}RPM',xy=(rpm_max_torque,max_torque),
                 xytext=(rpm_max_torque-700,max_torque-15),arrowprops=dict(arrowstyle='->'))
    ax1.axvspan(lowest_band_rpm,highest_band_rpm,alpha=0.2,label='Useful RPM Band',color='green')
    line1,label1 = ax1.get_legend_handles_labels()
    ax1.grid()

    ax2=ax1.twinx()
    ax2.plot(rpm,df['Power_hp'],color='red',label='Power (hp)',marker='o')
    lines2,label2 = ax2.get_legend_handles_labels()
    ax2.set_ylabel('Power (hp)',color='red')
    ax2.annotate(f'{max_power:.1f}hp@{rpm_max_power:.0f}RPM',xy=(rpm_max_power,max_power),
                xytext=(rpm_max_power+200,max_power-25),arrowprops=dict(arrowstyle='->'))
    ax2.legend(line1 + lines2,label1+label2,loc='best')
    ax2.grid(False)

    plt.title('RPM VS TORQUE & HORSEPOWER')
    plt.savefig('rpm_vs_torque&hp.png')
    plt.show()

if __name__ == '__main__':
    main()
    

    



