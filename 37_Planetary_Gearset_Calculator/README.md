This is project/tool models a planetary gearset,the building block of most automotive transmissions.Given the number of teeth on the sun and ring gears and the number of planets,it works out the gear ratio and the output speed and torque.

WHAT IT DOES 
The 'PlanetaryGearset'class checks that a gearset can actually be built:the planet gears need a whole number of teeth and they must space evenly around the carrier.It then calculates the ratio for four modes (1st,2nd,reverse,direct drive) and output rpm and torque for a given input

A negative ratio and RPM mean the output turns the opposite way to the input.Invalid gearsets and unknown modes raise a 'ValueError' with a clear message.

To test it,one can just change the values of the objects and check the results