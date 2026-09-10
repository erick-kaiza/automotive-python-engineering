This is the first object-oriented programming (OOP) in the portfolio.It introduces the 'Vehicle class' bundling a vehicle's data together with the methods that act on that data

#CONCEPTS PRACTICED
-Defining a class with '__innit___' to set up initial object state.
-Using 'self' to access and modify an object's own data
-Methods that update state across multiple calls (fuel level and total distance both persist and accumulate correctly)
-Creating multiple independent objects from the same class,each with its own separate data
-A guard condition inside a method to prevent invalid state (overfiling the tank)

Unlike function-based projects,'Vehicle'  objects hold their own state between method calls- 'total_distance_km' and 'fuel_level' persist and update across multiple ca;;s without needing to be passed in and returned each time