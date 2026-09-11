class Vehicle:
    #This is a class attribute,unlike our previous project,whereby each method had its attribute,these two are known as class attributes and they can be accesed by all methods
    total_vehicles_created=0
    fuel_price_per_l=194.50

    def __init__(self,make,model,tank_capacity_l):
        self.make=make
        self.model=model
        self.tank_capacity_l=tank_capacity_l
        self.fuel_level_l=tank_capacity_l
        self.distance_km=0
        #Add a vehicle each time a new one is bumped
        Vehicle.total_vehicles_created += 1

    def drive(self,distance_km,consumption_l_per_100km):
        self.distance_km += distance_km
        fuel_used = distance_km * (consumption_l_per_100km/100)
        self.fuel_level_l -= fuel_used
        if self.fuel_level_l < 0 :
            self.fuel_level_l = 0


    def fuel_cost_to_fill(self):
        #Cost to fill fuel tank completely
        litres_needed = self.tank_capacity_l - self.fuel_level_l
        cost= litres_needed * Vehicle.fuel_price_per_l
        return cost

    def describe(self):
        print(f'{self.make} {self.model} : {self.fuel_level_l}L/{self.tank_capacity_l}L\nDistance : {self.distance_km:.1f}km')

car1 = Vehicle('Toyota','Prado',80)
car1.drive(200,1.5)
car1.describe()
print(f'Cost to fill Fuel tank:KES {car1.fuel_cost_to_fill()}')

car2 = Vehicle('Lexus','Harrier',60)
car2.drive(200,2.5)
car2.describe()
print(f'Cost to fill fuel tank:KES {car2.fuel_cost_to_fill()}')

car3 = Vehicle('Subaru','Forester',50)
car3.drive(400,3.5)
car3.describe()
print(f'Cost to fill Fuel tank:KES {car3.fuel_cost_to_fill()}')

print(Vehicle.total_vehicles_created)   #To access the class attribute,we call it via the class name,not the object name  

      