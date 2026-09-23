This project models a vehicle cooling system as a three composed component - 'Radiator','Waterpump' and 'Cooling System' to determine whether an engine's heat output can be safely dissipated at a given load and across a swept range of loads.

An engine convertrs only part of its fuel energy into useful work ; the rest becomes waste heat that must be carried away by coolant and rejected to the atmosphere through the radiator.If the radiator cannot reject heat as fast as the engine produces it,the system overheats.

The formula used: heat rejected (kW) = surface area of the radiator(m^2) x coolant flow x coefficient.This is just a simplified method.

DEBUGGING NOTE:CORRECT LOGIC,WRONG CALIBRATION
NOTES:After fixing the structural bugs,the stress test ran without errors but returned 'Overheating: True' for every single load,including the lowest one.The code itself was correct,the constant in the heat rejection formula (0.015),before changing to 2.5,was far too low,so the radiator's calculated output sat at a fraction of a kilowatt regardless of input,always below every test load,guaranteeing True everytime and making the sweep meaningless.

LESSON:A program can be structurally and logically sound and still produce useless/unrealistic model if the underlying constants aren't callibrated to the scale of the values being tested.Raising the coefficient to 2.5 brought the radiator's output into the same order of magnitude as the test loads,producing a realistic mixed result - the system keeps up at low load and fails at high load,which is the actual real-world behavior being modeled.Working code and a working model are not the same thing,always sanity-check that output values fall in a plausible range before trusting the logic around them.