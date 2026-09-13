class Vehicle:
    total_vehicles_counted= 0
    fuel_price_per_litre= 194.50

    def __init__(self,make,model,tank_capacity_l):
        self.make = make
        self.model = model
        self.tank_capacity_l = tank_capacity_l
        self._fuel_level_l = tank_capacity_l      #encapsulation ie 'self._fuel_level',essentially protecting the value so it cannot be reached directly
        self.distance_km = 0
        Vehicle.total_vehicles_counted += 1

    def drive (self,distance_km,consumption_per_100km):
        self.distance_km += distance_km
        fuel_used = distance_km * (consumption_per_100km/100)
        self._fuel_level_l -= fuel_used
        #Ensure fuel level is never negative ie below zero
        if self._fuel_level_l < 0 :
            self._fuel_level_l = 0

        def get_fuel_level(self):
            return self._fuel_level_l

    def set_fuel_level(self,new_level):
        #'Setter: safely change fuel level with validation'
        if new_level < 0 :
            print('Fuel level cannot be zero.Setting to 0')
        elif new_level > self.tank_capacity_l :
            print('Fuel level cannot exceed tank capacity.')
        else:
            self._fuel_level_l = new_level

    def describe (self):
        print(f'{self.make} {self.model} \n {self._fuel_level_l}L/{self.tank_capacity_l}L Distance {self.distance_km}km')

car1=Vehicle('Toyota','Harrier',80)
print('Validation Testing (-50)')    #testing the validation line 'if new_level < 0'
car1.set_fuel_level(-50)
print('Validation Testing (9999)')   #testing the validation line 'if new_level > tank_capacity_l'
car1.set_fuel_level(9999)
car1.drive(200,3.5)
car1.describe()
