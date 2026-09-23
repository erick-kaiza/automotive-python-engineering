This project models power loss through a vehicle's drivetrain - engine output flowing through a transmission and a differential before reaching the wheels - using OOP to represent each stage as a component.

Power is never delivered to the wheels at 100% efficiency.Each mechanical stage (gearbox,driveshaft,differential) bleeds off a small percantage as heat and friction.This project chains those losses together and calculates total drivetrain efficiency

It uses the primary formula : input power x eficiency