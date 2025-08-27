# Parent class (base class)
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self._storage = storage
        self.__battery = battery
        
# Method to display phone information
    def show_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage:{self._storage}, Battery:{self.__battery}mAH")
        
# Method to charge the phone        
    def charge(self):
        self.__battery = 100
        print(f"{self.brand} is fully charged!")
     
# Getter method (to safely access private attribute)   
    def get_battery(self):
        return self.__battery
  
# Child class (inherits from Smartphone)  
class Studyingphone(Smartphone):
    def __init__(self, brand, model, storage, battery, subject):
        super().__init__(brand, model, storage, battery)
        self.subject = subject
    
# Overriding the parent's show_info method (Polymorphism)
    def show_info(self):
        super().show_info()
        print(f"Subject: {self.subject}")

# Create objects from both classes
phone1 = Smartphone("Samsung", "A35", 256, 5000)
phone2 = Studyingphone("Apple", "Iphone 14", 512, 6000, "Math")

# Call their methods
phone1.show_info()
phone2.show_info()
print("The battery level of phone2 is:", phone2.get_battery())
phone2.charge()


# Parent class
class Vehicle:
    
    def move(self):
        pass

# Subclasses
class Car(Vehicle):
    
    def move(self):
        print("🚙 Drives on the road")

class Plane(Vehicle):
    
    def move(self):
        print("✈️ Flies in the sky")
class Boat(Vehicle):
    
    def move(self):
        print("🚢 Sails on water")

# Create a list of vehicles
vehicles = [Car(), Plane(), Boat()]

# Loop through the list and call move() for each
for v in vehicles:
    v.move()


         
    
        