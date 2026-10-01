This project analyzes a mock engine dynamometer data.It takes torque readings across the engine's rpm range and turns them into power curve and key figures as a tuner reads from a dyno sheet.It uses pandas for the data table and matplotlib for plotting.

WHAT IT DOES
-Builds a table of RPM and torque readings and calculates power in kW and hp,using P(kW) = Torque x RPM/9549 and hp = power(kW) x 1.341
-Finds peak torque and peak power.
-Determines the usable RPM band,defined as the range where the torque stays at or above 90% of peak torque.
-Plots torque and power against RPM on a dual-axis chart,with the peaks annotated and usable rpm shaded green

It then outpiyts,a printed dyno table,a summary report and plots torque and power (hp) against rpm.