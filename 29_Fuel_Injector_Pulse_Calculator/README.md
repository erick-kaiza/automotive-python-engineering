A class-based Python tool that models how an ECU calculates fuel injector pulse-width ; the amount of time an injector stays open per engine cycle to deliver the correct fuel mass,including the injector's electromechanical 'dead time' delay.

AN engine's ECU doesen't just 'spray fuel',it calculates a precise pulse width for each injector based on how much fuel the engine needs and how fast the injector can deliver it.Real injectors also have a small delay before they physically begin flowing fuel once triggered,called dead time,which must be added on top of the calculated flow time.

ENGINEERING CONTEXT
Pulse Width calculation is core to how electronic fuel injection systems actually work-it's the real-time computation an ECU Performs many times per second to keep the air-fuel ratio correct under changing engine load.Dead time compensation specifically matters for accurate idle and light-load fuelling,where the delay is a larger fraction of the total pulse.