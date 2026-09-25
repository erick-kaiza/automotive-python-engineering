This project models an engine's torque output across its RPM range using a parabolic curve centered on peak torque RPM,then derives the power curve from torque via the standard metric conversion.Both curves are plotted together on a dual-axis chart,replicating a real dynp printout.

Real engines don't produce flat torque-output rises from idle,peaks somewhere in the mid-range and falls off toward redline,modeled as a parabola:
        torque(rpm)= max_torque - k * (rpm - peak_rpm)**2

'k' controls how sharply torque falls away from peak and is calibrated so torque approaches zero at whichever boundary (idle/redline) sits farther from peak RPM - preventing the curve from going negative on the nearer side.

Power is derived directly from torque:
    power(kW)= torque (Nm)/9550
Because torque falls off but RPM keeps climbing,power continues to rise even past peak torque - until torque's decline finally outpaces rising RPM.That crossover point is visible on the plot.
