class Vehicle:
    def __init__(self,make,model,tank_capacity_l):
        self.make= make
        self.model= model
        self.tank_capacity_l= tank_capacity_l
        self.fuel_level_l= tank_capacity_l
        self.total_distance_km= 0

    def drive(self,distance_km,consumption_l_per_100km):
        fuel_used= distance_km *(consumption_l_per_100km/100)
        self.fuel_level_l -= fuel_used
        if self.fuel_level_l < 0 :
            self.fuel_level_l = 0
        self.total_distance_km += distance_km

    def describe(self):
        print(f'{self.make} {self.model} : {self.fuel_level_l:.1f}L/{self.tank_capacity_l}L,Distance:{self.total_distance_km}km')

class Garage:
    def __init__(self,name):
        self.name= name
        self.vehicles = []

    def add_vehicle(self,vehicle):
        self.vehicles.append(vehicle)

    def list_vehicles(self):
        print(f'-----{self.name}-----')
        for v in self.vehicles:
            v.describe()
#Garage class (pass in garage name)
k_tech=Garage('K-Tech')
#1st car
car1=Vehicle('Toyota','Prado',80)
car1.drive(200,4.5)
k_tech.add_vehicle(car1)
#2nd car
car2=Vehicle('Lexus','Harrier',65)
car2.drive(100,2.5)
k_tech.add_vehicle(car2)
#3rd car
car3=Vehicle('Subaru','Forester',50)
car3.drive(80,1.5)
#Add the list of vehicles to the garage list
k_tech.add_vehicle(car3)
k_tech.list_vehicles()
