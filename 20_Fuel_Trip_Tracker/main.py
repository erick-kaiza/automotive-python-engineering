"""Vehicle Class- Fuel & Trip Tracker
"""

class Vehicle:
    #Like a blueprint for a certain vehicle,eg maake,model,essemtially,what is the information of our vehicle
    def __init__(self,make,model,tank_capacity_l):
        self.make= make
        self.model= model
        self.tank_capacity_l= tank_capacity_l
        self.fuel_level_l= tank_capacity_l
        self.total_distance_km=0
#What can our car do,it can drive,when we drive,fuel drops
    def drive(self,distance_km,consumption_l_per_100km):
        fuel_used= distance_km * (consumption_l_per_100km/100)
        self.fuel_level_l -=fuel_used
        if self.fuel_level_l < 0:
            self.fuel_level_l =0
        self.total_distance_km +=distance_km

    def refuel(self,litres):
        self.fuel_level_l += litres
        if self.fuel_level_l > self.tank_capacity_l:
            print('Overfill of Fuel')
            self.fuel_level_l = self.tank_capacity_l
            

    def describe(self):
        print(f'{self.make} {self.model} : {self.fuel_level_l:.1f}L/{self.tank_capacity_l}L,Distance:{self.total_distance_km:.1f}km')

my_car=Vehicle('Toyota','Prado',80)
my_car.describe()
my_car.drive(100,4.5)
# my_car.refuel(10.2)
my_car.describe()
