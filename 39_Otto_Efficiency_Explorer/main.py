import numpy as np
import matplotlib.pyplot as plt
"""
PROJECT:OTTO CYCLE EFFICIENCY EXPLORER
Description:Takes a few real engines and calculates the ideal otto efficiency for each.It also sweeps across compression ratio to show why engineers keep pushing it higher.
"""
#store the engines in a dictionary,name and compression ratio
engines = {'1NZ-FE 1.5L':10.5,
           'K20C1 2.0L':9.8,
           '2ZR-FXE 1.8L':13}    #the names and engines can be switched out with any real engines and real compression ratios,so long as they run on the otto cycle.
#Get the engine names
names = []
for name in engines.keys():
    names.append(name)
#Get the engine ratios
engine_ratios =[]
for ratio in engines.values():
    engine_ratios.append(ratio)
#function that calculates otto efficiency,taking r and gamma
def calculate_otto_efficiency(r,gamma=1.4):
    otto_efficiency = (1-(1/r**(gamma-1))) * 100
    return otto_efficiency
#function that can calculate compression temperature
def calculate_compression_temperature(t1_c,r,gamma=1.4):
    t1_c = t1_c + 273
    compression_temperature = (t1_c * (r**(gamma-1)))-273
    return compression_temperature
#loop through the engines and print a comparison table;ratio,efficiency,compression temperature
print('-'*45)
print(f'{'Ratio':<10} {'Efficiency':<15} {'Compression temp(C)':<10}')
print('-'*45)
#Get engine efficiencies
engine_eff = []
for r in engines.values():
    efficiency = calculate_otto_efficiency(r=r)
    compression_temp = calculate_compression_temperature(25,r=r)
    print(f'{r:<10} | {efficiency:<15.2f} | {compression_temp:<10.2f}')
    engine_eff.append(efficiency)

#sweep r(compression ratio) from 6-16 and calculate efficiency for each
ratios = np.linspace(6,16,100)
def sweep():
    efficiency_sweep = []
    for r in ratios:
        otto_efficiency = calculate_otto_efficiency(r=r) 
        efficiency_sweep.append(otto_efficiency)
    return efficiency_sweep

#plot efficiency against compression ratio and mark the engines on the curve
#plot two charts,efficiency curve on one and the three engines on a bar chart
def plot_results(ratios,engine_ratios,names,engine_eff,efficiency_sweep):
        fig,(ax1,ax2) = plt.subplots(1,2)
        #Efficiency curve :LEFT
        ax1.plot(ratios,efficiency_sweep,color='blue')
        ax1.scatter(engine_ratios,engine_eff,color='red',zorder=3)
        ax1.set_xlabel('Compression Ratio')
        ax1.set_ylabel('Efficiency(%)')
        ax1.set_title('Efficiency vs Compression ratio')
        ax1.grid(True)
        #labels for engine dots
        for name,r,eff in zip(names,engine_ratios,engine_eff):
            ax1.annotate(name,xy=(r,eff),xytext=(5,-15),textcoords='offset points')
        #BAR CHART :RIGHT
        ax2.bar(names,engine_eff,color='tab:green')
        ax2.set_ylabel('Efficiency(%)')
        ax2.set_title('Efficiency per engine')
    #Display the charts
        plt.tight_layout()
        plt.savefig('otto_efficiency.png')
        plt.show()
#Get the engine with the maximum efficiency
max_efficiency = max(engine_eff)
def find_best_engine(names,engine_eff):
    best_eff = max(engine_eff)
    best_index = engine_eff.index(best_eff)
    best_name = names[best_index]
    return best_name
#Get the percantage gain in engine efficiency across the engines
def efficiency_gain(engine_eff):
        lowest_efficiency = min(engine_eff)
        highest_efficiency = max(engine_eff)
        gain = highest_efficiency - lowest_efficiency
        return gain
def main():
    print(f'Most Efficient engine:{find_best_engine(names=names,engine_eff=engine_eff)} at {max_efficiency:.2f}%')
    print(f'Gain in Engine Efficiency : {efficiency_gain(engine_eff=engine_eff):.2f}%')
    plot_results(ratios=ratios,engine_ratios=engine_ratios,names=names,engine_eff=engine_eff,efficiency_sweep=sweep())

if __name__ == '__main__':
    main()