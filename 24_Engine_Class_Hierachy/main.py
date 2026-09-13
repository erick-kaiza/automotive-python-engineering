"""
PROJECT :ENGINE CLASS HIERACHY
Description :Practicing on class inheritance,one class (child) automatically gets the attributes and methods of another class (parent),then add or change things on top

"""
class Engine:
#Basic attributes shared by engines,displacement,number of cylinders etc
    def __init__(self,displacement_l,cylinders):
        self.displacement_l = displacement_l
        self.cylinders = cylinders
        self.is_running = False
#Basic actions shared by engines,ALL Engines start and/or stop
    def start(self):
        self.is_running = True
        print(f'{self.displacement_l}L {self.cylinders}cyl is running')

    def stop(self):
        self.is_running = False
        print('Engine stopped !')

class GasolineEngine (Engine):
    #Instead of repeating the attributes for this class,since they have been dea;t with by Engine class,we can pass on the engine attributes to this class,this is what is called 'Class Inheritance'
    def __init__(self, displacement_l, cylinders,octane_rating):
        super().__init__(displacement_l, cylinders)
        self.octane_rating = octane_rating

    def describe(self) :
        print(f'{self.displacement_l}L,{self.cylinders}cyl,requires {self.octane_rating} octane fuel rating')

class DieselEngine(Engine):
    def __init__(self, displacement_l, cylinders,compression_ratio):
        super().__init__(displacement_l, cylinders)
        self.compression_ratio = compression_ratio

    def describe(self):
        print(f'{self.displacement_l}L,{self.cylinders}cyl,{self.compression_ratio} compression ratio')


petrol_engine = GasolineEngine(3.0,6,90)
diesel_engine = DieselEngine(1.9,4,12.1)
#Start both engines
print('TESTING PETROL ENGINE START')
petrol_engine.start()
print('TESTING DIESEL ENGINE START')
diesel_engine.start()

#Describing both engines (testing child class methods)
print('---PETROL ENGINE---')
petrol_engine.describe()
print('---DIESEL ENGINE---')
diesel_engine.describe()