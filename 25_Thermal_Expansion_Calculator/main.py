"""
PROJECT:THERMAL EXPANSION CALCULATOR
Description:This project calculates how much a component grows given its material,original dimension and temperature change

"""

class Material:
    #Represents the material with a known thermal expansion coefficient
    coefficients={
        'aluminium':0.0000231,
        'steel':0.0000120,
        'cast_iron':0.0000106}

    def __init__(self,name):
        self.name = name.lower()
        self.coefficient = Material.coefficients.get(self.name)
        if self.coefficient is None:
            raise ValueError (f'Unknown material : {name}')

class Component:
    #Physical properties of the material,this is called composition,the Component class has a Material class as one of its objects
    def __init__(self,length,material,temp_change):
        self.length = length
        self.material = material
        self.temp_change = temp_change

    def expand_to_newtemp(self):
        linear_expansion = self.length * self.material.coefficient * self.temp_change
        new_length = self.length - linear_expansion
        return linear_expansion,new_length

material_1 = Material('steel')
rod = Component (100,material_1,20)
expansion,new_length = rod.expand_to_newtemp()

print(f'Linear Expansion : {expansion}mm/degree Celsius\nNew length : {new_length}mm')


    
