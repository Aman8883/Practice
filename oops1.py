class Car: # creating a class

    total_cars=0 # creating a class varibale

    def __init__(self, brand, model): # defining an attribute and __init__ is a constructor
        self.__brand = brand 
        self.model = model
        Car.total_cars+=1
    
    def full_name(self):#defining a method
        return f"{self.__brand} {self.model}"

    def get_brand(self):# part of encapsulation, standard naming convention for getter and setter methods
        return self.__brand + " !!!!"
    
    def fuel_type(self):# Polymorphism
        return "Petrol/Diesel"
    
    @staticmethod# Static methods are methodsd which are not dependent on objects, they can be called from the class.
    def gen_des():# no need to declare self in static methods
        return(" Cars are a means of transport ")
    

my_car = Car("Toyota", "Prius") #creation of an object
#print(my_car.brand)
#print(my_car.model )
#print(my_car.full_name())


class ElectricCar(Car):  # Inheritance
    def __init__(self,brand,model,battery_size):# again a constructor and a new attribute
        super().__init__(brand,model) # super is used to inherit attributes of parent class,super init is used to inherit all the variables of the init function
        self.battery_size = battery_size # new variable 

    
    def fuel_type(self):
        return "Electric"

my_elec_wagonR = ElectricCar("Maruti","WagonR","100000kwh")
#print(my_elec_wagonR.brand)
#print(my_elec_wagonR.full_name())# the child class has access to all the methods in the parent class

# Encapsulation
# This means hiding a particular variable or making it private
# What we basically do is give user a controlled output rather than the normal output
# for this we simply have to add "__" before a variable name

#print(my_elec_wagonR.__brand) # prints the normal brand name attribute
#print(my_elec_wagonR.get_brand()) # prints the method/ controlled output

# study for setter

# Polymorphism
# Same name but different output, depending on input
# same function used with different object gives different outputs
 
print("Not wagonR ",my_car.fuel_type()) # gives output for my_Car
#rint("WagronR ",my_elec_wagonR.fuel_type()) # gives output for wagonr

print(Car.total_cars)
print(Car.gen_des()) # called directly from the class without using any object

print(isinstance(my_elec_wagonR,Car))# this will give true as eleccar is child class
# isinstance gives a boolean value depicting whether or not an object is an
#instance of xyz class or not
#syntax isinstance(obj_name, class_name

# Multiple inheritance

class Battery:
    def bat_ery(self):
        return " This is battery class "
    
class Engine:
    def eng_ne(self):
        return "This is engine class"
    
class Mynewwagon(Battery,Engine, Car):
    pass

my_super_wagonR = Mynewwagon("WagonR","Maruti")
print(my_super_wagonR.bat_ery())
print(my_super_wagonR.eng_ne())
